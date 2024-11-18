#!/bin/bash
set -e  # Quit on error.

# Update the submodule.
echo "Updating RPLidar SDK submodule..."
echo
git pull && git submodule update --init --recursive

# Build the code.
echo
echo "Building the code..."
echo
if [ ! -d "build/" ]; then
    mkdir build
fi
cd build
cmake ..
make
sudo make install
cd ..

SRV_NAME=mbot-rplidar-driver
echo
echo "Installing $SRV_NAME.service..."

# Install services.
sudo cp services/$SRV_NAME.service /etc/systemd/system/$SRV_NAME.service
sudo systemctl daemon-reload
sudo systemctl enable $SRV_NAME.service
sudo systemctl restart $SRV_NAME.service

echo
echo "Done!"
