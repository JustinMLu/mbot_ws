#include <iostream>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <getopt.h>
#include <signal.h>
#include <sys/time.h>

#include <lcm/lcm-cpp.hpp>
#include <mbot_lcm_msgs/lidar_t.hpp>

#include <rplidar.h>

#ifndef _countof
#define _countof(_Array) (int)(sizeof(_Array) / sizeof(_Array[0]))
#endif

#define PI 3.1415926535f
#define CONNECT_PERIOD 2000000
#define MULTICAST_URL "udpm://239.255.76.67:7667?ttl=2"

using namespace rp::standalone::rplidar;

int64_t utime_now() // blacklist-ignore
{
    struct timeval tv;
    gettimeofday (&tv, NULL); // blacklist-ignore
    return (int64_t) tv.tv_sec * 1000000 + tv.tv_usec;
}

bool checkRPLIDARHealth(RPlidarDriver * drv)
{
    u_result     op_result;
    rplidar_response_device_health_t healthinfo;

    op_result = drv->getHealth(healthinfo);
    if (IS_OK(op_result)) { // the macro IS_OK is the preperred way to judge whether the operation is succeed.
        fprintf(stderr, "RPLidar health status : %d\n", healthinfo.status);
        if (healthinfo.status == RPLIDAR_STATUS_ERROR) {
            fprintf(stderr, "Error, rplidar internal error detected. Please reboot the device to retry.\n");
            // enable the following code if you want rplidar to be reboot by software
            // drv->reset();
            return false;
        } else {
            return true;
        }

    } else {
        fprintf(stderr, "Error, cannot retrieve the lidar health code: %x\n", op_result);
        return false;
    }
}

// Catch SIGINT
#include <signal.h>
bool ctrl_c_pressed;
void ctrlc(int)
{
    ctrl_c_pressed = true;
}

bool connect(RPlidarDriver* drv, const char* opt_com_path, _u32 opt_com_baudrate) {
    // If this driver thinks it is already connected, reset it.
    if (drv->isConnected()) {
        RPlidarDriver::DisposeDriver(drv);
        drv = RPlidarDriver::CreateDriver();
    }

    if (IS_FAIL(drv->connect(opt_com_path, opt_com_baudrate))) {
        fprintf(stderr, "ERROR: cannot bind to the specified serial port %s.\n" , opt_com_path);
        return false;
    }
    return true;
}


bool validateStartupHealth(RPlidarDriver* drv) {
    rplidar_response_device_info_t devinfo;

    // retrieving the device info
    u_result op_result = drv->getDeviceInfo(devinfo);

    if (IS_FAIL(op_result)) {
        fprintf(stderr, "ERROR: cannot get device info.\n");
        return false;
    }

    // print out the device serial number, firmware and hardware version number..
    fprintf(stderr, "RPLIDAR S/N: ");
    for (int pos = 0; pos < 16 ;++pos) {
        fprintf(stderr, "%02X", devinfo.serialnum[pos]);
    }

    fprintf(stderr, "\n"
            "Firmware Ver: %d.%02d\n"
            "Hardware Rev: %d\n"
            , devinfo.firmware_version>>8
            , devinfo.firmware_version & 0xFF
            , (int)devinfo.hardware_version);

    // check health...
    return checkRPLIDARHealth(drv);
}

int main(int argc, char *argv[]) {

    // Default values
    const char * opt_com_path = "/dev/rplidar";
    _u32         opt_com_baudrate = 115200;
    uint16_t pwm = 700;
    bool lidar_connected = false;

    lcm::LCM lcmConnection(MULTICAST_URL);

    if(!lcmConnection.good()) { return 1; }

    uint8_t stride = 0;

    // command line arguments
    int c;
    static struct option long_options[] = {
        {"path", optional_argument, NULL, 'p'},
        {"baudrate", optional_argument, NULL, 'b'},
        {"pwm", optional_argument, NULL, 'w'},
        {"help", no_argument, NULL, 'h'},
        {"stride", required_argument, NULL, 's'},
        {NULL, 0, NULL, 0}};

    while ((c = getopt_long(argc, argv, "p:b:w:s:h", long_options, NULL)) != -1) {
        switch (c) {
        case 'p':
            if(optarg)
                opt_com_path = optarg;
            break;
        case 'b':
            if(optarg)
                opt_com_baudrate = strtoul(optarg, NULL, 10);
            break;
        case 'w':
            if(optarg)
                pwm = atoi(optarg);
            break;
        case 's':
            stride = atoi(optarg);
            break;
        case 'h':
            std::cout << "Usage: \n"
                      << "\t--dev or -d: Path of the device (default: " << opt_com_path << ") \n"
                      << "\t--baudrate or -b: Baudrate of the device (default: " << opt_com_baudrate << ") \n"
                      << "\t--pwm or -w: Pulse Width Modulation value (default: " << pwm << ") \n"
                      << "\t--stride or -s: Stride value for lidar rays, 0 = include all (default: " << stride << ")\n"
                      << "\t--help or -h: Display this help message \n";
            return 0;
        default:
            return 1;
        }
    }

    std::cout << "LIDAR driver for RPLIDAR A1 & A2" << std::endl;
    // create the driver instance
    RPlidarDriver * drv = RPlidarDriver::CreateDriver();

    if (!drv) {
        fprintf(stderr, "insufficent memory, exit\n");
        exit(-2);
    }

    int64_t now = utime_now();
    int64_t prev_time;

    signal(SIGINT, ctrlc);
    signal(SIGTERM, ctrlc);

    // make connection...
    while (!connect(drv, opt_com_path, opt_com_baudrate))
    {
        if (ctrl_c_pressed) break;
        usleep(CONNECT_PERIOD);
    }

    if (!validateStartupHealth(drv)) goto on_finished;
    else lidar_connected = true;

    drv->startMotor();
    // start scan...
    drv->setMotorPWM(pwm);
    drv->startScan(0, 1);

    u_result     op_result;

    while (lidar_connected) {
        rplidar_response_measurement_node_hq_t nodes[8192];
        size_t   count = _countof(nodes);

        op_result = drv->grabScanDataHq(nodes, count);
        prev_time = now;
        now = utime_now();  // get current timestamp in milliseconds
        int64_t delta = (now - prev_time)/count;

        if (IS_OK(op_result)) {

            drv->ascendScanData(nodes, count);

            int stride_ray_count = count / (stride + 1);
            mbot_lcm_msgs::lidar_t newLidar;

            newLidar.utime = now;
            newLidar.num_ranges = stride_ray_count;
            newLidar.ranges.resize(stride_ray_count);
            newLidar.thetas.resize(stride_ray_count);
            newLidar.intensities.resize(stride_ray_count);
            newLidar.times.resize(stride_ray_count);

            for (int pos = 0; pos < stride_ray_count ; ++pos) {
            	int scan_idx = (int)count - (pos * (stride+1)) - 1;
                newLidar.ranges[pos] = nodes[scan_idx].dist_mm_q2/4000.0f;
            	newLidar.thetas[pos] = 2*PI - nodes[scan_idx].angle_z_q14 * (PI / 32768.0); // use updated angle formula
            	newLidar.intensities[pos] = nodes[scan_idx].quality >> RPLIDAR_RESP_MEASUREMENT_QUALITY_SHIFT;
            	newLidar.times[pos] = prev_time + pos*delta;
            }

            lcmConnection.publish("LIDAR", &newLidar);
        }
        else {
            // Attempt to reconnect to the driver.
            if (connect(drv, opt_com_path, opt_com_baudrate)) {
                if (!validateStartupHealth(drv)) goto on_finished;
                drv->startMotor();
                // start scan...
                drv->setMotorPWM(pwm);
                drv->startScan(0,1);
            }
        }

        if (ctrl_c_pressed){
            break;
        }
    }

    drv->stop();
    drv->stopMotor();
    // done!
on_finished:
    std::cout << "RPLidar Driver shutting down." << std::endl;
    RPlidarDriver::DisposeDriver(drv);
    return 0;
}
