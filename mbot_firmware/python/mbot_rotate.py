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
fwd_vel = 0.0   # m/s
turn_vel = 1.57  # rad/s (adjust based on calibration)

command = twist2D_t()
command.vx = fwd_vel
command.wz = turn_vel * 1 # -1 for right turn, 1 for left

# Send mbot velocity command
lc.publish("MBOT_VEL_CMD", command.encode())

# Let MBot drive for time = desired_angle / rotational_velocity
desired_angle = 3.14 # radians (pi / 2 is 90 degrees)

time_to_rotate = desired_angle / turn_vel  # seconds
time.sleep(time_to_rotate)

# Send velocity = 0 to stop
command.vx = 0
command.wz = 0
lc.publish("MBOT_VEL_CMD", command.encode())
