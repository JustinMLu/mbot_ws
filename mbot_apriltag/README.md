> This program is modified for ROB550 F24 Use
## mbot_apriltag
This project provides tools for camera calibration and Apriltag pose estimation, tailored for use with the MBot equipped with a **Raspberry Pi 5**.

The scripts offer:
- Streaming live camera feeds to a browser for real-time viewing and interaction.
- Publishing and subscribing to Apriltag LCM messages.

## Installation
1. Directly install from the official [github repo](https://github.com/AprilRobotics/apriltag):
    ```bash
    git clone https://github.com/AprilRobotics/apriltag.git
    ```

2. Following the install [instruction](https://github.com/AprilRobotics/apriltag) there:
    ```bash
    cd apriltag
    cmake -B build -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=OFF
    sudo cmake --build build --target install
    ```

3. Add python path
    ```bash
    echo 'export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.11/site-packages' >> ~/.bashrc
    ```

4. Clone this repo
## Usage and Features
### Run scripts
> Visit `http://your_mbot_ip:5001` to see the stream video
- `python3 video_streamer.py`
    - Only shows the video stream, to test your camera and your dependency installation
- `python3 save_image.py`
    - Shows the video stream, we use it to save image to `/images` for camera calibration
- `python3 camera_calibration.py`
    - Use the images from `/images` and output calibration result as `cam_calibration_data.npz`. The result will be used directly by apriltag_streamer.py you don't have to modify anything.
- `python3 apriltag_lcm_publisher.py`
    - Publish apriltag lcm message over `MBOT_APRILTAG_ARRAY`
- `python3 apriltag_lcm_subscriber.py`
    - Listen to `MBOT_APRILTAG_ARRAY` for apriltag lcm message
- `python3 apriltag_demo.py`
    - Displays the video live stream with apriltag detection to the browser

## Troubleshooting
### libapriltag.so.3
If you encounter the following runtime error: "ImportError: libapriltag.so.3: cannot open shared object file: No such file or directory," follow these steps:

1. Verify the Installation Location

    The library is typically installed in /usr/local/lib or /usr/lib. Check these locations:
    ```bash
    $ ls /usr/local/lib | grep libapriltag
    ```
    ```bash
    $ ls /usr/lib | grep libapriltag
    ```
    - If you see "libapriltag.so.3" in the output, proceed to the next step.

2. Update the Library Cache

    If the library is in a standard location but still not found, you may need to update your system's library cache. Run the following command to refresh it:

    ```bash
    $ sudo ldconfig
    ```
    - After updating, try running video_streamer.py again to check if the issue is resolved.