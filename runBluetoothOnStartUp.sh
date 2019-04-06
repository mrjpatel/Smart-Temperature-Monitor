#!/bin/sh

sudo cp $(pwd)/bluetooth-notify.service /lib/systemd/system/
sed -i "s+/home/pi/default+$(pwd)+g" /lib/systemd/system/bluetooth-notify.service
sudo chmod 664 /lib/systemd/system/bluetooth-notify.service
sudo systemctl daemon-reload
sudo systemctl enable bluetooth-notify.service
echo "Successfully added service to systemd. Restarting device..."
sudo reboot