import time
import lcm
import sys
from mbot_lcm_msgs.twist2D_t import twist2D_t
from mbot_lcm_msgs.pose2D_t import pose2D_t
from mbot_lcm_msgs.path2D_t import path2D_t

# The waypoints (x, y, theta) in the global frame
# Updated to match the working C++ implementation
drive_path = [
    (0.0, 0.0, 0.0),                     # Waypoint 0: Starting position
    (0.61, 0.0, 0.0),                    # Waypoint 1: Go straight 61 cm
    (0.61, 0.0, -1.5708),                # Waypoint 2: Turn right (-90 degrees)
    (0.61, -0.61, -1.5708),              # Waypoint 3: Go straight 61 cm
    (0.61, -0.61, 0.0),                  # Waypoint 4: Turn left (+90 degrees)
    (1.22, -0.61, 0.0),                  # Waypoint 5: Go straight 61 cm
    (1.22, -0.61, 1.5708),                # Waypoint 6: Turn left (+90 degrees)
    (1.22, 0.61, 1.5708),                 # Waypoint 7: Go straight 122 cm
    (1.22, 0.61, 0.0),                    # Waypoint 8: Turn right (-90 degrees)
    (1.83, 0.61, 0.0),                    # Waypoint 9: Go straight 61 cm
    (3.05, 0.61, 0.0),                    # Waypoint 10: Go straight 122 cm
    (3.05, 0.61, 1.5708),                 # Waypoint 11: Turn left (+90 degrees)
    (3.05, 1.22, 1.5708),                 # Waypoint 12: Go straight 61 cm
    (2.44, 1.22, 3.1416),                 # Waypoint 13: Turn left (+90 degrees)
    (2.44, 1.83, 1.5708),                 # Waypoint 14: Go straight 61 cm
    (2.44, 1.83, 1.5708),                 # Waypoint 15: Final orientation
]

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=0")

# Reset the Odometry to 0
init_odometry = pose2D_t()
init_odometry.x = 0
init_odometry.y = 0
init_odometry.theta = 0
lc.publish("MBOT_ODOMETRY_RESET", init_odometry.encode())

# Set the max speed
vel_limits = twist2D_t()
vel_limits.vx = 0.15
vel_limits.wz = 3.14

lc.publish("MBOT_MAX_VEL", vel_limits.encode())

# Get the path command
command = path2D_t()
command.path = []

# Build up path
for x, y, theta in drive_path:
    pose = pose2D_t()
    pose.x = x
    pose.y = y
    pose.theta = theta
    
    command.path.append(pose)

command.path_length = len(command.path)

# Send mbot velocity command
lc.publish("CONTROLLER_PATH", command.encode())
