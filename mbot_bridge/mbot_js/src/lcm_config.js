
let config = {
  LCM_ADDRESS: "udpm://239.255.76.67:7667?ttl=1",

  // Channels.
  ODOMETRY: {channel: "MBOT_ODOMETRY", dtype: "pose2D_t"},
  RESET_ODOMETRY: {channel: "MBOT_ODOMETRY_RESET", dtype: "pose2D_t"},
  CONTROLLER_PATH: {channel: "CONTROLLER_PATH", dtype: "path2D_t"},
  MOTOR_VEL_CMD: {channel: "MBOT_VEL_CMD", dtype: "twist2D_t"},
  LIDAR: {channel: "LIDAR", dtype: "lidar_t"},
  SLAM_MAP: {channel: "SLAM_MAP", dtype: "occupancy_grid_t"},
  SLAM_POSE: {channel: "SLAM_POSE", dtype: "pose2D_t"},
  MBOT_SYSTEM_RESET: {channel: "MBOT_SYSTEM_RESET", dtype: "mbot_slam_reset_t"}
}

export default config;
