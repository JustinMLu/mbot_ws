#ifndef MBOT_BRIDGE_LCM_UTILS_H
#define MBOT_BRIDGE_LCM_UTILS_H

#include <string>
#include <sstream>

#include <mbot_lcm_msgs/twist2D_t.hpp>
#include <mbot_lcm_msgs/pose2D_t.hpp>
#include <mbot_lcm_msgs/lidar_t.hpp>
#include <mbot_lcm_msgs/path2D_t.hpp>

#include "json_utils.h"

// Subs.
#define ODOMETRY_CHANNEL "MBOT_ODOMETRY"
#define SLAM_POSE_CHANNEL "SLAM_POSE"
#define SLAM_MAP_CHANNEL "SLAM_MAP"
#define LIDAR_CHANNEL "LIDAR"
// Pubs.
#define ODOMETRY_RESET_CHANNEL "MBOT_ODOMETRY_RESET"
#define ODOMETRY_RESET_TYPE "pose2D_t"
#define MBOT_VEL_CMD_CHANNEL "MBOT_VEL_CMD"
#define MBOT_VEL_CMD_TYPE "twist2D_t"
#define CONTROLLER_PATH_CHANNEL "CONTROLLER_PATH"
#define CONTROLLER_PATH_TYPE "path2D_t"


static inline std::string lcmTypeToString(const mbot_lcm_msgs::twist2D_t& data)
{
    std::ostringstream oss;
    oss << keyValToJSON("utime", data.utime) << ",";
    oss << keyValToJSON("vx", data.vx) << ",";
    oss << keyValToJSON("vy", data.vy) << ",";
    oss << keyValToJSON("wz", data.wz);
    return oss.str();
}


static inline std::string lcmTypeToString(const mbot_lcm_msgs::pose2D_t& data)
{
    std::ostringstream oss;
    oss << keyValToJSON("utime", data.utime) << ",";
    oss << keyValToJSON("x", data.x) << ",";
    oss << keyValToJSON("y", data.y) << ",";
    oss << keyValToJSON("theta", data.theta);
    return oss.str();
}


static inline std::string lcmTypeToString(const mbot_lcm_msgs::path2D_t& data)
{
    std::ostringstream oss;
    oss << keyValToJSON("utime", data.utime) << ",";
    oss << keyValToJSON("path_length", data.path_length) << ",";
    // Add the path vector one pose at a time.
    oss << "\"path\":[";
    for (size_t i = 0; i < data.path_length - 1; ++i)
    {
        oss << "{" << lcmTypeToString(data.path[i]) << "},";
    }
    oss << "{" << lcmTypeToString(data.path[data.path_length - 1]) << "}]";

    return oss.str();
}


static inline void stringToLCMType(const std::string& data, mbot_lcm_msgs::pose2D_t& out)
{
    // mbot_lcm_msgs::pose2D_t p;
    if (data.find("x") != std::string::npos)
    {
        auto x = strip(fetchVal(data, "x"));
        if (x.length() > 0) out.x = std::stof(x);
    }
    if (data.find("y") != std::string::npos)
    {
        auto y = strip(fetchVal(data, "y"));
        if (y.length() > 0) out.y = std::stof(y);
    }
    if (data.find("theta") != std::string::npos)
    {
        auto theta = strip(fetchVal(data, "theta"));
        if (theta.length() > 0) out.theta = std::stof(theta);
    }
    if (data.find("utime") != std::string::npos)
    {
        auto utime = fetchVal(data, "utime");
        if (utime.length() > 0) out.utime = std::stol(utime);
    }
}


static inline void stringToLCMType(const std::string& data, mbot_lcm_msgs::lidar_t& out)
{
    if (data.find("num_ranges") != std::string::npos)
    {
        auto num_ranges = strip(fetchVal(data, "num_ranges"));
        if (num_ranges.length() > 0) out.num_ranges = std::stoi(num_ranges);
    }
    if (data.find("ranges") != std::string::npos)
    {
        auto ranges_raw = strip(fetchList(data, "ranges"));
        if (ranges_raw.length() > 0)
        {
            auto ranges_str = split(ranges_raw, ',');
            std::vector<float> ranges;
            for (auto& ele : ranges_str) ranges.push_back(std::stof(ele));
            out.ranges = ranges;
        }
    }
    if (data.find("thetas") != std::string::npos)
    {
        auto thetas_raw = strip(fetchList(data, "thetas"));
        if (thetas_raw.length() > 0)
        {
            auto thetas_str = split(thetas_raw, ',');
            std::vector<float> thetas;
            for (auto& ele : thetas_str) thetas.push_back(std::stof(ele));
            out.thetas = thetas;
        }
    }
    if (data.find("utime") != std::string::npos)
    {
        auto utime = fetchVal(data, "utime");
        if (utime.length() > 0) out.utime = std::stol(utime);
    }
}


#endif // MBOT_BRIDGE_LCM_UTILS_H
