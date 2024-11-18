#ifndef SLAM_SENSOR_MODEL_HPP
#define SLAM_SENSOR_MODEL_HPP

class  lidar_t;
class  OccupancyGrid;
struct particle_t;


#include <utils/geometric/point.hpp>
#include <mbot_lcm_msgs/particle_t.hpp>
#include <slam/moving_laser_scan.hpp>
#include <slam/occupancy_grid.hpp>
#include <utils/grid_utils.hpp>
#include <list>
#include <numeric>
#include <random>


/**
* SensorModel implement a sensor model for computing the likelihood that a laser scan was measured from a
* provided pose, give a map of the environment.
* 
* A sensor model is compute the unnormalized likelihood of a particle in the proposal distribution.
*
* To use the SensorModel, a single method exists:
*
*   - double likelihood(const particle_t& particle, const lidar_t& scan, const OccupancyGrid& map)
*
* likelihood() computes the likelihood of the provided particle, given the most recent laser scan and map estimate.
*/
class SensorModel
{

    // using pose_offset_queue_t = std::queue<pose_offset_t>;
    using pose_offset_vector_t = std::vector<Point<int>>;

public:

    /**
    * Constructor for SensorModel.
    */
    SensorModel(void);

    /**
    * likelihood computes the likelihood of the provided particle, given the most recent laser scan and map estimate.
    * 
    * \param    particle            Particle for which the log-likelihood will be calculated
    * \param    scan                Laser scan to use for estimating log-likelihood
    * \param    map                 Current map of the environment
    * \return   Likelihood of the particle given the current map and laser scan.
    */
    double likelihood(const mbot_lcm_msgs::particle_t& particle,
                      const mbot_lcm_msgs::lidar_t& scan,
                      const OccupancyGrid& map);

    float max_scan_score;  // TODO: make getter

private:
    
    ///////// TODO: Add any private members for your SensorModel ///////////////////
    const float sigma_hit_;
	const int occupancy_threshold_;
    const int ray_stride_;
    const int max_ray_range_;

    pose_offset_vector_t bfs_offsets_;
    const int search_range;
    float max_offset_norm;
    float offset_quality_weight;

    double NormalPdf(const double& x);
    double scoreRay(const adjusted_ray_t& ray, const OccupancyGrid& map);
    Point<float> getRayEndPointOnMap(const adjusted_ray_t& ray, const OccupancyGrid& map);
    Point<int> gridBFS(const Point<int> endPoint, const OccupancyGrid& map);
    void initialize_bfs_offsets();
};

#endif // SLAM_SENSOR_MODEL_HPP
