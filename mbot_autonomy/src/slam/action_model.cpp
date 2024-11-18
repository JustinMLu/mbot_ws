#include <slam/action_model.hpp>
#include <mbot_lcm_msgs/particle_t.hpp>
#include <utils/geometric/angle_functions.hpp>
#include <cassert>
#include <cmath>
#include <iostream>
#include <algorithm>


ActionModel::ActionModel(void)
: k1_(0.1f) // Movement variability gain
, k2_(0.05f) // Turn variability gain
, min_dist_(0.0025)
, min_theta_(0.02)
, initialized_(false)
{
    //////////////// TODO: Handle any initialization for your ActionModel /////////////////////////

    // Initialize random number generator
    std::random_device rand;
    numberGenerator_ = std::mt19937(rand());
    
}

// Current odometry/time becomes previous odometry/time
void ActionModel::resetPrevious(const mbot_lcm_msgs::pose2D_t& odometry)
{
    previousPose_ = odometry;
}

////////////// TODO: Implement code here to compute a new distribution of the motion of the robot ////////////////
bool ActionModel::updateAction(const mbot_lcm_msgs::pose2D_t& odometry)
{   
    // Handle starting case
    if (!initialized_) {
        previousPose_ = odometry;
        initialized_ = true;
    }

    // Find total change in robot pose
    dx_ = odometry.x - previousPose_.x;
    dy_ = odometry.y - previousPose_.y;
    // dtheta_ = odometry.theta - previousPose_.theta;
    dtheta_ = angle_diff(odometry.theta, previousPose_.theta);

    // Calculate total linear distance
    ds_ = std::sqrt(dx_ * dx_ + dy_ * dy_);

    // Calculate alpha - the amount the robot needs to turn before driving
    alpha_ = angle_diff(std::atan2(dy_, dx_), previousPose_.theta); 
    
    // If initial rotation is > 90deg, subtract PI to get the "smaller angle" and move backwards instead
    if (std::abs(alpha_) > M_PI_2) {
        alpha_ = angle_diff(M_PI, alpha_);
        ds_ *= -1.0;
    }

    // Calculate beta - the amount the robot needs to turn after driving
    beta_ = angle_diff(dtheta_, alpha_);

    // If threshold for movement is exceeded, update the motion model
    if (ds_ >= min_dist_ || std::abs(dtheta_) > min_theta_) {
        e1_stdev_ = k1_ * std::abs(alpha_);
        e2_stdev_ = k2_ * std::abs(ds_);
        e3_stdev_ = k1_ * std::abs(beta_);
        
        resetPrevious(odometry);
        utime_ = odometry.utime;
        return true;
    }

    // Else return false
    resetPrevious(odometry);
    utime_ = odometry.utime;
    return false;
}

mbot_lcm_msgs::particle_t ActionModel::applyAction(const mbot_lcm_msgs::particle_t& sample)
{
    ////////////// TODO: Implement your code for sampling new poses from the distribution computed in updateAction //////////////////////
    // Make sure you create a new valid particle_t. Don't forget to set the new time and new parent_pose.
    mbot_lcm_msgs::particle_t newSample = sample;
    
    // Generate our sampled noise for each action
    e1_ = std::normal_distribution<float>(0.0, e1_stdev_)(numberGenerator_);
    e2_ = std::normal_distribution<float>(0.0, e2_stdev_)(numberGenerator_);
    e3_ = std::normal_distribution<float>(0.0, e3_stdev_)(numberGenerator_);

    // Get our sampled RTR actions
    float rot1 = alpha_ + e1_;
    float trans = ds_ + e2_;
    float rot2 = beta_ + e3_;

    // Update newSample's pose
    newSample.pose.x += trans * std::cos(sample.pose.theta + rot1);
    newSample.pose.y += trans * std::sin(sample.pose.theta + rot1);
    newSample.pose.theta = wrap_to_pi(sample.pose.theta + rot1 + rot2); // Keep in [-pi, pi]
    
    newSample.parent_pose = sample.pose;
    newSample.pose.utime = utime_;
    return newSample;
}
