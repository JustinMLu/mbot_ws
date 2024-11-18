import time
import lcm
import sys
from mbot_lcm_msgs.twist2D_t import twist2D_t
from mbot_lcm_msgs.pose2D_t import pose2D_t

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=0")

# Reset the Odometry to 0
init_odometry = pose2D_t()
init_odometry.x = 0
init_odometry.y = 0
init_odometry.theta = 0

lc.publish("MBOT_ODOMETRY_RESET", init_odometry.encode())

# Set velocity
fwd_vel = 0.0   # m/s
turn_vel = 3.14  # rad/s

command = twist2D_t() # A twist2D_t command encodes forward and rotational speeds of the bot
command.vx = fwd_vel
command.wz = turn_vel

# Send mbot velocity command
lc.publish("MBOT_VEL_CMD",command.encode())
# Let MBot drive for 1 seconds
time.sleep(1)

# Send velocity = 0 to stop
command.vx = 0
command.wz = 0
lc.publish("MBOT_VEL_CMD",command.encode())