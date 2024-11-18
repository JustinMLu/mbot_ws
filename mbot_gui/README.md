# MBot GUI

The legacy GUI built on VX.

## Installation

Dependencies:
```bash
sudo apt install libgtk2.0-dev \
                 mesa-common-dev \
                 libgl1-mesa-dev \
                 libglu1-mesa-dev \
                 libusb-dev libusb-1.0-0-dev \
                 libdc1394-dev libgsl-dev
```

```bash
mkdir build
cd build
cmake .. && make
```

## Usage

From the root directory, after building, do:
```bash
source setenv.sh
./build/botgui
```
