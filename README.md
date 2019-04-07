# TemperatureMonitoringSystem

This project contains a small IoT application using Raspberry Pi and Sense HAT in Python language.

# Prerequisites

### Hardware Requirements
- Raspberry Pi model 3 B/B+ or greater
- SenseHat that is compatible with your Raspberry Pi
- Smartphone for notifications

### Software Requirements
- This code uses Python 3.5 or > Python 3.5
- PushBullet Account ([https://www.pushbullet.com/](https://www.pushbullet.com/))
- Python PyBluz 
- Python Seaborn

# Installation of Prerequisites
### PushBullet
 1. Register and Log into your PushBullet account
 2. Go into Settings -> Account -> Create Access Token
 3. Copy the randomly generated string and insert it into the "accessToken.json" file in this repository

### Update System and install SenseHat Module
Run the following commands on your Raspberry Pi
```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get dist-upgrade
$ sudo apt-get install sense-hat
$ sudo reboot
```

### PyBluz
Run the following commands on your Raspberry Pi
```bash
$ sudo apt install bluetooth bluez blueman
$ pip3 install pybluez
$ sudo apt install bluez-tools
```

### Seaborn
Run the following commands on your Raspberry Pi
```bash
$ sudo pip3 install seaborn
```

# Programs
## Monitor and Notify
#### Description
This program will record the current tempurature and humidity from the SenseHat, log it to a SQLite DB on the Raspberry Pi, check if it is outside the configured ranges (config.json) and send an alert to your smartphone via push bullet. 
**Note: This will only send a notification once per day**
#### How to run
```bash
$ python3 monitorAndNotify.py
```
#### Scheduling
This program works ideally when it is scheduled. This can be done via CRON on Raspberry Pi. The following script can be used to start the systemd scheduling.
**Note: this script will restart your device for it to start**
```bash
$ bash sudo scheduleMonitorAndNotify.sh
```

## Create Report
#### Description
This program generates a report on each days climate reading data. This file contains a separate row for each days’ data that resides in the database. If each piece of data is within the configured temperature and humidity range then the status of OK is applied, otherwise the label of BAD is applied. An appropriate message detailing the error(s) is included.
#### How to run
```bash
$ python3 createReport.py
```

## Proximity Bluetooth Notify
#### Description
 This program uses Bluetooth to detect nearby devices and when connected send an appropriate message stating the current temperature, humidity and if these fall within the configured temperature and humidity range. The message is sent via PushBullet.
#### How to run
```bash
$ python3 greenhouse_bluetooth.py
```
#### Running on start up
Run this script to enable this script on start up.
**Note: this script will restart your device for it to start**
```bash
$ bash sudo runBluetoothOnStartUp.sh
```

## Analytics 
#### Description
TBD
#### How to run
```bash
$ python3 analytics.py
```
#### Result
The result of this is:
- Heat Map - (heatmap.png) which shows the distribution between temperature and humidity for all reading collected in the database
- Other Map - desc
