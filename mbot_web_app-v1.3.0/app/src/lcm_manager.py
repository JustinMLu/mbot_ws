import lcm
import time
import select

from mbot_lcm_msgs import twist2D_t
from mbot_lcm_msgs import occupancy_grid_t
from mbot_lcm_msgs import particles_t
from mbot_lcm_msgs import pose2D_t
from mbot_lcm_msgs import lidar_t
# from mbot_lcm_msgs import planner_request_t
from mbot_lcm_msgs import path2D_t
from mbot_lcm_msgs import mbot_slam_reset_t
from mbot_lcm_msgs import slam_status_t
# from mbot_lcm_msgs import costmap_t
from app import lcm_settings


class LcmCommunicationManager:
    def __init__(self, callback_dict={}):
        '''
        Runs the lcm handler thread

        :param callback_dict: contains lcm channel names as keys and
            callback functions as values. The functions are called when
            a message on their corresponding channel is handled. The decoded
            data will be passed to the callback function.
        '''
        self._lcm = lcm.LCM(lcm_settings.LCM_ADDRESS)
        self.subscriptions = []
        self._callback_dict = callback_dict

        ###################################
        # TODO: VERIFY AND FIX - ENSURE DATA IS SAVED
        self.__subscribe(lcm_settings.SLAM_MAP_CHANNEL, self._occupancy_grid_listener)
        self.__subscribe(lcm_settings.ODOMETRY_CHANNEL, self._position_listener)
        self.__subscribe(lcm_settings.LIDAR_CHANNEL, self.lidar_listener)
        self.__subscribe(lcm_settings.SLAM_POSE_CHANNEL, self.pose_listener)
        self.__subscribe(lcm_settings.CONTROLLER_PATH_CHANNEL, self.path_listener)
        self.__subscribe(lcm_settings.SLAM_PARTICLES_CHANNEL, self.particle_listener)
        self.__subscribe(lcm_settings.SLAM_STATUS_CHANNEL, self.slam_status_listener)
        # self.__subscribe(lcm_settings.COSTMAP_CHANNEL, self.obstacle_listener)
        ###################################

    def request_current_map(self):
        return self._callback_dict[lcm_settings.SLAM_MAP_CHANNEL].request_current_map()

    def request_map_update(self, cells):
        return self._callback_dict[lcm_settings.SLAM_MAP_CHANNEL].request_map_update(cells)

    def update_callback(self, channel, function):
        self._callback_dict[channel] = function

    def __subscribe(self, channel, handler):
        self.subscriptions.append(self._lcm.subscribe(channel, handler))

    def handle(self):
        self._lcm.handle()

    def handleOnce(self):
        # This is a non-blocking handle, which only calls handle if a message is ready.
        rfds, wfds, efds = select.select([self._lcm.fileno()], [], [], 0)
        if rfds:
            self._lcm.handle()

    def emit_msgs(self):
        for channel in self._callback_dict.keys():
            self._callback_dict[channel].emit()

    def publish_motor_commands(self, vx, vy, wz):
        cmd = twist2D_t()
        cmd.vx = vx; cmd.vy = vy; cmd.wz = wz
        cmd.utime = int(time.time() * 1000)
        self._lcm.publish(lcm_settings.MBOT_MOTOR_COMMAND_CHANNEL, cmd.encode())

    def publish_plan_data(self, goal: pose2D_t, plan: bool):
        pass  # TODO
        # goal_pose = pose2D_t()
        # goal_pose.utime = int(time.time() * 1000)
        # goal_pose.x = float(goal[0])
        # goal_pose.y = float(goal[1])
        # goal_pose.theta = 0.0

        # total_pose = planner_request_t()
        # total_pose.utime = int(time.time() * 1000)
        # total_pose.goal = goal_pose
        # total_pose.require_plan = plan

        # self._lcm.publish(lcm_settings.PATH_REQUEST, total_pose.encode())

    def publish_slam_reset(self, mode, map_file=None, retain_pose=False):
        # Reset the map manager so it does not continue to send old maps.
        self._callback_dict[lcm_settings.SLAM_MAP_CHANNEL].reset()

        slam_reset = mbot_slam_reset_t()
        slam_reset.utime = int(time.time() * 1000)
        slam_reset.slam_mode = int(mode)
        slam_reset.retain_pose = retain_pose
        if map_file is not None:
            slam_reset.slam_map_location = map_file

        self._lcm.publish(lcm_settings.MBOT_SYSTEM_RESET, slam_reset.encode())

    def reset_odometry_publisher(self):
        cmd = pose2D_t()
        cmd.x = 0.0
        cmd.y = 0.0
        cmd.theta = 0.0

        self._lcm.publish(lcm_settings.RESET_ODOMETRY_CHANNEL, cmd.encode())

    def _position_listener(self, channel, data):
        decoded_data = pose2D_t.decode(data)
        if channel in self._callback_dict.keys():
            self._callback_dict[channel](decoded_data)

    def _occupancy_grid_listener(self, channel, data):
        decoded_data = occupancy_grid_t.decode(data)
        cell_bytes = data[-decoded_data.num_cells:]
        if channel in self._callback_dict.keys():
            self._callback_dict[channel](decoded_data, cell_bytes)

    # Temporarily remove. Unclear if this is published by botlab.
    # def obstacle_listener(self, channel, data):
    #     decoded_data = costmap_t.decode(data)
    #     if channel in self._callback_dict.keys():
    #         self._callback_dict[channel](decoded_data)

    def lidar_listener(self, channel, data):
        decoded_data = lidar_t.decode(data)
        if channel in self._callback_dict.keys():
            self._callback_dict[channel](decoded_data)

    def pose_listener(self, channel, data):
        decoded_data = pose2D_t.decode(data)
        if channel in self._callback_dict.keys():
            self._callback_dict[channel](decoded_data)

    def path_listener(self, channel, data):
        decoded_data = path2D_t.decode(data)
        if channel in self._callback_dict.keys():
            self._callback_dict[channel](decoded_data)

    def particle_listener(self, channel, data):
        decoded_data = particles_t.decode(data)
        if channel in self._callback_dict.keys():
            self._callback_dict[channel](decoded_data)

    def slam_status_listener(self, channel, data):
        decoded_data = slam_status_t.decode(data)
        if channel in self._callback_dict.keys():
            self._callback_dict[channel](decoded_data)
