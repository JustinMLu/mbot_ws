import numpy as np
import signal
import atexit
import time

def rotation_matrix_to_euler_angles(R):
    """
    Calculate Euler angles (roll, pitch, yaw) from a rotation matrix.
    Assumes the rotation matrix uses the XYZ convention.
    """
    sy = np.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])
    singular = sy < 1e-6

    if not singular:
        x = np.arctan2(R[2, 1], R[2, 2])
        y = np.arctan2(-R[2, 0], sy)
        z = np.arctan2(R[1, 0], R[0, 0])
    else:
        x = np.arctan2(-R[1, 2], R[1, 1])
        y = np.arctan2(-R[2, 0], sy)
        z = 0

    return np.rad2deg(x), np.rad2deg(y), np.rad2deg(z)  # Convert to degrees

def rotation_matrix_to_quaternion(R):
    """
    Convert a rotation matrix to a quaternion.
    """
    q_w = np.sqrt(1.0 + R[0, 0] + R[1, 1] + R[2, 2]) / 2.0
    q_x = (R[2, 1] - R[1, 2]) / (4.0 * q_w)
    q_y = (R[0, 2] - R[2, 0]) / (4.0 * q_w)
    q_z = (R[1, 0] - R[0, 1]) / (4.0 * q_w)
    return [q_w, q_x, q_y, q_z]

def register_signal_handlers(cleanup_function):
    """
    Register signal handlers for graceful shutdown.
    """
    def signal_handler(sig, frame):
        print(f'Received signal: {sig}, initiating cleanup...')
        cleanup_function()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    atexit.register(cleanup_function)


def retry_detection(detector, gray_frame, retries=3):
    # prevent quit from one detection fail
    for attempt in range(retries):
        try:
            return detector.detect(gray_frame)
        except RuntimeError as e:
            if "Unable to create" in str(e) and attempt < retries - 1:
                print(f"Detection failed, retrying... Attempt {attempt + 1}")
                time.sleep(0.2)
            else:
                raise
    return ()  # Return an empty tuple if detection ultimately fails