#!/bin/bash
set -e  # Quit on error.

SRV_NAME=mbot-rplidar-driver

sudo cp $SRV_NAME.service /etc/systemd/system/$SRV_NAME.service
sudo systemctl daemon-reload
sudo systemctl enable $SRV_NAME.service
