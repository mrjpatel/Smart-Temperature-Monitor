#!/bin/sh

sed -i "s+/home/pi+$(pwd)+g" bluetooth-notify.service
sed -i "s+sample+greenhouse_bluetooth+g" bluetooth-notify.service
sudo cp $(pwd)/bluetooth-notify.service /lib/systemd/system/
sudo chmod 664 /lib/systemd/system/bluetooth-notify.service
sudo systemctl daemon-reload
sudo systemctl enable bluetooth-notify.service
echo "Successfully added service to systemd. Restarting device..."
sudo reboot