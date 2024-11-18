#!/bin/bash
set -e  # Quit on error.

# Make the build folder first. Otherwise, it gets made with the sudo command below and will be owned by the root user.
if [ ! -d "build/" ]; then
    mkdir build
fi

# Python installation.
echo "Installing the Python MBot Bridge code..."
echo

# Install the dependencies globally first with apt to minimize the number of packages installed with pip.
sudo apt install -y python3-yaml \
	                python3-websockets \
                    python3-numpy

# Get the distribution ID.
distro_id=$(grep ^ID= /etc/os-release | cut -d '=' -f 2 | tr -d '"')

# Warning: As of Debian 12 (bookworm) a warning prevents you from globally installing Python packages with pip,
# as per PEP 668. We're doing it anyway since we want mbot_bridge globally installed. Only do this on an MBot.
if [ "$distro_id" = "debian" ] || [ "$distro_id" = "raspbian" ]; then
    # Get the Debian version number
    debian_version=$(grep VERSION_ID /etc/os-release | cut -d '"' -f 2)
    if [ "$debian_version" -ge "12" ]; then
        echo
        echo "Debian 12 or above detected. Globally installing mbot_bridge, ignoring warnings."
        echo
        sudo python3 -m pip install . --break-system-packages
    else
        sudo python3 -m pip install .
    fi
else
    sudo python3 -m pip install .
fi

# Websockets C++ dependency installation.
echo
echo "Installing dependencies for the API..."
echo
wget https://github.com/zaphoyd/websocketpp/archive/refs/tags/0.8.2.tar.gz
tar -xzf 0.8.2.tar.gz
cd websocketpp-0.8.2/
mkdir build && cd build
cmake ..
make
sudo make install

echo
echo "Cleaning up..."
echo
cd ../../
rm 0.8.2.tar.gz
rm -rf websocketpp-0.8.2/

# C++ API installation.
echo
echo "Building the C++ MBot API..."
echo

cd build
cmake ../mbot_cpp/
make

echo
echo "Installing the C++ MBot API..."
echo
sudo make install
cd ..

# Install service.
echo
echo "Installing the MBot Bridge service..."
echo
# Copy the services.
sudo cp services/mbot-bridge.service /etc/systemd/system/mbot-bridge.service

# Enable the services.
sudo systemctl daemon-reload
sudo systemctl enable mbot-bridge.service
sudo systemctl restart mbot-bridge.service

echo
echo "MBot Bridge setup complete."
echo
