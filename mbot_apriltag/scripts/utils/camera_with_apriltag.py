import cv2, time
from apriltag import apriltag
import numpy as np
import lcm
from utils.config import TAG_CONFIG
from utils.utils import rotation_matrix_to_euler_angles, rotation_matrix_to_quaternion, retry_detection
from utils.camera import Camera

class CameraWithAprilTag(Camera):
    def __init__(self, camera_id, width, height, calibration_data, frame_duration=None):
        super().__init__(camera_id, width, height, frame_duration)
        config = TAG_CONFIG
        self.frame_count = 0
        self.detections = dict()
        self.detector = apriltag(config["tag_family"], threads=1)
        self.skip_frames = config["skip_frames"]
        self.tag_size = config["tag_size"]
        self.small_tag_size = config["small_tag_size"]
        self.camera_matrix = calibration_data['camera_matrix']
        self.dist_coeffs = calibration_data['dist_coeffs']
        self.object_points = np.array([
            [-self.tag_size/2,  self.tag_size/2, 0],  # Top-left corner
            [ self.tag_size/2,  self.tag_size/2, 0],  # Top-right corner
            [ self.tag_size/2, -self.tag_size/2, 0],  # Bottom-right corner
            [-self.tag_size/2, -self.tag_size/2, 0],  # Bottom-left corner
        ], dtype=np.float32)
        self.small_object_points = np.array([
            [-self.small_tag_size/2,  self.small_tag_size/2, 0],  # Top-left corner
            [ self.small_tag_size/2,  self.small_tag_size/2, 0],  # Top-right corner
            [ self.small_tag_size/2, -self.small_tag_size/2, 0],  # Bottom-right corner
            [-self.small_tag_size/2, -self.small_tag_size/2, 0],  # Bottom-left corner
        ], dtype=np.float32)
        self.lcm = lcm.LCM("udpm://239.255.76.67:7667?ttl=0")

    def process_frame(self, frame):
        # Increment frame count and check if it's time for detection
        self.frame_count += 1
        if self.frame_count % self.skip_frames == 0:
            # Convert frame to grayscale and detect tags
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.detections = retry_detection(self.detector, gray, retries=3)

        # Annotate frame if detections are present
        if self.detections:
            for idx, detection in enumerate(self.detections):
                self.draw_tag_and_label(frame, detection, idx)

        return frame

    def draw_tag_and_label(self, frame, detection, idx):
        # Drawing and labeling logic for detected tags
        x, y, z, roll, pitch, yaw, quaternion = self.decode_detection(detection)
        corners = np.array(detection['lb-rb-rt-lt'], dtype=np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [corners], isClosed=True, color=(0, 255, 0), thickness=2)

        # Position text annotation
        pos_text = f"Tag ID {detection['id']}: x={x:.2f}, y={y:.2f}, z={z:.2f},"
        orientation_text = f" roll={roll:.2f}, pitch={pitch:.2f}, yaw={yaw:.2f}"
        vertical_pos = 40 * (idx + 1)
        text = pos_text + orientation_text

        # Draw the background rectangle and text
        (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        box_coords = ((10, vertical_pos - text_height - 10), (10 + text_width, vertical_pos + baseline))
        cv2.rectangle(frame, box_coords[0], box_coords[1], (200, 200, 200), cv2.FILLED)
        cv2.putText(frame, text, (10, vertical_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    def decode_detection(self, detect):
        # Pose estimation for detected tag
        if detect['id'] < 10:  # Big tag
            image_points = np.array(detect['lb-rb-rt-lt'], dtype=np.float32)
            retval, rvec, tvec = cv2.solvePnP(self.object_points, image_points, self.camera_matrix, self.dist_coeffs, flags=cv2.SOLVEPNP_IPPE_SQUARE)

        if detect['id'] >= 10:  # Small tag at center
            image_points = np.array(detect['lb-rb-rt-lt'], dtype=np.float32)
            retval, rvec, tvec = cv2.solvePnP(self.small_object_points, image_points, self.camera_matrix, self.dist_coeffs, flags=cv2.SOLVEPNP_IPPE_SQUARE)

        # Convert rotation vector to a rotation matrix
        rotation_matrix, _ = cv2.Rodrigues(rvec)

        # Calculate Euler angles
        roll, pitch, yaw = rotation_matrix_to_euler_angles(rotation_matrix)

        quaternion = rotation_matrix_to_quaternion(rotation_matrix)

        # return x, y, z, roll, pitch, yaw
        return tvec[0][0], tvec[1][0], tvec[2][0], roll, pitch, yaw, quaternion
