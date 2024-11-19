#include <slam/sensor_model.hpp>
#include <slam/moving_laser_scan.hpp>
#include <slam/occupancy_grid.hpp>
#include <mbot_lcm_msgs/particle_t.hpp>
#include <utils/grid_utils.hpp>
#include <utils/geometric/point.hpp>
SensorModel::SensorModel(void)
:   sigma_hit_(0.075),
	occupancy_threshold_(10),
	ray_stride_(7),
	max_ray_range_(1000),
    search_range(2),
    offset_quality_weight(3)
{
    initialize_bfs_offsets();
}

void SensorModel::initialize_bfs_offsets()
{
    /// TODO: Initialize the BFS offsets based on the search range 
    bfs_offsets_.clear();
    for (int i = -search_range; i <= search_range; i++)
    {
        for (int j = -search_range; j <= search_range; j++)
        {
            bfs_offsets_.push_back(Point<int>(i, j));
            // bfs_offset_.emplace_back(Point<int>(i, j));
        }
    }
    
}

double SensorModel::likelihood(const mbot_lcm_msgs::particle_t& sample, 
                               const mbot_lcm_msgs::lidar_t& scan, 
                               const OccupancyGrid& map)
{
    /// TODO: Compute the likelihood of the given particle using the provided laser scan and map. 
    MovingLaserScan movingScan(scan, sample.parent_pose, sample.pose);
    float likelihood;

    for (const auto &ray : movingScan) {
        Point<float> rayEndPointGlobal = getRayEndPointOnMap(ray, map);
        Point<float> rayEndPoint = global_position_to_grid_position(rayEndPointGlobal, map);

        // Nearest occupied cell from the ray end point
        Point<int> nearest = gridBFS(rayEndPoint, map);

        if (nearest.x >= 0 && nearest.y >= 0) {
            float zHitProb = NormalPdf(distance_between_points(rayEndPoint, nearest) / map.metersPerCell());
            float zRandProb = 1.0 / max_ray_range_;
            likelihood *= (0.5 * zHitProb) + (0.0075 * zRandProb); // Adjust constants
        }
    }

    return likelihood;
}

double SensorModel::scoreRay(const adjusted_ray_t& ray, const OccupancyGrid& map)
{
    /// TODO: Compute a score for a given ray based on its end point and the map. 
    // Consider the offset from the nearest occupied cell.  
    Point<float> rayEndPointGlobal = getRayEndPointOnMap(ray, map);
    Point<int> rayEndPoint = global_position_to_grid_cell(rayEndPointGlobal, map);
    Point<int> nearest = gridBFS(rayEndPoint, map);
    int dx = rayEndPoint.x - nearest.x;
    int dy = rayEndPoint.y - nearest.y;
    float distance = std::sqrt(dx*dx + dy*dy);

    return NormalPdf(distance) * offset_quality_weight;
}

double SensorModel::NormalPdf(const double& x)
{
    return (1.0/(sqrt(2.0 * M_PI)*sigma_hit_))*exp((-0.5*x*x)/(sigma_hit_*sigma_hit_));
}

// Do BFS on grid to find nearest occupied cell. I'm not even sure this is actual BFS, Copilot did it for me
Point<int> SensorModel::gridBFS(const Point<int> end_point, const OccupancyGrid& map)
{
    /// TODO: Use Breadth First Search to find the nearest occupied cell to the given end point. 
    Point<int> nearest = Point<int>(-1, -1);
    float minDist = std::numeric_limits<float>::infinity();

    // Find nearest occupied cell from end_point via bfs_offsets_
    for (const auto &offset : bfs_offsets_) {
        Point<int> current = end_point + offset;
        if (map.isCellInGrid(current.x, current.y) && map.logOdds(current.x, current.y) >= occupancy_threshold_) {
            float dist = distance_between_points(end_point, current);
            if (dist < minDist) {
                minDist = dist;
                nearest = current;
            }
        }
    }
    return nearest;
}

Point<float> SensorModel::getRayEndPointOnMap(const adjusted_ray_t& ray, const OccupancyGrid& map)
{
    /// TODO: Calculate the end point of a given ray on the map 
    Point<double> rayEndPointGlobal(ray.origin.x + ray.range * std::cos(ray.theta), 
                                ray.origin.y + ray.range * std::sin(ray.theta));

    return rayEndPointGlobal;
}
