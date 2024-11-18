from picamera2 import Picamera2
import libcamera
import logging
import cv2

logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more verbosity during development
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Camera:
    def __init__(self, camera_id, width, height, frame_duration=None):
        """
        Initializes the camera with the given parameters.
        :param camera_id: The ID of the camera to use.
        :param width: The width of the camera frame.
        :param height: The height of the camera frame.
        :param frame_duration: Optional frame duration limit for the camera.
        """
        logging.info("Initializing camera...")
        self.cap = Picamera2(camera_id)
        config = self.cap.create_preview_configuration(main={"size": (width, height), "format": "RGB888"})
        if frame_duration:
            config["controls"] = {'FrameDurationLimits': (frame_duration, frame_duration)}
        config["transform"] = libcamera.Transform(hflip=1, vflip=1)
        self.cap.align_configuration(config)
        self.cap.configure(config)
        self.cap.start()
        self.running = True
        logging.info("Camera initialized.")

    def capture_frame(self):
        """
        Captures a single frame from the camera.
        :return: The captured frame as a numpy array.
        """
        return self.cap.capture_array()

    def generate_frames(self):
        """
        Generates frames for streaming purposes.
        :return: A generator yielding encoded frames.
        """
        while self.running:
            # Capture the frame
            frame = self.capture_frame()

            # Process the frame (to be defined in subclasses)
            frame = self.process_frame(frame)

            # Encode the frame
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    def process_frame(self, frame):
        """
        This method will be overridden by subclasses to perform custom processing.
        """
        return frame

    def cleanup(self):
        """
        Cleans up the camera resources.
        """
        self.running = False
        if self.cap:
            logging.info("Releasing camera resources")
            self.cap.close()
            self.cap = None


