import subprocess as sp
import os
import re
import bluetooth
import time
from climateReading import ClimateReading
from readingRanges import ReadingRanges
from pushBullet import PushBullet


class Bluetooth_notify:
    @staticmethod
    def run(config_file, push_token):
        while True:
            if(Bluetooth_notify.notify_about_weather(config_file, push_token)):
                print("Sent notification. Sleeping 10 minutes...")
                time.sleep(600)
            else:
                print("Not Notified. Sleeping 10 seconds...")
                time.sleep(10)

    @staticmethod
    def notify_about_weather(config_file, push_token):
        paired_list = Bluetooth_notify.get_paired_list()

        connected_device = Bluetooth_notify.is_in_range(paired_list)
        if(connected_device != ""):
            ReadingRanges.update_defaults_from_json(config_file)
            reading = ClimateReading.from_sensehat()
            if(reading.outside_config_range(ReadingRanges) == ""):
                PushBullet.loadToken(push_token)
                PushBullet.notify(
                    "Device {} is in range. ".format(connected_device) +
                    "Current Temp is {}, ".format(reading.temperature) +
                    "Humidity is {}".format(reading.humidity)
                )
                return True
            print("Outside Config Ranges")
            return False
        print("Not Found Paired Device")
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
        print("Paired: ")
        print(*paired_list, sep=", ")
        return paired_list

    @staticmethod
    def is_in_range(paired_list):
        print("Scanning...")
        nearby_devices = bluetooth.discover_devices()
        for macAddress in nearbyDevices:
            print("Found device with mac-address: " + macAddress)
        print("Nearby: ")
        print(*nearby_devices, sep=", ")

        for macAddress in nearby_devices:
            if macAddress in paired_list:
                print("Found paired device with mac-address: " + macAddress)
                return macAddress
        return ""

Bluetooth_notify.run("config.json", "accessToken.json")
