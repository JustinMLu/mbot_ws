#!/usr/bin/env python3
from flask import Flask, Response
import numpy as np

from utils.utils import register_signal_handlers
from utils.config import CAMERA_CONFIG
from utils.camera_with_apriltag import CameraWithAprilTag

"""
Features:
1. Displays the video live stream with apriltag detection to the browser.
2. Display the pose estimate values.

visit: http://your_mbot_ip:5001
"""

app = Flask(__name__)
@app.route('/')
def video():
    return Response(camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    camera_id = CAMERA_CONFIG["camera_id"]
    image_width = CAMERA_CONFIG["image_width"]
    image_height = CAMERA_CONFIG["image_height"]
    fps = CAMERA_CONFIG["fps"]

    frame_duration = int((1./fps) * 1e6)
    calibration_data = np.load('cam_calibration_data.npz')

    camera = CameraWithAprilTag(camera_id, image_width, image_height,
                                      calibration_data, frame_duration)
    register_signal_handlers(camera.cleanup)
    app.run(host='0.0.0.0', port=5001)
