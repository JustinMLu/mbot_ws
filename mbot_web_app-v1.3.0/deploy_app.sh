#!/bin/bash
set -e  # Quit on error.

if [[ "$@" == *"--no-rebuild"* ]]; then
  echo "Webapp will be installed from the dist/ folder without rebuild."
else
  # Build the webapp.
  echo "#############################"
  echo "Building the webapp..."
  echo "#############################"
  npm install
  npm run build
fi

echo
echo "Installing the web app..."
echo
# Remove any old files to ensure we don't make duplicates.
sudo rm -rf /data/www/mbot/*
# Move the build files into the public repo.
sudo cp -r dist/* /data/www/mbot/

echo "Restarting Nginx..."
echo
sudo systemctl restart nginx

echo "#############################"
echo "Setting up Python server..."
echo "#############################"
echo

ENVS_ROOT="/home/$USER/.envs"
MBOT_APP_ENV="$ENVS_ROOT/mbot-app-env/"  # Virtual env where app is run.

if [ ! -d "/data/www/mbot/api" ]; then
    sudo mkdir /data/www/mbot/api
fi

# Copy over all the needed Python code.
sudo cp mbot_omni_app.py /data/www/mbot/api
sudo cp -r app/ /data/www/mbot/api

if [ ! -f "/etc/systemd/system/mbot-web-server.service" ]; then
  # This is the first time installing.
  sudo cp config/mbot-web-server.service /etc/systemd/system/
  # Fill in the path to this env and the correct Python path.
  sudo sed -i "s#WEBAPP_ENV_PATH#$MBOT_APP_ENV#" /etc/systemd/system/mbot-web-server.service

  echo "Enabling MBot Web App service."
  # Reload the service.
  sudo systemctl daemon-reload
  sudo systemctl enable mbot-web-server.service
  sudo systemctl start mbot-web-server.service
else
  # This service has already been installed. Pull new changes then restart it.
  sudo cp config/mbot-web-server.service /etc/systemd/system/
  # Fill in the path to this env.
  sudo sed -i "s#WEBAPP_ENV_PATH#$MBOT_APP_ENV#" /etc/systemd/system/mbot-web-server.service

  echo "MBot Web App service is already enabled. Restarting it."
  sudo systemctl daemon-reload
  sudo systemctl restart mbot-web-server.service
fi

echo
echo "Done! The webapp is now available at http://localhost on this computer or http://[MBOT_IP] on the network."
