import subprocess as sp
import os
import re
import bluetooth
import time


class Bluetooth:
    @staticmethod
    def notify_about_weather():
        pass

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
                return True
        return False
