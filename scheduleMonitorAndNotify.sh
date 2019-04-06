#!/bin/sh

sudo cp $(pwd)/minute-timer.timer /lib/systemd/system/
sudo chmod 664 /lib/systemd/system/minute-timer.timer
sudo systemctl enable /etc/systemd/system/minute-timer.timer
sudo systemctl start  /etc/systemd/system/minute-timer.timer
echo "Successfully added minute timer"

sed -i "s+/home/pi+$(pwd)+g" monitor-and-notify.service
sudo cp $(pwd)/monitor-and-notify.service /lib/systemd/system/
sudo chmod 664 /lib/systemd/system/monitor-and-notify.service
sudo systemctl daemon-reload
sudo systemctl enable monitor-and-notify.service
echo "Successfully added service to systemd. Restarting device..."
sudo reboot