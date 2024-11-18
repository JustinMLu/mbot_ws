import json
import numpy as np


class MBotMessageType(object):
    INIT = 99
    REQUEST = 0
    PUBLISH = 1
    RESPONSE = 2
    SUBSCRIBE = 3
    UNSUBSCRIBE = 4
    ERROR = -98
    INVALID = -99


class BadMBotRequestError(Exception):
    pass


class MBotJSONMessage(object):
    def __init__(self, data=None, channel=None, dtype=None, rtype=None, as_bytes=False, from_json=False):
        if from_json:
            self.decode(data)
        else:
            if rtype not in [MBotMessageType.INIT, MBotMessageType.REQUEST,
                             MBotMessageType.PUBLISH, MBotMessageType.RESPONSE,
                             MBotMessageType.SUBSCRIBE, MBotMessageType.UNSUBSCRIBE,
                             MBotMessageType.ERROR, MBotMessageType.INVALID]:
                raise AttributeError(f"Invalid message type: {rtype}")
            self._request_type = rtype
            self._data = data
            self._channel = channel
            self._dtype = dtype
            self._as_bytes = as_bytes

    def data(self):
        return self._data

    def dtype(self):
        return self._dtype

    def type(self):
        return self._request_type

    def channel(self):
        return self._channel

    def as_bytes(self):
        return self._as_bytes

    def encode(self):
        if self._request_type == MBotMessageType.INIT:
            rtype = "init"
        elif self._request_type == MBotMessageType.PUBLISH:
            rtype = "publish"
        elif self._request_type == MBotMessageType.REQUEST:
            rtype = "request"
        elif self._request_type == MBotMessageType.RESPONSE:
            rtype = "response"
        elif self._request_type == MBotMessageType.SUBSCRIBE:
            rtype = "subscribe"
        elif self._request_type == MBotMessageType.UNSUBSCRIBE:
            rtype = "unsubscribe"
        elif self._request_type == MBotMessageType.ERROR:
            rtype = "error"
        else:
            rtype = "invalid"

        msg = {"type": rtype}

        if self._channel is not None:
            msg.update({"channel": self._channel})
        if self._dtype is not None:
            msg.update({"dtype": self._dtype})
        if self._request_type in [MBotMessageType.REQUEST, MBotMessageType.SUBSCRIBE]:
            msg.update({"as_bytes": self._as_bytes})
        if self._data is not None:
            # Special consideration for the lidar data because it's so big.
            if self._dtype == "lidar_t":
                # Round to 4 data points.
                self._data["ranges"] = np.round(self._data["ranges"], 4).tolist()
                self._data["thetas"] = np.round(self._data["thetas"], 4).tolist()

                # Remove times and intensities which are not used.
                self._data.pop("intensities", None)
                self._data.pop("times", None)

            msg.update({"data": self._data})

        return json.dumps(msg)

    def decode(self, data):
        raw_data = data
        # First try to load the data as JSON.
        try:
            data = json.loads(data)
        except json.decoder.JSONDecodeError:
            raise BadMBotRequestError(f"Message is not valid JSON: \"{raw_data}\"")

        # Get the type and channel for the request.
        try:
            request_type = data["type"]
        except KeyError:
            raise BadMBotRequestError("JSON request does not have a type attribute.")

        # Parse the type.
        try:
            request_type = getattr(MBotMessageType, request_type.upper())
        except AttributeError:
            raise BadMBotRequestError(f"Invalid request type: \"{request_type}\"")

        if request_type == MBotMessageType.INVALID:
            raise BadMBotRequestError(f"Invalid request type: \"{request_type}\"")

        channel = None
        if "channel" in data:
            channel = data["channel"]

        # The request should have a channel if it is a publish, subscribe or a request type.
        if request_type in (MBotMessageType.REQUEST, MBotMessageType.PUBLISH,
                            MBotMessageType.SUBSCRIBE, MBotMessageType.UNSUBSCRIBE) and channel is None:
            raise BadMBotRequestError("JSON request does not have a channel attribute.")

        # Read the data, if any.
        msg_data, dtype = None, None
        if "data" in data:
            msg_data = data["data"]
        if "dtype" in data:
            dtype = data["dtype"]

        # Whether the data should be returned in raw bytes.
        as_bytes = data["as_bytes"] if "as_bytes" in data else False

        # If this was a publish request, data is required.
        if request_type == MBotMessageType.PUBLISH and (msg_data is None or dtype is None):
            raise BadMBotRequestError("Publish was requested but data or data type is missing.")

        self._channel = channel
        self._data = msg_data
        self._dtype = dtype
        self._request_type = request_type
        self._as_bytes = as_bytes


class MBotJSONRequest(MBotJSONMessage):
    def __init__(self, channel, dtype=None, as_bytes=False):
        super().__init__(channel=channel, dtype=dtype, as_bytes=as_bytes, rtype=MBotMessageType.REQUEST)


class MBotJSONResponse(MBotJSONMessage):
    def __init__(self, data, channel, dtype):
        super().__init__(data, channel=channel, dtype=dtype, rtype=MBotMessageType.RESPONSE)


class MBotJSONPublish(MBotJSONMessage):
    def __init__(self, data, channel, dtype):
        super().__init__(data, channel=channel, dtype=dtype, rtype=MBotMessageType.PUBLISH)


class MBotJSONError(MBotJSONMessage):
    def __init__(self, msg):
        super().__init__(msg, rtype=MBotMessageType.ERROR)
