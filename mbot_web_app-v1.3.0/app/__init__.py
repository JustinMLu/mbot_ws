from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from app.src import lcm_settings
from app.src.lcm_manager import LcmCommunicationManager
from app.src.lcm_callbacks import (
    LidarEmitter,
    CostmapEmitter,
    OccupancyGridEmitter,
    PoseEmitter,
    PathEmitter,
    ParticleEmitter,
    SLAMStatusEmitter
)


class ConnectionManager(object):
    def __init__(self, connected=False):
        self.connected = connected


# The Flask app gets created here. Other Python functions and classes should be
# stored in the "src" folder.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'development key'
# Note: For debugging, add logger=True, engineio_logger=True.
socket = SocketIO(app, cors_allowed_origins='*')  #, max_http_buffer_size = 10000000000)
CORS(app)

lcm_callback_dict = {
    lcm_settings.SLAM_MAP_CHANNEL: OccupancyGridEmitter(socket, 'map', period=0.5, emit=False),
    lcm_settings.LIDAR_CHANNEL: LidarEmitter(socket, 'lidar', period=0.5),
    lcm_settings.SLAM_POSE_CHANNEL: PoseEmitter(socket, 'pose', period=0.5),
    lcm_settings.CONTROLLER_PATH_CHANNEL: PathEmitter(socket, 'path', period=0.5),
    lcm_settings.SLAM_PARTICLES_CHANNEL: ParticleEmitter(socket, 'particles', period=0.5),
    lcm_settings.SLAM_STATUS_CHANNEL: SLAMStatusEmitter(socket, 'slam_status', period=0.5),
    lcm_settings.COSTMAP_CHANNEL: CostmapEmitter(socket, 'obstacles', period=0.5)
}

lcm_manager = LcmCommunicationManager(lcm_callback_dict)
connection_manager = ConnectionManager()

from app import routes

