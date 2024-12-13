#!/bin/bash
# Install dependencies
sudo apt update
sudo apt install -y python3 python3-pip
pip3 install flask requests

# Set up service
sudo cp LNLOsiris.service /etc/systemd/system/
sudo systemctl enable LNLOsiris
sudo systemctl start LNLOsiris