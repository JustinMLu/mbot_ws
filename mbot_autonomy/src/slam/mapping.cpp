#include <slam/mapping.hpp>
#include <utils/grid_utils.hpp>
#include <numeric>
#include <chrono>
using namespace std::chrono;

Mapping::Mapping(float maxLaserDistance, int8_t hitOdds, int8_t missOdds)
    : kMaxLaserDistance_(maxLaserDistance), kHitOdds_(hitOdds), kMissOdds_(missOdds), initialized_(false)
{
}

void Mapping::updateMap(const mbot_lcm_msgs::lidar_t &scan,
                        const mbot_lcm_msgs::pose2D_t &pose,
                        OccupancyGrid &map)
{
    if (!initialized_)
        previousPose_ = pose;
    
    MovingLaserScan movingScan(scan, previousPose_, pose);

    /// TODO: Update the map's log odds using the movingScan
    // Hint: Consider both the cells the laser hit and the cells it passed through.

    for (auto& ray : movingScan) {
        scoreEndpoint(ray, map);
    }
    
    for (auto& ray : movingScan) {
        scoreRay(ray, map);
    }
    
    previousPose_ = pose;
    initialized_ = true;
}

void Mapping::scoreEndpoint(const adjusted_ray_t &ray, OccupancyGrid &map)
{
    /// TODO: Implement how to score the cell that the laser endpoint hits
    if (ray.range <= kMaxLaserDistance_) {
        
        // Find grid cell of ray origin (GASKELL'S CODE DIFFERS, ASK HIM ABOUT THIS)
        Point<int> start = global_position_to_grid_cell(ray.origin, map);

        // Find grid cell of endpoint
        Point<int> endpoint;
        endpoint.x = static_cast<int>(start.x + (ray.range * std::cos(ray.theta) * map.cellsPerMeter()));
        endpoint.y = static_cast<int>(start.y + (ray.range * std::sin(ray.theta) * map.cellsPerMeter()));

        // Increase cell odds of endpoint cell if it's in the grid
        if(map.isCellInGrid(endpoint.x, endpoint.y)) {
            increaseCellOdds(endpoint.x, endpoint.y, map);
        }
    }
    
}

void Mapping::scoreRay(const adjusted_ray_t &ray, OccupancyGrid &map)
{
    /// TODO: Implement how to score the cells that the laser ray passes through
    // Bresenham algorithm returns list of 'passed through points
    std::vector<Point<int>> cells = bresenham(ray, map);
    
    for (auto& cell : cells) {
        if (map.isCellInGrid(cell.x, cell.y)) {
            decreaseCellOdds(cell.x, cell.y, map);
        }   
    }
}

/*
Takes the ray and map, and returns a vector of map cells to check
*/
std::vector<Point<int>> Mapping::bresenham(const adjusted_ray_t &ray, const OccupancyGrid &map)
{
    /// TODO: Implement the Bresenham's line algorithm to find cells touched by the ray.


    // Correct range of ray if it's longer than our kMaxLaserDistance
    float range_corrected = ray.range;
    
    if (ray.range > kMaxLaserDistance_) {
        range_corrected = kMaxLaserDistance_;
    }

    // Grid cell of ray origin
    Point<int> start = global_position_to_grid_cell(ray.origin, map);

    
    // // Define global position of ray endpoint TODO: fix it
    // Point<float> endpoint_global = Point<float>(
    //         ray.origin.x + range_corrected * std::cos(ray.theta), 
    //         ray.origin.y + range_corrected * std::sin(ray.theta)
    //     );

    // // Define grid cell of endpoint
    // Point<float> endpoint = global_position_to_grid_cell(endpoint_global, map);

    
    // This might be a quicker way to get the endpoint's grid cell?
    Point<int> endpoint;
    endpoint.x = static_cast<int>(start.x + (range_corrected * std::cos(ray.theta) * map.cellsPerMeter()));
    endpoint.y = static_cast<int>(start.y + (range_corrected * std::sin(ray.theta) * map.cellsPerMeter()));
    

    ////////// BRESENHAM PSEUDOCODE //////////
    int x0 = static_cast<int> (start.x);
    int y0 = static_cast<int> (start.y);
    int x1 = static_cast<int> (endpoint.x);
    int y1 = static_cast<int> (endpoint.y);

    int dx = std::abs(x1 - x0);
    int dy = std::abs(y1 - y0);
    int sx = (x1 - x0 > 0) ? 1 : -1;
    int sy = (y1 - y0 > 0) ? 1 : -1;
    int err = dx - dy;
    
    int x = x0;
    int y = y0;

    std::vector<Point<int>> cells; 
    cells.push_back(Point<int>(x,y));

    while (x != x1 || y != y1) {
        int e2 = 2 * err;

        if (e2 >= -dy) {
            err = err - dy;
            x = x + sx;
        }

        if (e2 <= dx) {
            err = err + dx;
            y = y + sy;
        }
        cells.push_back(Point<int>(x,y));
    }
    return cells;
}

std::vector<Point<int>> Mapping::divideAndStepAlongRay(const adjusted_ray_t &ray, const OccupancyGrid &map)
{
    /// TODO: Implement an alternative approach to find cells touched by the ray.
    
    return {}; // Placeholder
}

void Mapping::increaseCellOdds(int x, int y, OccupancyGrid &map) {
    /// TODO: Increase the odds of the cell at (x,y)
    if (!initialized_)
        return;

    if (map(x,y) < 127) {
        map(x,y) += kHitOdds_;
    }
    else {
        map(x,y) = 127;
    }
}

void Mapping::decreaseCellOdds(int x, int y, OccupancyGrid &map) {
    /// TODO: Decrease the odds of the cell at (x,y)
    if (!initialized_)
        return;

    if (map(x,y) < -127) {
        map(x,y) -= kMissOdds_;
    }
    else {
        map(x,y) = -127;
    }

}
