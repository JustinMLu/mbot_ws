#!/bin/bash
set -e  # Quit on error.

echo "Installing Nginx..."
echo
sudo apt install nginx -y

# Remove default nginx config
if [ -f "/etc/nginx/sites-enabled/default" ]; then
    sudo rm /etc/nginx/sites-enabled/default
fi

# Create the directory for the mbot web application
if [ ! -d "/data/www/mbot/" ]; then
    sudo mkdir -p /data/www/mbot/
    sudo chmod -R a+rwx /data/www/mbot
fi

echo
echo "Setting up Nginx"
echo
if [ -f "/etc/nginx/nginx.conf" ]; then
    sudo rm /etc/nginx/nginx.conf
fi
sudo cp config/nginx.conf /etc/nginx/nginx.conf
