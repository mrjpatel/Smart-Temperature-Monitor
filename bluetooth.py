import subprocess as sp
import os
import re
import bluetooth
import time
import ClimateReading from climateReading
import ReadingRanges from readingRanges
import PushBullet from pushBullet


class Bluetooth:
    @staticmethod
    def run(config_file, push_token):
        while True:
            if(Bluetooth.notify_about_weather(config_file, push_token)):
                print("Sent notification. Sleeping 10 minutes...")
                time.sleep(600)
            else:
                print("Not Notified. Sleeping 10 seconds...")
                time.sleep(10)
    
    @staticmethod
    def notify_about_weather(config_file, push_token):
        paired_list = Bluetooth.get_paired_list()

        connected_device = Bluetooth.is_in_range(paired_list)
        if(connected_device != ""):
            ReadingRanges.update_defaults_from_json(config_file)
            reading = ClimateReading.from_sensehat()
            if(reading.outside_config_range(ReadingRanges) == ""):
                PushBullet.loadToken(push_token)
                PushBullet.notify(
                    "Device {} is in range.".format(connected_device) +
                    "Current Temp is {}, ".format(reading.temperature) +
                    "Humidity is {}".format(reading.humidity)
                )
                return True
        return False

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
        return paired_list

    @staticmethod
    def is_in_range(paired_list):
        print("Scanning...")
        nearbyDevices = bluetooth.discover_devices()
        for macAddress in nearbyDevices:
            if macAddress in paired_list:
                print("Found device with mac-address: " + macAddress)
                return macAddress
        return ""

Bluetooth.run("config.json", "accessToken.json")
