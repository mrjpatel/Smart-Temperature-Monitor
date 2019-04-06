#!/bin/sh

sed -i "s+/home/pi/sample+$(pwd)/greenhouse_bluetooth+g" bluetooth-notify.service
sudo cp $(pwd)/bluetooth-notify.service /lib/systemd/system/
sudo chmod 664 /lib/systemd/system/bluetooth-notify.service
sudo systemctl daemon-reload
sudo systemctl enable bluetooth-notify.service
sudo reboot