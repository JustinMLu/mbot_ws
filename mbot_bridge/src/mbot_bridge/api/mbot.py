import websockets
import asyncio
from mbot_bridge.utils import type_utils
from mbot_bridge.utils.json_messages import (
    MBotJSONRequest, MBotJSONPublish, MBotJSONMessage, MBotMessageType
)
from .lcm_config import LCMConfig


class MBot(object):
    """Utility class for controlling the mbot."""

    def __init__(self, host="localhost", port=5005, connect_timeout=5):
        self.uri = f"ws://{host}:{port}"
        self.connect_timeout = connect_timeout
        self.lcm_config = LCMConfig()

    """PUBLISHERS"""

    async def _send(self, ch, data, dtype):
        res = MBotJSONPublish(data, ch, dtype)
        try:
            async with websockets.connect(self.uri, open_timeout=self.connect_timeout) as websocket:
                await websocket.send(res.encode())
        except asyncio.exceptions.TimeoutError:
            print(f"[MBot API] ERROR: Cannot connect to MBot Bridge at: {self.uri}")
            return

    def drive(self, vx, vy, wz):
        data = {"vx": vx, "vy": vy, "wz": wz}
        asyncio.run(self._send(self.lcm_config.MOTOR_VEL_CMD.channel, data, self.lcm_config.MOTOR_VEL_CMD.dtype))

    def stop(self):
        self.drive(0, 0, 0)

    def reset_odometry(self):
        zero = {"x": 0, "y": 0, "theta": 0}
        asyncio.run(self._send(self.lcm_config.RESET_ODOMETRY.channel, zero, self.lcm_config.RESET_ODOMETRY.dtype))

    def drive_path(self, path):
        path_data = [{"x": p[0], "y": p[1], "theta": p[2] if len(p) == 3 else 0} for p in path]
        data = {"path_length": len(path), "path": path_data}
        asyncio.run(self._send(self.lcm_config.CONTROLLER_PATH.channel, data, self.lcm_config.CONTROLLER_PATH.dtype))

    """SUBSCRIBERS"""

    async def _request(self, ch, dtype=None, as_bytes=False):
        res = MBotJSONRequest(ch, dtype=dtype, as_bytes=as_bytes)
        try:
            async with websockets.connect(self.uri, open_timeout=self.connect_timeout) as websocket:
                await websocket.send(res.encode())

                # Wait for the response
                response = await websocket.recv()
        except asyncio.exceptions.TimeoutError:
            print(f"[MBot API] ERROR: Cannot connect to MBot Bridge at: {self.uri}")
            return

        if isinstance(response, bytes):
            assert dtype is not None, "Must provide data type to process data as bytes."
            try:
                msg = type_utils.decode(response, dtype)
            except type_utils.BadMessageError as e:
                print("[MBot API] ERROR:", e)
                return

            return msg
        # Convert this to a JSON message.
        response = MBotJSONMessage(response, from_json=True)

        # Check if this is an error. If so, print it and quit.
        if response.type() == MBotMessageType.ERROR:
            print("[MBot API] ERROR:", response.data())
            return

        # If this was a response as expected, convert it to an LCM message and return.
        if response.type() == MBotMessageType.RESPONSE:
            if ch == "HOSTNAME":
                # Hostname is not an LCM message.
                return response.data()
            try:
                msg = type_utils.dict_to_lcm_type(response.data(), response.dtype())
            except type_utils.BadMessageError as e:
                print("[MBot API] ERROR:", e)

            return msg
        else:
            print("[MBot API] ERROR: Got a bad response:", response.encode())

    def read_hostname(self):
        res = asyncio.run(self._request("HOSTNAME"))
        if res is not None:
            return res

        return "unknown"

    def read_odometry(self):
        res = asyncio.run(self._request(self.lcm_config.ODOMETRY.channel,
                                        self.lcm_config.ODOMETRY.dtype,
                                        as_bytes=True))
        if res is not None:
            return [res.x, res.y, res.theta]

        return []

    def read_slam_pose(self):
        res = asyncio.run(self._request(self.lcm_config.SLAM_POSE.channel,
                                        self.lcm_config.SLAM_POSE.dtype,
                                        as_bytes=True))
        if res is not None:
            return [res.x, res.y, res.theta]

        return []

    def read_lidar(self):
        res = asyncio.run(self._request(self.lcm_config.LIDAR.channel,
                                        self.lcm_config.LIDAR.dtype,
                                        as_bytes=True))
        if res is not None:
            return res.ranges, res.thetas

        return [], []

    def read_data(self, channel, dtype):
        res = asyncio.run(self._request(channel, dtype, as_bytes=True))
        return res
