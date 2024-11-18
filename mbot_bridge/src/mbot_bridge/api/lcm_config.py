

class MBotChannel(object):
    def __init__(self, channel, dtype):
        self.channel = channel
        self.dtype = dtype


class LCMConfig(object):
    LCM_ADDRESS = "udpm://239.255.76.67:7667?ttl=1"

    # Channels.
    ODOMETRY = MBotChannel("MBOT_ODOMETRY", "pose2D_t")
    RESET_ODOMETRY = MBotChannel("MBOT_ODOMETRY_RESET", "pose2D_t")
    CONTROLLER_PATH = MBotChannel("CONTROLLER_PATH", "path2D_t")
    MOTOR_VEL_CMD = MBotChannel("MBOT_VEL_CMD", "twist2D_t")
    LIDAR = MBotChannel("LIDAR", "lidar_t")
    SLAM_MAP = MBotChannel("SLAM_MAP", "occupancy_grid_t")
    SLAM_POSE = MBotChannel("SLAM_POSE", "pose2D_t")
