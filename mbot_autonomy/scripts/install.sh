#!/bin/bash

# Quit if any command returns a non-zero status (errors).
set -e

MBOT_TYPE=""

print_usage() {
    echo "Usage:"
    echo
    echo "  ./scripts/install.sh -t <TYPE>"
    echo
    echo "with <TYPE> set to either OMNI or DIFF."
}

while getopts ":t:" opt; do
    case $opt in
        t)
            MBOT_TYPE=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            ;;
    esac
done

if [ -z "$MBOT_TYPE" ]; then
    echo "Error: MBot type is required."
    print_usage
    exit 1
fi

if [[ "$MBOT_TYPE" != "DIFF" ]] && [[ "$MBOT_TYPE" != "OMNI" ]]; then
    echo "Error: Unrecognized MBot type: $MBOT_TYPE"
    print_usage
    exit 1
fi

# Print initial msg.
echo "Building the MBot Autonomy code for MBot $MBOT_TYPE..."
echo

# Build the code.
if [ ! -d "build/" ]; then
    mkdir build
fi
cd build
cmake -DMBOT_TYPE=$MBOT_TYPE ..
make
sudo make install
cd ..

# Define and copy the services to system directory.
SERVICE_LIST="mbot-motion-controller
              mbot-slam"

for serv in $SERVICE_LIST
do
    sudo cp services/$serv.service /etc/systemd/system/$serv.service
done

# Enable the services.
sudo systemctl daemon-reload

echo
if [[ "$@" == *"--no-enable"* ]]; then
    echo "Services installed but not enabled."
else
    echo "Enabling and starting services..."
    # Enable all the services.
    for serv in $SERVICE_LIST
    do
        sudo systemctl enable $serv.service
        sudo systemctl restart $serv.service
    done
fi

# Success message.
echo "Installed the following services:"
echo
for serv in $SERVICE_LIST
do
    echo "    $serv.service"
done
echo

echo "Done!"
