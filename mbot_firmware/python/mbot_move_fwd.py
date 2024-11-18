import time
import lcm
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
fwd_vel = 0.2   # m/s (adjust based on calibration)
turn_vel = 0.0  # rad/s

command = twist2D_t()
command.vx = fwd_vel
command.wz = turn_vel

# Send mbot velocity command
lc.publish("MBOT_VEL_CMD", command.encode())
# Let MBot drive for time = distance / velocity
distance = 0.5  # meters
time_to_drive = distance / fwd_vel  # seconds
time.sleep(time_to_drive)

# Send velocity = 0 to stop
command.vx = 0
command.wz = 0
lc.publish("MBOT_VEL_CMD", command.encode())
