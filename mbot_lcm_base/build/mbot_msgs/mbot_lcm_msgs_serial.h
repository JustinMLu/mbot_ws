/*
 * This header file was autogenerated by the LCM to C header file generator.
 * Included LCM types:
 *   twist2D_t
 *   timestamp_t
 *   pose2D_t
 *   mbot_slam_reset_t
 *   mbot_encoders_t
 *   point3D_t
 *   joy_t
 *   mbot_imu_t
 *   mbot_motor_pwm_t
 *   pose3D_t
 *   mbot_motor_vel_t
 *   twist3D_t
 *   mbot_message_received_t
 *   particle_t
 *   slam_status_t
 *   exploration_status_t
 *   planner_request_t
 *   mbot_apriltag_t
 */

#ifndef SERIAL_MSG_H
#define SERIAL_MSG_H
#pragma once
#include <stdint.h>
#include <string.h>

#include <stdbool.h>

typedef struct __attribute__((__packed__)) serial_twist2D_t {
    int64_t utime;
    float vx;
    float vy; // this should be 0 when use differential drive 
    float wz;
} serial_twist2D_t;

static inline int twist2D_t_deserialize(uint8_t* src, serial_twist2D_t* dest);
static inline int twist2D_t_serialize(serial_twist2D_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_timestamp_t {
    int64_t utime;
} serial_timestamp_t;

static inline int timestamp_t_deserialize(uint8_t* src, serial_timestamp_t* dest);
static inline int timestamp_t_serialize(serial_timestamp_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_pose2D_t {
    int64_t utime;
    float x;
    float y;
    float theta;
} serial_pose2D_t;

static inline int pose2D_t_deserialize(uint8_t* src, serial_pose2D_t* dest);
static inline int pose2D_t_serialize(serial_pose2D_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_mbot_slam_reset_t {
    int64_t utime;
    int32_t slam_mode; // mapping_only=0, action_only=1, localization_only=2, full_slam=3
    char slam_map_location[256]; // only necessary when for localization-only and action_only modes
    bool retain_pose; // Whether to keep the pose when resetting.
} serial_mbot_slam_reset_t;

static inline int mbot_slam_reset_t_deserialize(uint8_t* src, serial_mbot_slam_reset_t* dest);
static inline int mbot_slam_reset_t_serialize(serial_mbot_slam_reset_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_mbot_encoders_t {
    int64_t utime;
    int64_t ticks[3]; // no units
    int32_t delta_ticks[3]; // no units
    int32_t delta_time; // [usec]
} serial_mbot_encoders_t;

static inline int mbot_encoders_t_deserialize(uint8_t* src, serial_mbot_encoders_t* dest);
static inline int mbot_encoders_t_serialize(serial_mbot_encoders_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_point3D_t {
    int64_t utime;
    float x;
    float y;
    float z;
} serial_point3D_t;

static inline int point3D_t_deserialize(uint8_t* src, serial_point3D_t* dest);
static inline int point3D_t_serialize(serial_point3D_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_joy_t {
    int64_t timestamp;
    float left_analog_X;
    float left_analog_Y;
    float right_analog_X;
    float right_analog_Y;
    float right_trigger;
    float left_trigger;
    float dpad_X;
    float dpad_Y;
    int8_t button_A;
    int8_t button_B;
    int8_t button_2; // not used
    int8_t button_X;
    int8_t button_Y;
    int8_t button_5; // not used
    int8_t button_l1;
    int8_t button_r1;
    int8_t button_l2;
    int8_t button_r2;
    int8_t button_select;
    int8_t button_start;
    int8_t button_12; // not used
    int8_t button_left_analog;
    int8_t button_right_analog;
    int8_t button_15; //not used
} serial_joy_t;

static inline int joy_t_deserialize(uint8_t* src, serial_joy_t* dest);
static inline int joy_t_serialize(serial_joy_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_mbot_imu_t {
    int64_t utime;
    float gyro[3];
    float accel[3];
    float mag[3];
    float angles_rpy[3]; // roll (x), pitch (y), yaw, (z)
    float angles_quat[4]; // quaternion
    float temp;
} serial_mbot_imu_t;

static inline int mbot_imu_t_deserialize(uint8_t* src, serial_mbot_imu_t* dest);
static inline int mbot_imu_t_serialize(serial_mbot_imu_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_mbot_motor_pwm_t {
    int64_t utime;
    float pwm[3]; // [-1.0..1.0]
} serial_mbot_motor_pwm_t;

static inline int mbot_motor_pwm_t_deserialize(uint8_t* src, serial_mbot_motor_pwm_t* dest);
static inline int mbot_motor_pwm_t_serialize(serial_mbot_motor_pwm_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_pose3D_t {
    int64_t utime;
    float x;
    float y;
    float z;
    float angles_rpy[3];
    float angles_quat[4];
} serial_pose3D_t;

static inline int pose3D_t_deserialize(uint8_t* src, serial_pose3D_t* dest);
static inline int pose3D_t_serialize(serial_pose3D_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_mbot_motor_vel_t {
    int64_t utime;
    float velocity[3]; // [rad/s]
} serial_mbot_motor_vel_t;

static inline int mbot_motor_vel_t_deserialize(uint8_t* src, serial_mbot_motor_vel_t* dest);
static inline int mbot_motor_vel_t_serialize(serial_mbot_motor_vel_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_twist3D_t {
    int64_t utime;
    float vx;
    float vy;
    float vz;
    float wx;
    float wy;
    float wz;
} serial_twist3D_t;

static inline int twist3D_t_deserialize(uint8_t* src, serial_twist3D_t* dest);
static inline int twist3D_t_serialize(serial_twist3D_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_mbot_message_received_t {
    int64_t utime; // Time of confirmation message creation
    int64_t creation_time; // time of message creation (assumption that this will be unique between messages)
    char channel[256]; //name of channel 
} serial_mbot_message_received_t;

static inline int mbot_message_received_t_deserialize(uint8_t* src, serial_mbot_message_received_t* dest);
static inline int mbot_message_received_t_serialize(serial_mbot_message_received_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_particle_t {
    serial_pose2D_t pose; // (x,y,theta) pose estimate
    serial_pose2D_t parent_pose; // (x,y,theta) of the prior pose the new estimate came from
    double weight; // normalized weight of the particle as computed by the sensor model
} serial_particle_t;

static inline int particle_t_deserialize(uint8_t* src, serial_particle_t* dest);
static inline int particle_t_serialize(serial_particle_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_slam_status_t {
    int64_t utime;
    int32_t slam_mode; // mapping_only=0, action_only=1, localization_only=2, full_slam=3
    char map_path[256]; // Path to where the map is stored.
} serial_slam_status_t;

static inline int slam_status_t_deserialize(uint8_t* src, serial_slam_status_t* dest);
static inline int slam_status_t_serialize(serial_slam_status_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_exploration_status_t {
    int64_t utime;
    int8_t state;
    int8_t status;
} serial_exploration_status_t;

static inline int exploration_status_t_deserialize(uint8_t* src, serial_exploration_status_t* dest);
static inline int exploration_status_t_serialize(serial_exploration_status_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_planner_request_t {
    int64_t utime;
    serial_pose2D_t goal;
    bool require_plan;
} serial_planner_request_t;

static inline int planner_request_t_deserialize(uint8_t* src, serial_planner_request_t* dest);
static inline int planner_request_t_serialize(serial_planner_request_t* src, uint8_t* dest);


typedef struct __attribute__((__packed__)) serial_mbot_apriltag_t {
    int32_t tag_id;
    serial_pose3D_t pose;
} serial_mbot_apriltag_t;

static inline int mbot_apriltag_t_deserialize(uint8_t* src, serial_mbot_apriltag_t* dest);
static inline int mbot_apriltag_t_serialize(serial_mbot_apriltag_t* src, uint8_t* dest);


int twist2D_t_deserialize(uint8_t* src, serial_twist2D_t* dest) {
    memcpy(dest, src, sizeof(serial_twist2D_t));
    return 1;
}

int twist2D_t_serialize(serial_twist2D_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_twist2D_t));
    return 1;
}


int timestamp_t_deserialize(uint8_t* src, serial_timestamp_t* dest) {
    memcpy(dest, src, sizeof(serial_timestamp_t));
    return 1;
}

int timestamp_t_serialize(serial_timestamp_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_timestamp_t));
    return 1;
}


int pose2D_t_deserialize(uint8_t* src, serial_pose2D_t* dest) {
    memcpy(dest, src, sizeof(serial_pose2D_t));
    return 1;
}

int pose2D_t_serialize(serial_pose2D_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_pose2D_t));
    return 1;
}


int mbot_slam_reset_t_deserialize(uint8_t* src, serial_mbot_slam_reset_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_slam_reset_t));
    return 1;
}

int mbot_slam_reset_t_serialize(serial_mbot_slam_reset_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_slam_reset_t));
    return 1;
}


int mbot_encoders_t_deserialize(uint8_t* src, serial_mbot_encoders_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_encoders_t));
    return 1;
}

int mbot_encoders_t_serialize(serial_mbot_encoders_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_encoders_t));
    return 1;
}


int point3D_t_deserialize(uint8_t* src, serial_point3D_t* dest) {
    memcpy(dest, src, sizeof(serial_point3D_t));
    return 1;
}

int point3D_t_serialize(serial_point3D_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_point3D_t));
    return 1;
}


int joy_t_deserialize(uint8_t* src, serial_joy_t* dest) {
    memcpy(dest, src, sizeof(serial_joy_t));
    return 1;
}

int joy_t_serialize(serial_joy_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_joy_t));
    return 1;
}


int mbot_imu_t_deserialize(uint8_t* src, serial_mbot_imu_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_imu_t));
    return 1;
}

int mbot_imu_t_serialize(serial_mbot_imu_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_imu_t));
    return 1;
}


int mbot_motor_pwm_t_deserialize(uint8_t* src, serial_mbot_motor_pwm_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_motor_pwm_t));
    return 1;
}

int mbot_motor_pwm_t_serialize(serial_mbot_motor_pwm_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_motor_pwm_t));
    return 1;
}


int pose3D_t_deserialize(uint8_t* src, serial_pose3D_t* dest) {
    memcpy(dest, src, sizeof(serial_pose3D_t));
    return 1;
}

int pose3D_t_serialize(serial_pose3D_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_pose3D_t));
    return 1;
}


int mbot_motor_vel_t_deserialize(uint8_t* src, serial_mbot_motor_vel_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_motor_vel_t));
    return 1;
}

int mbot_motor_vel_t_serialize(serial_mbot_motor_vel_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_motor_vel_t));
    return 1;
}


int twist3D_t_deserialize(uint8_t* src, serial_twist3D_t* dest) {
    memcpy(dest, src, sizeof(serial_twist3D_t));
    return 1;
}

int twist3D_t_serialize(serial_twist3D_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_twist3D_t));
    return 1;
}


int mbot_message_received_t_deserialize(uint8_t* src, serial_mbot_message_received_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_message_received_t));
    return 1;
}

int mbot_message_received_t_serialize(serial_mbot_message_received_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_message_received_t));
    return 1;
}


int particle_t_deserialize(uint8_t* src, serial_particle_t* dest) {
    memcpy(dest, src, sizeof(serial_particle_t));
    return 1;
}

int particle_t_serialize(serial_particle_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_particle_t));
    return 1;
}


int slam_status_t_deserialize(uint8_t* src, serial_slam_status_t* dest) {
    memcpy(dest, src, sizeof(serial_slam_status_t));
    return 1;
}

int slam_status_t_serialize(serial_slam_status_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_slam_status_t));
    return 1;
}


int exploration_status_t_deserialize(uint8_t* src, serial_exploration_status_t* dest) {
    memcpy(dest, src, sizeof(serial_exploration_status_t));
    return 1;
}

int exploration_status_t_serialize(serial_exploration_status_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_exploration_status_t));
    return 1;
}


int planner_request_t_deserialize(uint8_t* src, serial_planner_request_t* dest) {
    memcpy(dest, src, sizeof(serial_planner_request_t));
    return 1;
}

int planner_request_t_serialize(serial_planner_request_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_planner_request_t));
    return 1;
}


int mbot_apriltag_t_deserialize(uint8_t* src, serial_mbot_apriltag_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_apriltag_t));
    return 1;
}

int mbot_apriltag_t_serialize(serial_mbot_apriltag_t* src, uint8_t* dest) {
    memcpy(dest, src, sizeof(serial_mbot_apriltag_t));
    return 1;
}


#endif
