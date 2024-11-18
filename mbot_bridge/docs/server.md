# The MBot Bridge Server

The MBot Bridge Server must be running in the background in order to use the API. This page describes the configuration and the protocol.

**Note:** This is an advanced guide for developers and instructors. For regular usage, see the [API documentation](index.md#api-documentation).

## Configuration

## MBot Bridge Protocol

The MBot Bridge defines a custom protocol in JSON to communicate over websockets.

**Note:** In most cases, you should use the API rather than creating and sending JSON messages directly. The API provides interfaces for common functionality and constructs JSON messages for you. See the [API documentation](index.md#api-documentation) for more details.

These fields are available for all types:
* `type`: The message type as an integer (see [Message Types](#message-types))

These types are included in some message types:
* `channel`: The LCM channel being read or published to
* `dtype`: The LCM message type being published or requested
* `as_bytes`: Whether the client wants raw LCM messages in bytes or a formatted string.
* `data`: A data payload as a string

### Message Types

The following types are defined:
* `REQUEST`: A request to read data. When a request is sent over a websocket connection, the server will respond with either a `RESPONSE` message or an `ERROR` message on the same websocket connection.

  This message type has the following JSON keys:
  * `type` (value: `0`): The message type.
  * `channel`: The LCM channel to read from.
  * `dtype` (Optional): The LCM message type to read. By default, the server will use its internal knowledge of the data type on the channel in question.
  * `as_bytes` (Optional. Default: False): If true, the server will return the *raw LCM message*, which is in bytes. The user is then responsible for knowing the LCM type and for decoding it. This is useful for efficiency and for large messages which are inefficient to pass as strings (e.g. large lists of floats). If false, the server will return a `RESPONSE` object with the data as a JSON object.

* `PUBLISH`: A request to publish data. There is no response to this message.

  This message type has the following JSON keys:
  * `type` (value: `1`): The message type.
  * `channel`: The LCM channel to publish to.
  * `dtype`: A string with the name of the LCM message type. The format should be `"my_lcm_type_pkg.my_type_t"`. If the type is in `mbot_lcm_msgs`, the package can be excluded (e.g. `"pose2D_t"`)
  * `data`: The LCM data to publish formatted as a JSON string.

* `RESPONSE`: A response from the server.

  This message type has the following JSON keys:
  * `type` (value: `2`): The message type.
  * `channel`: The LCM channel that was read.
  * `dtype`: A string with the name of the LCM message type. The format is `"my_lcm_type_pkg.my_type_t"`. If the type is in `mbot_lcm_msgs`, the package can be excluded (e.g. `"pose2D_t"`)
  * `data`: The data requested formatted as a JSON string.

* `SUBSCRIBE`: A request to subscribe to a certain channel. If the server receives a request to subscribe, it will send *all* data on the given channel back along the same websocket connection, until the connection is closed or an `UNSUBSCRIBE` message is sent.

  *Note:* This is mostly useful for languages that are not supported by LCM (e.g. Javascript). Subscribe functionality is not supported by the Python or C++ APIs. If using these languages, you should subscribe with LCM if you need this functionality.

  This message type has the following JSON keys:
  * `type` (value: `3`): The message type.
  * `channel`: The LCM channel to subscribe to.
  * `dtype` (Optional): The LCM message type to read. By default, the server will use its internal knowledge of the data type on the channel in question.
  * `as_bytes` (Optional. Default: False): If true, the server will return the *raw LCM message*, which is in bytes. The user is then responsible for knowing the LCM type and for decoding it. This is useful for efficiency and for large messages which are inefficient to pass as strings (e.g. large lists of floats). If false, the server will return a `RESPONSE` object with the data as a JSON object.

* `UNSUBSCRIBE`: A request to unsubscribe from a channel on the given websocket connection.

  This message type has the following JSON keys:
  * `type` (value: `4`): The message type.
  * `channel`: The LCM channel to unsubscribe from.

* `ERROR`: An error response from the server.

  This message type has the following JSON keys:
  * `type` (value: `-98`): The message type.
  * `data`: A string with the error message from the server.
