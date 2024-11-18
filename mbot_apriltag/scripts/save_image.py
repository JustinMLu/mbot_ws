from flask import Flask, Response, render_template, request, jsonify
import cv2
import os

from utils.utils import register_signal_handlers
from utils.config import CAMERA_CONFIG
from utils.camera import Camera

"""
This script displays the video live stream to browser with a button "save image".
When you click the button, the current frame will be saved to "/images"

url: http://your_mbot_ip:5001
"""

class CameraWithSave(Camera):
    def __init__(self, camera_id, width, height):
        super().__init__(camera_id, width, height)
        self.image_count = 0

    def save_frame(self, save_path):
        """
        Saves the current frame to the given path.
        :param save_path: Path to save the captured frame.
        :return: True if saved successfully, False otherwise.
        """
        frame = self.capture_frame()
        if frame is not None:
            cv2.imwrite(save_path, frame)
            return True
        return False

app = Flask(__name__)

@app.route('/')
def video_page():
    return render_template('image_save_page.html')

@app.route('/video')
def video():
    return Response(camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/save-image', methods=['POST'])
def save_image():
    # Extract the image save path from the POST request
    camera.image_count += 1
    save_path = f"images/image{camera.image_count}.jpg"
    if camera.save_frame(save_path):
        return jsonify({"message": "Image saved successfully", "path": save_path}), 200
    else:
        return jsonify({"message": "Failed to capture image"}), 500

if __name__ == '__main__':
    camera_id = CAMERA_CONFIG["camera_id"]
    image_width = CAMERA_CONFIG["image_width"]
    image_height = CAMERA_CONFIG["image_height"]

    camera = CameraWithSave(camera_id, image_width, image_height)
    register_signal_handlers(camera.cleanup)
    app.run(host='0.0.0.0', port=5001, threaded=True)
