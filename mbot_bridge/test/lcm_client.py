import lcm
import time
from mbot_lcm_msgs import pose2D_t

_lcm = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

cmd = pose2D_t()
cmd.x = 0
cmd.y = 0
cmd.theta = 0
# for i in range(10):
#     print(f"PUB:  vx: {cmd.x} vy: {cmd.y} wz: {cmd.theta}")
#     _lcm.publish("SLAM_POSE", cmd.encode())
#     time.sleep(2)
#     cmd.x += 1


while True:
    cmd.utime = time.time_ns() // 1000
    _lcm.publish("MBOT_ODOMETRY", cmd.encode())
    time.sleep(0.1)
