import time
import threading
import copy
import numpy as np


class OccupancyGridEmitter():
    def __init__(self, socket, event_name, period, emit=False):
        self.__socket           = socket
        self.__event_name       = event_name
        self.__period           = period
        self.__map_available    = False
        self.__map              = None
        self.__cells_b          = None
        # To turn off sending the map message, so it can be requested at a different frequency.
        self.__emit             = emit

        self.__lock = threading.Lock()

    def __lcm_map_to_dict(self):
        cells = self.__map.cells if self.__cells_b is None else self.__cells_b
        return {
            "utime" : self.__map.utime,
            "origin" : [self.__map.origin_x , self.__map.origin_y],
            "meters_per_cell" : self.__map.meters_per_cell,
            "width" : self.__map.width,
            "height" : self.__map.height,
            "num_cells" : self.__map.num_cells,
            "cells" : cells,
            # "slam_mode" : self.__map.slam_mode,
            # "slam_map_location" : self.__map.slam_map_location
        }

    def __compute_update(self, new_cells):
        cells = np.array(self.__map.cells)
        new_cells = np.array(new_cells)
        indices, = np.nonzero(1 - np.isclose(cells, new_cells))
        values = cells[indices]
        return indices, values

    def __get_update_dict(self, indices, values):
        return {
            "utime" : self.__map.utime,
            "indices" : indices.tolist(),
            "values" : values.tolist()
        }

    def reset(self):
        self.__lock.acquire()
        self.__map = None
        self.__cells_b = None
        self.__map_available = False
        self.__lock.release()

    def emit(self):
        if not self.__emit:
            return
        if self.__map_available:
            self.__lock.acquire()
            self.__socket.emit(self.__event_name, self.__lcm_map_to_dict())
            self.__map_available = False
            self.__lock.release()

    def __call__(self, data, cell_bytes=None):
        self.__lock.acquire()
        self.__map = data
        if cell_bytes is not None:
            self.__cells_b = cell_bytes
        self.__map_available = True
        self.__lock.release()

    def request_current_map(self):
        # Return an empty map if we have not received one yet or there is no new map to send.
        if self.__map is None or not self.__map_available:
            return {}

        self.__lock.acquire()
        map_data = self.__lcm_map_to_dict()
        self.__map_available = False
        self.__lock.release()
        return map_data

    def request_map_update(self, cells):
        if self.__map is None:
            return {}

        if len(cells) != self.__map.num_cells:
            return {}

        indices, values = self.__compute_update(cells)
        return self.__get_update_dict(indices, values)


class LidarEmitter():
    def __init__(self, socket, event_name, period):
        self.__socket           = socket
        self.__event_name       = event_name
        self.__period           = period
        self.__lidar_available  = False
        self.__lidar            = None

        self.__lock   = threading.Lock()

    def __lcm_lidar_to_dict(self):
        return {
            "utime" : self.__lidar.utime,
            "num_ranges" : self.__lidar.num_ranges,
            "ranges" : self.__lidar.ranges,
            "thetas" : self.__lidar.thetas,
            # The following are unused by the front end. Commented to save bandwidth.
            # "times" : self.__lidar.times,
            # "intensities" : self.__lidar.intensities,
        }

    def emit(self):
        if self.__lidar_available:
            self.__lock.acquire()
            self.__socket.emit(self.__event_name, self.__lcm_lidar_to_dict())
            self.__lidar_available = False
            self.__lock.release()

    def __call__(self, data):
        self.__lock.acquire()
        self.__lidar = data
        self.__lidar_available = True
        self.__lock.release()


class PoseEmitter():
    def __init__(self, socket, event_name, period):
        self.__socket           = socket
        self.__event_name       = event_name
        self.__period           = period
        self.__pose_available   = False
        self.__pose             = None

        self.__lock   = threading.Lock()

    def __lcm_pose_to_dict(self):
        return {
            "utime" : self.__pose.utime,
            "x" : self.__pose.x,
            "y" : self.__pose.y,
            "theta" : self.__pose.theta,
        }

    def emit(self):
        if self.__pose_available:
            self.__lock.acquire()
            self.__socket.emit(self.__event_name, self.__lcm_pose_to_dict())
            self.__pose_available = False
            self.__lock.release()

    def __call__(self, data):
        self.__lock.acquire()
        self.__pose = data
        self.__pose_available = True
        self.__lock.release()


class PathEmitter():
    def __init__(self, socket, event_name, period):
        self.__socket           = socket
        self.__event_name       = event_name
        self.__period           = period
        self.__path_available   = False
        self.__path             = None

        self.__lock   = threading.Lock()

    def __lcm_path_to_dict(self):
        return {
            "utime" : self.__path.utime,
            "path_length" : self.__path.path_length,
            "path" : self.__extract_path(self.__path.path_length, self.__path.path),
        }

    def __extract_path(self, path_length, path):
        parts = []
        for i in range(path_length):
            x = path[i].x
            y = path[i].y
            parts.append((x, y))
        return parts

    def emit(self):
        if self.__path_available:
            self.__lock.acquire()
            self.__socket.emit(self.__event_name, self.__lcm_path_to_dict())
            self.__path_available = False
            self.__lock.release()

    def __call__(self, data):
        self.__lock.acquire()
        self.__path = data
        self.__path_available = True
        self.__lock.release()


class ParticleEmitter():
    def __init__(self, socket, event_name, period):
        self.__socket           = socket
        self.__event_name       = event_name
        self.__period           = period
        self.__particle_available   = False
        self.__particle             = None

        self.__lock   = threading.Lock()

    def __lcm_particle_to_dict(self):
        return {
            "utime" : self.__particle.utime,
            "num_particles" : self.__particle.num_particles,
            "particles" : self.__extract_particle_poses(self.__particle.num_particles, self.__particle.particles),
        }

    def __extract_particle_poses(self, num_particles, particles):
        parts = []
        for i in range(num_particles):
            x = particles[i].pose.x
            y = particles[i].pose.y
            parts.append((x,y))
        return parts

    def emit(self):
        if self.__particle_available:
            self.__lock.acquire()
            self.__socket.emit(self.__event_name, self.__lcm_particle_to_dict())
            self.__particle_available = False
            self.__lock.release()

    def __call__(self, data):
        self.__lock.acquire()
        self.__particle = data
        self.__particle_available = True
        self.__lock.release()


class SLAMStatusEmitter():
    def __init__(self, socket, event_name, period):
        self.__socket           = socket
        self.__event_name       = event_name
        self.__period           = period
        self.__status_available = False
        self.__status           = None

        self.__lock   = threading.Lock()

    def __lcm_status_to_dict(self):
        return {
            "utime" : self.__status.utime,
            "slam_mode" : self.__status.slam_mode,
            "map_path" : self.__status.map_path
        }

    def emit(self):
        if self.__status_available:
            self.__lock.acquire()
            self.__socket.emit(self.__event_name, self.__lcm_status_to_dict())
            self.__status_available = False
            self.__lock.release()

    def __call__(self, data):
        self.__lock.acquire()
        self.__status = data
        self.__status_available = True
        self.__lock.release()


class CostmapEmitter():
    def __init__(self, socket, event_name, period):
        self.__socket           = socket
        self.__event_name       = event_name
        self.__period           = period
        self.__obstacle_available    = False
        self.__obstacle              = None

        self.__lock   = threading.Lock()

    def __lcm_obstacle_to_dict(self):
        return {
            "utime" : self.__obstacle.utime,
            "num_cells" : self.__obstacle.num_cells,
            "distances" : self.__obstacle.distances,
            "pairs" : self.__extract_pairs(self.__obstacle.num_cells, self.__obstacle.pairs)
        }

    def __extract_pairs(self, num_cells, pairs):
        parts = []
        for i in range(num_cells):
            x = pairs[i].x
            y = pairs[i].y
            parts.append((x,y))
        return parts

    def emit(self):
        if self.__obstacle_available:
            self.__lock.acquire()
            self.__socket.emit(self.__event_name, self.__lcm_obstacle_to_dict())
            self.__obstacle_available = False
            self.__lock.release()

    def __call__(self, data):
        self.__lock.acquire()
        self.__obstacle = data
        self.__obstacle_available = True
        self.__lock.release()
