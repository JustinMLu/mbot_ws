#include <utils/lcm_config.h>
#include <mbot/mbot_channels.h>
#include <mbot_lcm_msgs/path2D_t.hpp>
#include <mbot_lcm_msgs/pose2D_t.hpp>
#include <lcm/lcm-cpp.hpp>
#include <iostream>
#include <unistd.h>
#include <cmath>

using namespace mbot_lcm_msgs;

int main(int argc, char** argv)
{
    std::cout << "Commanding robot to follow custom zigzag path.\n";

    path2D_t path;
    pose2D_t nextPose;

    // Starting position
    nextPose.x = 0.0f;
    nextPose.y = 0.0f;
    nextPose.theta = 0.0f; // facing right
    path.path.push_back(nextPose);

    // Define distances
    float short_dist = 0.61f;  // 61 cm
    float long_dist = 1.22f;   // 122 cm

    // Follow the sequence
    // 1. Go straight 61
    nextPose.x += short_dist;
    path.path.push_back(nextPose);

    // 2. Turn right (90 degrees) and go straight 61
    nextPose.theta = -M_PI / 2;
    path.path.push_back(nextPose);
    nextPose.y -= short_dist;
    path.path.push_back(nextPose);

    // 3. Turn left (0 degrees) and go straight 61
    nextPose.theta = 0.0f;
    path.path.push_back(nextPose);
    nextPose.x += short_dist;
    path.path.push_back(nextPose);

    // 4. Turn left (90 degrees) and go straight 122
    nextPose.theta = M_PI / 2;
    path.path.push_back(nextPose);
    nextPose.y += long_dist;
    path.path.push_back(nextPose);

    // 5. Turn right (0 degrees) and go straight 61
    nextPose.theta = 0.0f;
    path.path.push_back(nextPose);
    nextPose.x += short_dist;
    path.path.push_back(nextPose);

    // 6. Turn right (-90 degrees) and go straight 122
    nextPose.theta = -M_PI / 2;
    path.path.push_back(nextPose);
    nextPose.y -= long_dist;
    path.path.push_back(nextPose);

    // 7. Turn left (0 degrees) and go straight 61
    nextPose.theta = 0.0f;
    path.path.push_back(nextPose);
    nextPose.x += short_dist;
    path.path.push_back(nextPose);

    // 8. Turn left (90 degrees) and go straight 61
    nextPose.theta = M_PI / 2;
    path.path.push_back(nextPose);
    nextPose.y += short_dist;
    path.path.push_back(nextPose);

    // 9. Turn right (0 degrees) and go straight 61
    nextPose.theta = 0.0f;
    path.path.push_back(nextPose);
    nextPose.x += short_dist;
    path.path.push_back(nextPose);

    // Set path length
    path.path_length = path.path.size();

    lcm::LCM lcmInstance(MULTICAST_URL);
    std::cout << "publish to: " << CONTROLLER_PATH_CHANNEL << std::endl;
    lcmInstance.publish(CONTROLLER_PATH_CHANNEL, &path);
    sleep(1);

    return 0;
}