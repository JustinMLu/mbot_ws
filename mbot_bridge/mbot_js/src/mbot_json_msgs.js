
const MBotMessageType = {
  INIT: 99,
  REQUEST: 0,
  PUBLISH: 1,
  RESPONSE: 2,
  SUBSCRIBE: 3,
  UNSUBSCRIBE: 4,
  ERROR: -98,
  INVALID: -99
};


class MBotJSONMessage {
  constructor(data=null, ch=null, dtype=null, rtype=null) {
    this.data = data;
    this.channel = ch;
    this.dtype = dtype;
    this.rtype = rtype;
  }

  encode() {
    // Encode the type.
    let rtype = "invalid";
    if (this.rtype === MBotMessageType.INIT)
        rtype = "init";
    else if (this.rtype === MBotMessageType.PUBLISH)
        rtype = "publish";
    else if (this.rtype === MBotMessageType.REQUEST)
        rtype = "request";
    else if (this.rtype === MBotMessageType.RESPONSE)
        rtype = "response";
    else if (this.rtype === MBotMessageType.SUBSCRIBE)
        rtype = "subscribe";
    else if (this.rtype === MBotMessageType.UNSUBSCRIBE)
        rtype = "unsubscribe";
    else if (this.rtype === MBotMessageType.ERROR)
        rtype = "error";

    let msg = {"type": rtype};

    if (this.channel !== null) msg.channel = this.channel;
    if (this.dtype !== null) msg.dtype = this.dtype;
    if (this.data !== null) msg.data = this.data;

    return JSON.stringify(msg);
  }

  decode(data) {
    data = JSON.parse(data);

    // Get the type and channel for the request.
    if (data.type === undefined) {
      return;
    }
    let request_type = data.type;

    // except KeyError:
    //     raise BadMBotRequestError("JSON request does not have a type attribute.")

    if (request_type === "request")
      request_type = MBotMessageType.REQUEST;
    else if (request_type === "publish")
      request_type = MBotMessageType.PUBLISH;
    else if (request_type === "response")
      request_type = MBotMessageType.RESPONSE;
    else if (request_type === "error")
      request_type = MBotMessageType.ERROR;
    else if (request_type === "init")
      request_type = MBotMessageType.INIT;
    else
      request_type = MBotMessageType.INVALID;
    // TODO: raise error
    // raise BadMBotRequestError(f"Invalid request type: \"{request_type}\"")

    // Read the data, if any.
    let channel = null;
    let msg_data = null;
    let dtype = null;
    if (data.channel !== undefined) channel = data.channel;
    if (data.data !== undefined) msg_data = data.data;
    if (data.dtype !== undefined) dtype = data.dtype;

    // TODO: Raise errors for bad data combinations.

    this.channel = channel;
    this.data = msg_data;
    this.dtype = dtype;
    this.rtype = request_type;
  }
}

export { MBotMessageType, MBotJSONMessage };
