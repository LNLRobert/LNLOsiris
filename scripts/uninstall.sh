#!/bin/bash
# Uninstallation script for Printer Dashboard

# Stop and disable the service
echo "Stopping and disabling the Printer Dashboard service..."
sudo systemctl stop LNLOsiris
sudo systemctl disable LNLOsiris

# Remove service file
echo "Removing service file..."
sudo rm /etc/systemd/system/LNLOsiris.service
sudo systemctl daemon-reload

# Remove installation directory
INSTALL_DIR="/home/osiris"  # Replace with the actual directory where the app is installed
echo "Removing application files from $INSTALL_DIR..."
sudo rm -rf "$INSTALL_DIR"

# Optionally remove Python dependencies
read -p "Do you want to remove Python dependencies installed by pip? (y/n) " REMOVE_PIP
if [ "$REMOVE_PIP" = "y" ]; then
    pip3 uninstall -y -r "$INSTALL_DIR/requirements.txt"
fi

echo "Uninstallation complete."