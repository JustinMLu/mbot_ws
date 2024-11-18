/**
 * This file is the main executable for the MBot Classic firmware.
 */
#include "mbot_classic.h"
#pragma pack(1)

// Global Variables and Forward Declarations
static bool running = false;
mbot_params_t params;
uint64_t timestamp_offset = 0;
uint64_t global_utime = 0;
uint64_t global_pico_time = 0;
bool global_comms_status = COMMS_ERROR;
int drive_mode = 0;
mbot_bhy_config_t mbot_imu_config;
mbot_bhy_data_t mbot_imu_data;

// Forward declaration for internal helper function
int mbot_init_pico(void);
int mbot_init_hardware(void);
void mbot_read_encoders(serial_mbot_encoders_t* encoders);
void mbot_read_imu(serial_mbot_imu_t *imu);
void mbot_calculate_motor_vel(serial_mbot_encoders_t encoders, serial_mbot_motor_vel_t *motor_vel);
static float _calibrated_pwm_from_vel_cmd(float vel_cmd, int motor_idx);
void print_mbot_params(const mbot_params_t* params);

/*********************************************************************
 * Main Control Functions
 * ----------------------------------------------------
 * These functions are critical for MBot's operation and include the
 * main loop and initial setup. Students may be asked to review or
 * modify parts of this section depending on their assignment.
 *********************************************************************/

bool mbot_loop(repeating_timer_t *rt)
{
    // Update mbot_vel with current global time
    global_utime = to_us_since_boot(get_absolute_time()) + timestamp_offset;
    mbot_vel.utime = global_utime;

    // Read encoder and IMU
    mbot_read_encoders(&mbot_encoders);
    mbot_read_imu(&mbot_imu);

    // Calculate motor velocities from encoder values
    mbot_calculate_motor_vel(mbot_encoders, &mbot_motor_vel);

    // // Calculate EMPIRICAL differential drive velocities (linear and angular) from motor velocities
    // mbot_calculate_diff_body_vel(   mbot_motor_vel.velocity[MOT_L],
    //                                 mbot_motor_vel.velocity[MOT_R],
    //                                 &mbot_vel
    //                             );

    mbot_calculate_diff_body_vel_imu(   mbot_motor_vel.velocity[MOT_L],
                                    mbot_motor_vel.velocity[MOT_R],
                                    mbot_imu,
                                    &mbot_vel
                                );

    // float theta_prev = 0.0f;
    // float odo_theta_prev = 0.0f;
    // float gyro_theta_prev = 0.0f;
    
    // mbot_calculate_diff_body_vel_imu_2(   mbot_motor_vel.velocity[MOT_L],
    //                                 mbot_motor_vel.velocity[MOT_R],
    //                                 mbot_imu,
    //                                 &mbot_vel,
    //                                 &theta_prev,
    //                                 &odo_theta_prev,
    //                                 &gyro_theta_prev
    //                             );


    // Update mbot_odometry
    mbot_odometry.utime = global_utime;
    mbot_calculate_odometry(mbot_vel, MAIN_LOOP_PERIOD, &mbot_odometry);

    // only run if we've got 2 way communication...
    if (global_comms_status == COMMS_OK) {
        if (drive_mode == MODE_MOTOR_VEL_OL) {
            mbot_motor_pwm.utime = global_utime;
            mbot_motor_pwm_cmd.pwm[MOT_R] = _calibrated_pwm_from_vel_cmd(mbot_motor_vel_cmd.velocity[MOT_R], MOT_R);
            mbot_motor_pwm_cmd.pwm[MOT_L] = _calibrated_pwm_from_vel_cmd(mbot_motor_vel_cmd.velocity[MOT_L], MOT_L);
        }

        else if (drive_mode == MODE_MBOT_VEL) {
           

            //TODO: open loop for now - implement closed loop controller
            mbot_motor_vel_cmd.velocity[MOT_L] = (mbot_vel_cmd.vx - DIFF_BASE_RADIUS * mbot_vel_cmd.wz) / DIFF_WHEEL_RADIUS;
            mbot_motor_vel_cmd.velocity[MOT_R] = (-mbot_vel_cmd.vx - DIFF_BASE_RADIUS * mbot_vel_cmd.wz) / DIFF_WHEEL_RADIUS;

            float vel_left_comp = params.motor_polarity[MOT_L] * mbot_motor_vel_cmd.velocity[MOT_L];
            float vel_right_comp = params.motor_polarity[MOT_R] * mbot_motor_vel_cmd.velocity[MOT_R];

            mbot_motor_pwm.utime = global_utime;

            // Calculate PID vel --> output PWM is passed by reference here to be changed
            mbot_motor_vel_ctlr(mbot_motor_vel_cmd, mbot_motor_vel, &mbot_motor_pwm_cmd);

            // Don't ask
            mbot_motor_pwm_cmd.pwm[MOT_R] *= params.motor_polarity[MOT_R];
            mbot_motor_pwm_cmd.pwm[MOT_L] *= params.motor_polarity[MOT_L];

            mbot_motor_pwm_cmd.pwm[MOT_R] += _calibrated_pwm_from_vel_cmd(vel_right_comp, MOT_R);
            mbot_motor_pwm_cmd.pwm[MOT_L] += _calibrated_pwm_from_vel_cmd(vel_left_comp, MOT_L);
        }

        else {
            drive_mode = MODE_MOTOR_PWM;
            mbot_motor_pwm.utime = global_utime;
        }

        // Set motors
        mbot_motor_set_duty(MOT_R, mbot_motor_pwm_cmd.pwm[MOT_R]);
        mbot_motor_pwm.pwm[MOT_R] = mbot_motor_pwm_cmd.pwm[MOT_R];
        mbot_motor_set_duty(MOT_L, mbot_motor_pwm_cmd.pwm[MOT_L]);
        mbot_motor_pwm.pwm[MOT_L] = mbot_motor_pwm_cmd.pwm[MOT_L];

        // write the encoders to serial
        comms_write_topic(MBOT_ENCODERS, &mbot_encoders);
        // send odom on wire
        comms_write_topic(MBOT_ODOMETRY, &mbot_odometry);
        // write the IMU to serial
        comms_write_topic(MBOT_IMU, &mbot_imu);
        // write the Body velocity to serial
        comms_write_topic(MBOT_VEL, &mbot_vel);
        // write the Motor velocity to serial
        comms_write_topic(MBOT_MOTOR_VEL, &mbot_motor_vel);
        // write the PWMs to serial
        comms_write_topic(MBOT_MOTOR_PWM, &mbot_motor_pwm);
    }
    // comparing current pico time against the last successful communication timestamp(global_pico_time)
    uint64_t timeout = to_us_since_boot(get_absolute_time()) - global_pico_time;
    if(timeout > MBOT_TIMEOUT_US){
        mbot_motor_set_duty(MOT_L, 0.0);
        mbot_motor_set_duty(MOT_R, 0.0);
        global_comms_status = COMMS_ERROR;
    }

    return true;
}

int main()
{
    printf("********************************\n");
    printf("* MBot Classic Firmware v%s *\n", VERSION);
    printf("********************************\n");

    mbot_init_pico();
    mbot_init_hardware();
    mbot_init_comms();
    mbot_read_fram(0, sizeof(params), &params);

    // Set PID tuning constants
    mbot_ctlr_cfg_t pid_cfgs = {
        .left = (mbot_pid_cfg_t) {
            0.26, 
            0.0, 
            0.025 * params.motor_polarity[MOT_L], 
            4.0 * MAIN_LOOP_PERIOD
        }, 

        .right = (mbot_pid_cfg_t) {
            0.26, 
            0.0, 
            0.025 * params.motor_polarity[MOT_R], 
            4.0 * MAIN_LOOP_PERIOD
        },

        .wz = (mbot_pid_cfg_t) {
            0.75, 
            0.0, 
            0.0, 
            4.0 * MAIN_LOOP_PERIOD
        }
    };

    // Initialize PID configuration struct
    mbot_init_ctlr(pid_cfgs);

    //Check also that define drive type is same as FRAM drive type
    int validate_status = validate_mbot_classic_FRAM_data(&params, MOT_L, MOT_R, MOT_UNUSED);
    if (validate_status < 0)
    {
        printf("Failed to validate FRAM Data! Error code: %d\n", validate_status);
        return -1;
    }

    sleep_ms(3000);
    print_mbot_params(&params);
    printf("Starting MBot Loop...\n");
    repeating_timer_t loop_timer;
    add_repeating_timer_ms(MAIN_LOOP_PERIOD * 1000, mbot_loop, NULL, &loop_timer); // 1000x to convert to ms
    printf("Done Booting Up!\n");
    running = true;

    while(running){
        // Print State
        mbot_print_state(mbot_imu, mbot_encoders, mbot_odometry, mbot_motor_vel);

        sleep_ms(200);
    }
}


/******************************************************
 * Helper Functions
 * ----------------------------------------------------
 * These functions are used internally by the main control functions.
 * They are not intended for modification by students. These functions
 * provide lower-level control and utility support.
 ******************************************************/
int mbot_init_pico(void){
    bi_decl(bi_program_description("Firmware for the MBot Robot Control Board"));

    // set master clock to 250MHz (if unstable set SYS_CLOCK to 125Mhz)
    if(!set_sys_clock_khz(125000, true)){
        printf("ERROR mbot_init_pico: cannot set system clock\n");
        return MBOT_ERROR;
    };

    stdio_init_all(); // enable USB serial terminal
    sleep_ms(500);
    printf("\nMBot Booting Up!\n");
    return MBOT_OK;
}

int mbot_init_hardware(void){
    sleep_ms(1000);
    // Initialize Motors
    printf("initializinging motors...\n");
    mbot_motor_init(MOT_L);
    mbot_motor_init(MOT_R);
    printf("initializinging encoders...\n");
    mbot_encoder_init();

    // Initialize LED
    printf("Starting heartbeat LED...\n");
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    mbot_imu_config = mbot_imu_default_config();
    mbot_imu_config.sample_rate = 200;
    // Initialize the IMU using the Digital Motion Processor
    printf("Initializing IMU...\n");
    mbot_imu_init(&mbot_imu_data, mbot_imu_config);
    mbot_init_fram();
    return MBOT_OK;
}

void mbot_read_encoders(serial_mbot_encoders_t* encoders){
    int64_t delta_time = global_utime - encoders->utime;
    encoders->utime = global_utime;
    encoders->delta_time = delta_time;

    encoders->ticks[MOT_R] = mbot_encoder_read_count(MOT_R);
    encoders->delta_ticks[MOT_R] = mbot_encoder_read_delta(MOT_R);
    encoders->ticks[MOT_L] = mbot_encoder_read_count(MOT_L);
    encoders->delta_ticks[MOT_L] = mbot_encoder_read_delta(MOT_L);
}

void mbot_read_imu(serial_mbot_imu_t *imu){
    imu->utime = global_utime;
    imu->gyro[0] = mbot_imu_data.gyro[0];
    imu->gyro[1] = mbot_imu_data.gyro[1];
    imu->gyro[2] = mbot_imu_data.gyro[2]; // USE THIS FOR GYRODOMETRY
    imu->accel[0] = mbot_imu_data.accel[0];
    imu->accel[1] = mbot_imu_data.accel[1];
    imu->accel[2] = mbot_imu_data.accel[2];
    imu->mag[0] = mbot_imu_data.mag[0];
    imu->mag[1] = mbot_imu_data.mag[1];
    imu->mag[2] = mbot_imu_data.mag[2];
    imu->angles_rpy[0] = mbot_imu_data.rpy[0];
    imu->angles_rpy[1] = mbot_imu_data.rpy[1];
    imu->angles_rpy[2] = mbot_imu_data.rpy[2];
    imu->angles_quat[0] = mbot_imu_data.quat[0];
    imu->angles_quat[1] = mbot_imu_data.quat[1];
    imu->angles_quat[2] = mbot_imu_data.quat[2];
    imu->angles_quat[3] = mbot_imu_data.quat[3];
}

// Converting the raw encoder ticks into actual rotational velocities in radians per second
void mbot_calculate_motor_vel(serial_mbot_encoders_t encoders, serial_mbot_motor_vel_t *motor_vel){
    float conversion = (1.0 / GEAR_RATIO) * (1.0 / ENCODER_RES) * 1E6f * 2.0 * M_PI;
    motor_vel->velocity[MOT_L] = params.encoder_polarity[MOT_L] * (conversion / encoders.delta_time) * encoders.delta_ticks[MOT_L];
    motor_vel->velocity[MOT_R] = params.encoder_polarity[MOT_R] * (conversion / encoders.delta_time) * encoders.delta_ticks[MOT_R];
}

int mbot_calculate_diff_body_vel(float wheel_left_vel, float wheel_right_vel, serial_twist2D_t *mbot_vel){
    mbot_vel->vx =  DIFF_WHEEL_RADIUS * (wheel_left_vel - wheel_right_vel) / 2.0f;
    mbot_vel->vy = 0;
    mbot_vel->wz =  DIFF_WHEEL_RADIUS * (-wheel_left_vel - wheel_right_vel) / (2.0f * DIFF_BASE_RADIUS); // wz from odometry (rad)
    return 0; // Return 0 to indicate success
}

int mbot_calculate_diff_body_vel_imu(float wheel_left_vel, float wheel_right_vel, serial_mbot_imu_t imu, serial_twist2D_t *mbot_vel){
    mbot_vel->vx =  DIFF_WHEEL_RADIUS * (wheel_left_vel - wheel_right_vel) / 2.0f;

    float wz_odometry = DIFF_WHEEL_RADIUS * (-wheel_left_vel - wheel_right_vel) / (2.0f * DIFF_BASE_RADIUS);
    float wz_gyro = imu.gyro[2];
    float delta_wz = fabs(wz_gyro - wz_odometry);
    float threshold = 0.1; // Radians

    // // Print the computed angular velocities and their difference for debugging
    // printf("wz_odometry: %.6f rad/s | wz_gyro: %.6f rad/s | delta_wz: %.6f rad/s | gyro_theta: %.6f rad\n", wz_odometry, wz_gyro, delta_wz, imu.angles_rpy[2]);
    
    // If threshold passed, use gyro, else use odometry
    if (delta_wz > threshold) {
        // printf("THRESHOLD PASSED\n");
        mbot_vel->wz = wz_gyro;
    }
    else {
        mbot_vel->wz = wz_odometry;
    }

    return 0; // Return 0 to indicate success
}


int mbot_calculate_diff_body_vel_imu_2(float wheel_left_vel, float wheel_right_vel, serial_mbot_imu_t imu, serial_twist2D_t *mbot_vel, float *theta_prev, float *odo_theta_prev, float *gyro_theta_prev) {
    mbot_vel->vx = DIFF_WHEEL_RADIUS * (wheel_left_vel - wheel_right_vel) / 2.0f;
    mbot_vel->vy = 0;
    float gyro_theta = imu.angles_rpy[2];
    float delta_odo_theta = DIFF_WHEEL_RADIUS * (-wheel_left_vel - wheel_right_vel) / (2.0f * DIFF_BASE_RADIUS) * MAIN_LOOP_PERIOD;
    float delta_gyro_theta = gyro_theta - *gyro_theta_prev;

    printf("gyro_theta: %.6f rad/s, delta_odo_theta: %.6f rad/s, delta_gyro_theta: %.6f rad/s\n", gyro_theta, delta_odo_theta, delta_gyro_theta);

    if (gyro_theta < 0 && *gyro_theta_prev > 0) {
        if (gyro_theta < -1.5) {
            // gyro_theta ~ -3.14 and gyro_theta_prev ~ 3.14
            delta_gyro_theta = (M_PI - *gyro_theta_prev) + (gyro_theta - (-M_PI));
        }
        else {
            gyro_theta - *gyro_theta_prev;
        }
    }

    if (gyro_theta > 0 && *gyro_theta_prev < 0) {
        if (gyro_theta > 1.5) {
            // gyro_theta ~ 3.14 and gyro_theta_prev ~ -3.14
            delta_gyro_theta = (-M_PI - *gyro_theta_prev) + (gyro_theta - M_PI);
        }
        else {
            delta_gyro_theta = gyro_theta - *gyro_theta_prev;
        }
    }

    float imu_wz = delta_gyro_theta / MAIN_LOOP_PERIOD;
    // *odo_theta_prev = odo_theta;
    *gyro_theta_prev = gyro_theta;
    float theta = 0.0f;

    if (fabs(delta_gyro_theta - delta_odo_theta) > 0.1) {
        theta = *theta_prev + (delta_gyro_theta);
    }
    else {
        theta = *theta_prev + (delta_odo_theta);
    }

    mbot_vel->wz = (theta - *theta_prev) / MAIN_LOOP_PERIOD;
    mbot_vel->wz = imu_wz;
    *theta_prev = theta;

    return 0; // Return 0 to indicate success

}

// Use slope + intercept from calibration to generate a PWM command.
static float _calibrated_pwm_from_vel_cmd(float vel_cmd, int motor_idx){
    if (vel_cmd > 0.0)
    {
        return (vel_cmd * params.slope_pos[motor_idx]) + params.itrcpt_pos[motor_idx];
    }
    else if (vel_cmd < 0.0)
    {
        return (vel_cmd * params.slope_neg[motor_idx]) + params.itrcpt_neg[motor_idx];
    }
    return 0.0;
}

void print_mbot_params(const mbot_params_t* params) {
    printf("Motor Polarity: %d %d %d\n", params->motor_polarity[0], params->motor_polarity[1], params->motor_polarity[2]);
    printf("Encoder Polarity: %d %d %d\n", params->encoder_polarity[0], params->encoder_polarity[1], params->encoder_polarity[2]);
    printf("Positive Slope: %f %f %f\n", params->slope_pos[0], params->slope_pos[1], params->slope_pos[2]);
    printf("Positive Intercept: %f %f %f\n", params->itrcpt_pos[0], params->itrcpt_pos[1], params->itrcpt_pos[2]);
    printf("Negative Slope: %f %f %f\n", params->slope_neg[0], params->slope_neg[1], params->slope_neg[2]);
    printf("Negative Intercept: %f %f %f\n", params->itrcpt_neg[0], params->itrcpt_neg[1], params->itrcpt_neg[2]);
}
