#!/bin/python3

import yaml
import asyncio
import signal
import select
import logging
import threading
import websockets
import time

import lcm
from mbot_bridge.utils import type_utils
from mbot_bridge.utils.json_messages import (
    MBotJSONMessage, MBotJSONResponse, MBotJSONError,
    MBotMessageType, BadMBotRequestError
)


class LCMMessageQueue(object):
    def __init__(self, channel, dtype, queue_size=1):
        self.channel = channel
        self.dtype = dtype
        self.queue_size = queue_size

        self._queue = []
        self._lock = threading.Lock()
        self._last_push_time = None

    def push(self, msg):
        self._lock.acquire()
        # Add the current message to the back of the queue.
        self._queue.append(msg)
        # Remove old messages if necessary.
        while len(self._queue) > self.queue_size:
            self._queue.pop(0)
        # Keep track of the last message time.
        self._last_push_time = time.time()
        self._lock.release()

    def latest(self, decode=True):
        latest = None
        self._lock.acquire()
        if len(self._queue) > 0:
            latest = self._queue[-1]
        self._lock.release()

        # Decode to LCM type if requested.
        if decode:
            latest = type_utils.decode(latest, self.dtype)

        return latest

    def latest_utime(self):
        latest = None
        self._lock.acquire()
        if len(self._queue) > 0:
            latest = self._queue[-1]
        self._lock.release()
        latest = type_utils.decode(latest, self.dtype)
        return latest.utime

    def pop(self, decode=False):
        first = None
        self._lock.acquire()
        if len(self._queue) > 0:
            first = self._queue.pop(0)
        self._lock.release()

        # Decode to LCM type if requested.
        if decode:
            first = type_utils.decode(first, self.dtype)

        return first

    def empty(self):
        return len(self._queue) == 0

    def header(self):
        return {"channel": self.channel,
                "dtype": self.dtype,
                "queue_size": self.queue_size}

    def active(self, stale_threshold=10):
        self._lock.acquire()
        if self._last_push_time is None:
            active = False
        else:
            active = time.time() - self._last_push_time < stale_threshold
        self._lock.release()
        return active


class MBotBridgeServer(object):
    def __init__(self, lcm_address, subs,
                 ignore_channels=[], map_channel="SLAM_MAP",
                 lcm_type_modules=["mbot_lcm_msgs"], lcm_timeout=1000,
                 hostfile="/etc/hostname", discard_msgs=-1):
        self._hostname = self._read_hostname(hostfile)
        self._loop = None
        self._map_channel = map_channel
        self.lcm_type_modules = lcm_type_modules
        self.discard_msgs = discard_msgs

        # LCM setup.
        self._lcm_timeout = lcm_timeout  # This is how long to timeout in the LCM handle call.
        self._lcm = lcm.LCM(lcm_address)

        logging.info(f"Hostname: {self._hostname}")
        logging.info(f"Connecting to LCM on address: {lcm_address}")

        self._msg_managers = {}
        self._subs = {}
        self._ignore_channels = ignore_channels

        if isinstance(subs, list):
            # The user has provided a list of channels to subscribe to, so only subscribe to these.
            logging.info("Listening to only provided channels.")
            for channel in subs:
                ch, lcm_type = channel["channel"], channel["type"]
                self._init_channel(ch, lcm_type=lcm_type)
                self._lcm.subscribe(ch, self.listener)
        elif subs == 'all':
            # Listen to all the available channels.
            logging.info("Listening to all published channels.")
            self._lcm.subscribe(".*", self.listener)
        else:
            logging.error(f"Cannot interpret subs configuration: {subs}")
            raise Exception("Bad arguments provided")

        self._running = True
        self._lock = threading.Lock()

        logging.info("MBot Bridge Server running!")

    async def stop(self, *args):
        self._lock.acquire()
        self._running = False
        self._lock.release()

        # Stop any websockets that might still be there.
        for _, connections in self._subs.items():
            for ws in connections:
                if ws.open:
                    await ws.close()

    def running(self):
        self._lock.acquire()
        res = self._running
        self._lock.release()
        return res

    def _read_hostname(self, hostfile):
        if not os.path.exists(hostfile):
            logging.warning(f"Host file does not exist, hostname will be empty. Host file: {hostfile}")
            return ""

        # Read the robot's host name.
        with open(hostfile, 'r') as f:
            name = f.read()

        return name.strip()

    def _latest_as_msg(self, ch, decode=True):
        latest = self._msg_managers[ch].latest(decode)
        if decode:
            latest = type_utils.lcm_type_to_dict(latest)  # Convert to dictionary, only message is decoded.
        # Wrap the response data for sending over the websocket.
        res = MBotJSONResponse(latest, ch, self._msg_managers[ch].dtype)
        return res

    def _init_channel(self, channel, lcm_type=None, data=None):
        # If we already have this channel, return success.
        if channel in self._msg_managers.keys():
            return True

        # If we are ignoring this channel, return and don't add it.
        if channel in self._ignore_channels:
            return False

        # If the user did not specify a channel, try to find it.
        if lcm_type is None:
            if data is None:
                logging.warn(f"Can't initialize channel without either the type or data: {channel}")
                return False

            try:
                lcm_type = type_utils.find_lcm_type(data, self.lcm_type_modules)
            except type_utils.BadMessageError as e:
                logging.warn(f"Can't find a valid message type for channel: {channel}. Ignoring in future.")
                self._ignore_channels.append(channel)
                return False

        # Add this channel to the message queue.
        logging.info(f"Listening on channel: {channel} ({lcm_type})")
        self._subs.update({channel: []})
        self._msg_managers.update({channel: LCMMessageQueue(channel, lcm_type)})
        return True

    def listener(self, channel, data):
        # Ignore any data on an ignore channel.
        if channel in self._ignore_channels:
            return

        if channel not in self._msg_managers.keys():
            # If we have never seen this channel before, try to initialize it. If it fails, ignore.
            if not self._init_channel(channel, data=data):
                return

        self._msg_managers[channel].push(data)

        # If there are subscribers, send them the data.
        if len(self._subs[channel]) > 0:
            # res = self._msg_managers[channel].latest(decode=True)
            res = self._latest_as_msg(channel, decode=True)
            for ws_sub in self._subs[channel]:
                if not ws_sub.open:
                    self._subs[channel].remove(ws_sub)
                    continue

                try:
                    self._loop.run_until_complete(ws_sub.send(res.encode()))
                except (websockets.exceptions.ConnectionClosedOK,
                        websockets.exceptions.ConnectionClosedError,
                        RuntimeError):
                    # If this websocket is closed, remove it.
                    logging.debug(f"Websocket ID {ws_sub.id} - Disconnected and unsubscribed from {channel}")
                    self._subs[channel].remove(ws_sub)

    def handleOnce(self):
        # This is a non-blocking handle, which only calls handle if a message is ready.
        rfds, wfds, efds = select.select([self._lcm.fileno()], [], [], 0)
        if rfds:
            self._lcm.handle()

    def lcm_loop(self):
        self._loop = asyncio.new_event_loop()
        while self.running():
            # This will block for a maximum of _lcm_timeout milliseconds, so it
            # might slow stopping the server, but it's less expensive than using
            # the non-blocking handleOnce.
            self._lcm.handle_timeout(self._lcm_timeout)

    def _subscribe(self, ws, channel):
        self._subs[channel].append(ws)

    async def _unsubscribe(self, ws, channel=None):
        await ws.close()
        self._subs[channel].remove(ws)

    async def process_msg(self, websocket, message):
        try:
            request = MBotJSONMessage(message, from_json=True)
        except BadMBotRequestError as e:
            # If something went wrong parsing this request, send the error message then continue.
            msg = f"Bad MBot request. Ignoring. BadMBotRequestError: {e}"
            logging.warning(f"{websocket.id} - {msg}")
            err = MBotJSONError(msg)
            await websocket.send(err.encode())
            return

        if request.type() == MBotMessageType.REQUEST:
            res = self.handle_request(request, websocket.id)
            if not isinstance(res, bytes):
                # If the result is in bytes, skip the encoding and send it directly.
                res = res.encode()
            await websocket.send(res)
        elif request.type() == MBotMessageType.PUBLISH:
            try:
                # Publish the data sent over the websocket.
                pub_msg = type_utils.dict_to_lcm_type(request.data(), request.dtype())
                pub_msg.utime = time.time_ns() // 1000
                self._lcm.publish(request.channel(), pub_msg.encode())
            except type_utils.BadMessageError as e:
                # If the type or data is bad, send back an error message.
                msg = (f"Bad MBot publish. Bad message type ({request.dtype()}) or data (\"{request.data()}\"). "
                       f"AttributeError: {e}")
                logging.warning(f"{websocket.id} - {msg}")
                err = MBotJSONError(msg)
                await websocket.send(err.encode())
        elif request.type() == MBotMessageType.SUBSCRIBE:
            ch = request.channel()
            if ch not in self._msg_managers:
                # If the channel being requested does not exist, return an error.
                msg = f"Bad subscribe request. No channel: {ch}"
                logging.warning(f"{websocket.id} - {msg}")
                err = MBotJSONError(msg)
                await websocket.send(err.encode())
            else:
                logging.debug(f"Websocket ID {websocket.id} - Subscribed to channel {request.channel()}")
                self._subscribe(websocket, request.channel())
        elif request.type() == MBotMessageType.UNSUBSCRIBE:
            ch = request.channel()
            if ch not in self._msg_managers:
                # If the channel being requested does not exist, return an error.
                msg = f"Bad unsubscribe request. No channel: {ch}"
                logging.warning(f"{websocket.id} - {msg}")
                err = MBotJSONError(msg)
                await websocket.send(err.encode())
            else:
                logging.debug(f"Websocket ID {websocket.id} - Unsubscribed from channel {request.channel()}")
                await self._unsubscribe(websocket, request.channel())

    def handle_request(self, request, ws_id):
        ch = request.channel()
        if ch == "HOSTNAME":
            # If hostname, return the hostname as a string.
            res = MBotJSONResponse(self._hostname, ch, "")
            return res
        elif ch == "CHANNELS":
            # If channels, return the list of current subscriptions.
            subs = []
            for _, v in self._msg_managers.items():
                # Only return active channels.
                if v.active():
                    subs.append(v.header())
            res = MBotJSONResponse(subs, ch, "")
            return res
        elif ch not in self._msg_managers:
            # If the channel being requested does not exist, return an error.
            msg = f"Bad MBot request. No channel: {ch}"
            logging.warning(f"{ws_id} - {msg}")
            err = MBotJSONError(msg)
            return err
        elif self._msg_managers[ch].empty():
            msg = f"No data on channel: {ch}"
            logging.warning(f"{ws_id} - {msg}")
            err = MBotJSONError(msg)
            return err
        else:
            # Get the newest data and send it as bytes.
            if request.as_bytes():
                # This msg should be returned as raw bytes.
                res = self._msg_managers[ch].latest(decode=False)
            elif ch == self._map_channel:
                # If the map was requested, but not as bytes, use the special
                # function to ensure the cells are returned as bytes.
                latest = type_utils.occupancy_grid_to_byte_dict(self._msg_managers[ch].latest(False))
                # Wrap the response data for sending over the websocket.
                res = MBotJSONResponse(latest, ch, self._msg_managers[ch].dtype)
            else:
                res = self._latest_as_msg(ch, decode=True)

            if self.discard_msgs > 0:
                message_staleness_us = time.time_ns() // 1000 - self._msg_managers[ch].latest_utime()
                if message_staleness_us > self.discard_msgs * 1E6:
                    # Remove from the queue
                    msg = f"Data on channel {ch} is old."
                    logging.warning(f"Old data on channel: {ch} of staleness {message_staleness_us} us discarded")
                    self._msg_managers[ch].pop()
                    err = MBotJSONError(msg)
                    return err

            return res

    async def handler(self, websocket):
        logging.debug(f"Websocket connected with ID: {websocket.id}")

        try:
            # Handle all incoming messages from the websocket.
            async for message in websocket:
                logging.debug(f"Message from WS {websocket.id}: {message}")
                await self.process_msg(websocket, message)
        except websockets.exceptions.ConnectionClosedOK:
            logging.debug(f"Websocket connection closed: {websocket.id}")
        except websockets.exceptions.ConnectionClosedError as e:
            logging.warning(f"Websocket ID {websocket.id} - Closed with error: {e}")


async def main(args):
    # Set the stop condition when receiving SIGTERM or SIGINT.
    loop = asyncio.get_running_loop()
    stop = asyncio.Future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)
    loop.add_signal_handler(signal.SIGINT, stop.set_result, None)
    lcm_manager = MBotBridgeServer(args.lcm_address, subs=args.subs,
                                   ignore_channels=args.ignore_channels,
                                   lcm_type_modules=args.lcm_type_modules,
                                   hostfile=args.host_file, discard_msgs=args.discard_msgs)

    # Not awaiting the task will cause it to be stoped when the loop ends.
    asyncio.create_task(asyncio.to_thread(lcm_manager.lcm_loop))

    async with websockets.serve(
        lcm_manager.handler,
        host="",
        port=args.port,
        reuse_port=True,
    ):
        await stop
        await lcm_manager.stop()

    logging.info("MBot Bridge exited cleanly.")


def load_args(conf="config/default.yml"):
    parser = argparse.ArgumentParser(description="MBot Bridge Server.")
    parser.add_argument("--config", type=str, default=conf, help="Configuration file.")
    parser.add_argument("--port", type=int, default=5005, help="Websocket port.")
    parser.add_argument("--log-file", type=str, default="mbot_bridge_server.log", help="Log file.")
    parser.add_argument("--log", type=str, default="INFO", help="Log level.")
    parser.add_argument("--max-log-size", type=int, default=2 * 1024 * 1024, help="Max log size.")
    parser.add_argument("--host-file", type=str, default="/etc/hostname", help="Hostname file.")
    parser.add_argument("--discard-msgs", type=float, default=-1, help="Discard stale msgs after X seconds.")

    args = parser.parse_args()

    # Turn the logging level into the correct form.
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {args.log}')
    args.log = numeric_level

    return args


def load_config(args):
    # Read the configuration file.
    logging.info(f"Reading configuration from: {args.config}")
    with open(args.config, 'r') as f:
        config = yaml.load(f, Loader=yaml.Loader)

    # Extract data from the config file.
    args.lcm_address = config["lcm_address"]
    subs = config["subs"]
    # Confirm subs where either a list or equal to "all".
    if subs != "all" and not isinstance(subs, list):
        logging.error(f"Config parameter \'subs\' must be either a list of channel data or the string \'all\'. " +
                      f"Got: {subs} (type: {type(subs)})")
        raise Exception("Bad config file")

    args.subs = subs

    args.ignore_channels = config["ignore_channels"] if "ignore_channels" in config.keys() else []
    lcm_type_modules = config["lcm_type_modules"] if "lcm_type_modules" in config.keys() else ["mbot_lcm_msgs"]

    # Confirm that the LCM modules are loadable.
    good_type_modules = []
    for pkg in lcm_type_modules:
        try:
            importlib.import_module(pkg)
            good_type_modules.append(pkg)
        except ModuleNotFoundError as e:
            logging.warning(f"No LCM type module named: \'{pkg}\'. Ignoring.")
    if len(good_type_modules) < 1:
        # If there are no valid types, add the default.
        logging.warning("No valid LCM type modules provided. Using default: \'mbot_lcm_msgs\'")
        good_type_modules = ["mbot_lcm_msgs"]
    args.lcm_type_modules = good_type_modules

    return args


if __name__ == "__main__":
    import os
    import argparse
    import importlib
    from . import config
    from logging import handlers

    DEFAULT_CONFIG = os.path.join(config.__path__[0], 'default.yml')

    args = load_args(DEFAULT_CONFIG)

    # Setup logging.
    file_handler = handlers.RotatingFileHandler(args.log_file, maxBytes=args.max_log_size)
    logging.basicConfig(level=args.log,
                        handlers=[
                            file_handler,
                            logging.StreamHandler()  # Also print to terminal.
                        ],
                        format='%(asctime)s [%(name)s] [%(levelname)s] %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    # Websocket messages are too noisy, make sure they aren't higher than warning.
    logging.getLogger("websockets").setLevel(logging.WARNING)

    load_config(args)

    # Log all the arguments before running.
    logging.info("Starting the MBot Bridge with arguments:")
    for arg in vars(args):
        logging.info(f"\t{arg}: {getattr(args, arg)}")

    asyncio.run(main(args))
