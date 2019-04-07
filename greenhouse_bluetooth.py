import subprocess as sp
import os
import re
import bluetooth
import time
from climateReading import ClimateReading
from readingRanges import ReadingRanges
from pushBullet import PushBullet

"""
This file is for the bluetooth notify funtionality
It run untill exited scanning devices in range.
If devices found is same as the paired devices,
it will send a notificaiton via PushBullet
"""


class Bluetooth_notify:
    """
    This run function will start the program
    Params: config file name and push notificaiton token file name
    It will sleep for 10 mins if it sends a notification or take a 10 second
    pause between scans
    """
    @staticmethod
    def run(config_file, push_token):
        while True:
            if(Bluetooth_notify.notify_about_weather(config_file, push_token)):
                print("Sent notification. Sleeping 10 minutes...")
                time.sleep(600)
            else:
                print("Not Notified. Sleeping 10 seconds...")
                time.sleep(10)

    """
    This method does the orchastration between the other static methods and
    sends the notification via PushBullet
    """
    @staticmethod
    def notify_about_weather(config_file, push_token):
        paired_list = Bluetooth_notify.get_paired_list()

        connected_device = Bluetooth_notify.is_in_range(paired_list)
        if(connected_device != ""):
            ReadingRanges.update_defaults_from_json(config_file)
            reading = ClimateReading.from_sensehat()
            error = reading.outside_config_range(ReadingRanges)
            PushBullet.load_token(push_token)
            PushBullet.notify(
                "Device {} is in range. ".format(connected_device) +
                "Current Temp is {}, ".format(reading.temperature) +
                "Humidity is {}. ".format(reading.humidity) +
                error
            )
            return True
        print("Not Found Paired Device")
        return False

    """
    This method returns a list of paired devices
    """
    @staticmethod
    def get_paired_list():
        p = sp.Popen(
            ["bt-device", "--list"],
            stdin=sp.PIPE,
            stdout=sp.PIPE,
            close_fds=True
        )
        (stdout, stdin) = (p.stdout, p.stdin)
        data = stdout.readlines()

        paired_list = []
        for d in data:
            paired_list.append(re.sub('^.*\((.*?)\)[^\(]*$', '\g<1>', str(d)))

        paired_list.pop(0)
        return paired_list

    """
    This method checks if the paried device is within range
    Params: list of paired devices
    """
    @staticmethod
    def is_in_range(paired_list):
        print("Scanning...")
        nearby_devices = bluetooth.discover_devices()

        for macAddress in nearby_devices:
            if macAddress in paired_list:
                print("Found paired device with mac-address: " + macAddress)
                return macAddress
        return ""

"""
Main method executed at run of this file
"""


def main():
    Bluetooth_notify.run("config.json", "accessToken.json")

if __name__ == '__main__':
    main()
