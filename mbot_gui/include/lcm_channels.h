#ifndef MBOT_GUI_BOTLAB_LCM_CHANNELS_H
#define MBOT_GUI_BOTLAB_LCM_CHANNELS_H

/////// Data channels //////

#define MBOT_STATUS_CHANNEL "MBOT_STATUS"
#define MBOT_IMU_CHANNEL "MBOT_IMU"
#define MBOT_ENCODERS_CHANNEL "MBOT_ENCODERS"
#define LIDAR_CHANNEL "LIDAR"
#define WIFI_READINGS_CHANNEL "WIFI"
#define PATH_REQUEST_CHANNEL "PATH_REQUEST"

//////// Additional channels for processes that run on the Mbot -- odometry and motion_controller.
#define ODOMETRY_CHANNEL "MBOT_ODOMETRY"
#define ODOMETRY_RESET_CHANNEL "MBOT_ODOMETRY_RESET"
#define CONTROLLER_PATH_CHANNEL "CONTROLLER_PATH"

#define BOTGUI_GOAL_CHANNEL "BOTGUI_GOAL" //separate channel for lcm-server excluding the motion controller

/////// Command channels ///////

#define MBOT_MOTOR_COMMAND_CHANNEL "MBOT_MOTOR_VEL"

#define MBOT_TIMESYNC_CHANNEL "MBOT_TIMESYNC"
#define MESSAGE_CONFIRMATION_CHANNEL "MSG_CONFIRM"

#define MBOT_SYSTEM_RESET_CHANNEL "MBOT_SYSTEM_RESET"

/////// SLAM channels ///////

#define SLAM_MAP_CHANNEL "SLAM_MAP"
#define SLAM_POSE_CHANNEL "SLAM_POSE"
#define SLAM_PARTICLES_CHANNEL "SLAM_PARTICLES"

/////// Optitrack channels ///////

#define TRUE_POSE_CHANNEL "TRUE_POSE"

#endif // MBOT_GUI_BOTLAB_LCM_CHANNELS_H
