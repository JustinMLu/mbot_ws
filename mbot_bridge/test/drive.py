import time
from mbot_bridge.api import MBot

# Initialize a mbot object.
mbot = MBot()

# Read hostname.
print("MBot hostname:", mbot.read_hostname())

# Read the latest odometry message.
odom = mbot.read_odometry()
print("Odometry:", odom)

# Read the latest lidar scan.
ranges, thetas = mbot.read_lidar()
print("Ranges length:", len(ranges), "Thetas length:", len(thetas))

# Drive in a square.
vel = 0.5
mbot.drive(vel, 0, 0)
time.sleep(1)
mbot.drive(0, vel, 0)
time.sleep(1)
mbot.drive(-vel, 0, 0)
time.sleep(1)
mbot.drive(0, -vel, 0)
time.sleep(1)

# Make sure motors are stopped.
mbot.stop()
