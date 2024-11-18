# MBot Bridge Documentation

The MBot Bridge is a tool for end-user applications on the MBot without LCM. There are two pieces to the MBot Bridge:

1. The MBot Bridge Server: A process that runs in the background and interfaces with the other MBot programs.
2. The MBot Bridge API: An API for interfacting with the MBot, available in C++, Python, and Javascript.

The MBot Bridge lets a user read or publish data through websocket requests. Many of the common MBot apps, like the web app or the LCM monitor, rely on the MBot Bridge.

## Quickstart

The MBot Bridge is designed to be easy to use. You can run it (once [installed](../README.md#install-instructions)) with this command:
```bash
python -m mbot_bridge.server [--config [PATH/TO/CONFIG]]
```

**Note:** On many MBots, the MBot Bridge is configured to run on startup. Before running the server, check if it's already running with command `sudo systemctl status mbot-bridge.service`. If it is, skip the above step!

### Python

To use the MBot Bridge API in Python, do:
```python
from mbot_bridge.api import MBot
mbot = MBot()
```
You can then use the `mbot` object to send and read messages. This example drives the robot forward for one second:
```python
import time
mbot.drive(0.5, 0, 0)  # Set the robot forward velocity to 0.5 m/s.
time.sleep(1)          # Sleep for one second.
mbot.stop()            # Stop the robot.
```
You can also read data from the MBot. For example, this code reads the latest odometry data:
```python
odom = mbot.read_odometry()  # Returns the odometry in format [x, y, theta].
```

### C++

To use the MBot Bridge API in C++, do:
```cpp
#include <mbot_bridge/robot.h>

int main(int argc, char* argv[])
{
    mbot_bridge::MBot mbot;
}
```
You can then use the `mbot` object to read and publish data.

## When to use the MBot Bridge API

The MBot Bridge API is meant to make it easy and quick to program the MBot. It's intended for quick prototyping or beginner programmers.  Use the MBot Bridge API if:
* You want to write single-threaded code,
* You don't want to use LCM,
* You want to read the latest data and don't care about a bit of latency or missed messages.

## When not to use the MBot Bridge API

The MBot Bridge API provides a user-friendly interfact at the cost of some efficiency. In the background, it subscribes to a bunch of LCM channels and stores the data. Then, it waits for websocket requests for the data, formats it, then returns it. For many applications, you probably don't care about a few fractions of a second of delay. For applications where this delay does matter, you can also program the MBot by directly interfacting with the LCM code.

You should choose this option if:
* You need to write code where it's important to not have delays reading the messages (e.g. SLAM or a low-level controller),
* You can't miss any messages,
* You have a time-critical application.

## For developers (Advanced)

A common pattern for tools for the MBot (like visualizers, web apps, or command line utilities) is to aggregate LCM data and then do something with it. If you are building such a tool, you should first check if you can use the MBot Bridge instead of writing your own LCM manager. These types of applications can be expensive, so it's best to use the existing MBot Bridge Server instead of adding a new process that does the same thing.

## API Documentation

The following languages are supported in the current API:
* [Python](python-api.md)
* [C++](cpp-api.md)
* [Javascript](js-api.md)

**Advanced Usage:** You can interface with the MBot Bridge Server directly through websockets (for example, if you want to use it in an unsupported language). See the [server documentation](server.md) for more details.
