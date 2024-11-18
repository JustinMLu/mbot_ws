#include <mbot_bridge/robot.h>


int main(int argc, char* argv[])
{
    mbot_bridge::MBot mbot;
    mbot.drive(0, 0, 0);

    auto odom = mbot.readOdometry();
    std::cout << "Odometry: ";
    for (auto& ele : odom) std::cout << ele << " ";
    std::cout << std::endl;

    auto pose = mbot.readSlamPose();
    std::cout << "SLAM pose: ";
    for (auto& ele : pose) std::cout << ele << " ";
    std::cout << std::endl;

    std::vector<float> ranges, thetas;
    mbot.readLidarScan(ranges, thetas);
    std::cout << "Lidar scan length: " << ranges.size() << " " << thetas.size() << std::endl;

    mbot.resetOdometry();

    std::vector<std::array<float, 3>> path;
    path.push_back({1,2,0.3});
    path.push_back({4,5,0.6});
    mbot.drivePath(path);
}
