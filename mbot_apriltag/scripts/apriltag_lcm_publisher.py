import cv2
import time
import numpy as np
from apriltag import apriltag
from mbot_lcm_msgs.mbot_apriltag_array_t import mbot_apriltag_array_t
from mbot_lcm_msgs.mbot_apriltag_t import mbot_apriltag_t

from utils.utils import register_signal_handlers, retry_detection
from utils.config import CAMERA_CONFIG
from utils.camera_with_apriltag import CameraWithAprilTag
"""
This script publish apriltag lcm message to MBOT_APRILTAG_ARRAY
"""

class AprilTagPublisher(CameraWithAprilTag):
    def __init__(self, camera_id, width, height, calibration_data, frame_duration=None):
        super().__init__(camera_id, width, height, calibration_data, frame_duration)

    def detect(self):
        while True:
            self.frame_count += 1
            frame = self.cap.capture_array()

            # Process for tag detection only every 5th frame
            if self.frame_count % self.skip_frames == 0:
                # Convert frame to grayscale for detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Retry logic, prevent quit from one detection fail
                self.detections = retry_detection(self.detector, gray, 3)

                self.publish_apriltag()

    def publish_apriltag(self):
        """
        Publish the apriltag message
        """
        msg = mbot_apriltag_array_t()
        msg.array_size = len(self.detections)
        msg.detections = []
        if msg.array_size > 0:
            for detection in self.detections:
                x, y, z, roll, pitch, yaw, quaternion = self.decode_detection(detection)

                apriltag = mbot_apriltag_t()
                apriltag.tag_id = detection['id']
                apriltag.pose.x = x
                apriltag.pose.y = y
                apriltag.pose.z = z
                apriltag.pose.angles_rpy = [roll, pitch, yaw]
                apriltag.pose.angles_quat = quaternion
                msg.detections.append(apriltag)

        self.lcm.publish("MBOT_APRILTAG_ARRAY", msg.encode())

if __name__ == '__main__':
    camera_id = CAMERA_CONFIG["camera_id"]
    image_width = CAMERA_CONFIG["image_width"]
    image_height = CAMERA_CONFIG["image_height"]
    fps = CAMERA_CONFIG["fps"]

    calibration_data = np.load('cam_calibration_data.npz')
    frame_duration = int((1./fps)*1e6)
    camera = AprilTagPublisher(camera_id, image_width, image_height, calibration_data, frame_duration)
    register_signal_handlers(camera.cleanup)
    camera.detect()


