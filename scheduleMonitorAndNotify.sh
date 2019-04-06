#!/bin/sh

sudo cp $(pwd)/minute-timer.timer /etc/systemd/system/
sudo cp $(pwd)/minute-timer.target /etc/systemd/system/
sudo chmod 664 /etc/systemd/system/minute-timer.timer
sudo chmod 644 /etc/systemd/system/minute-timer.target
sudo systemctl enable minute-timer.timer
sudo systemctl start  minute-timer.timer
echo "Successfully added minute timer"

sed -i "s+/home/pi+$(pwd)+g" monitor-and-notify.service
sudo cp $(pwd)/monitor-and-notify.service /lib/systemd/system/
sudo chmod 664 /lib/systemd/system/monitor-and-notify.service
sudo systemctl daemon-reload
sudo systemctl enable monitor-and-notify.service
echo "Successfully added service to systemd. Restarting device..."
sudo reboot
