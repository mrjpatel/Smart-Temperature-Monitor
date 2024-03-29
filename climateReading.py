from sense_hat import SenseHat
import datetime
import os

"""
This class is to encapsulate the climate reading object.
Provides methods to gather from sense hat and check the data against
config ranges
"""


class ClimateReading:
    """
    Init function to allow to create a new reading for use by the reporting
    """
    def __init__(self, current_date_time, temperature, humidity):
        self.current_date_time = current_date_time
        self.temperature = round(temperature, 2)
        self.humidity = round(humidity, 2)

    """
    Alt constructor to create instance from sense hat data
    """
    @classmethod
    def from_sensehat(cls):
        sense = SenseHat()
        date_time = datetime.datetime.now()
        sense_temp = sense.get_temperature()
        cpu_temp = ClimateReading.get_cpu_temp()
        humidity = sense.get_humidity()
        calculated_temp = sense_temp - (
            (cpu_temp - sense_temp)/0.5923)

        return cls(date_time, calculated_temp, humidity)

    """
    This method is to check if the reading is outside the ranges specifed
    Returns error string if it is outside configured ranges
    """
    def outside_config_range(self, range):
        rstr = ""
        if self.temperature < range.min_temperature:
            rstr += "Temp: {}*C, {}*C Below the minimum temperature. ".format(
                round(self.temperature, 1),
                round((range.min_temperature - self.temperature), 1))
        if self.temperature > range.max_temperature:
            rstr += "Temp: {}*C, {}*C Above the maximum temperature. ".format(
                round(self.temperature, 1),
                round((self.temperature - range.max_temperature), 1))
        if self.humidity < range.min_humidity:
            rstr += "Humidity: {}%, {}% Below the minimum humidity. ".format(
                round(self.humidity, 1),
                round((range.min_humidity - self.humidity), 1))
        if self.humidity > range.max_humidity:
            rstr += "Humidity: {}%, {}% Above the maximum humidity. ".format(
                round(self.humidity, 1),
                round((self.humidity - range.max_humidity), 1))
        return rstr

    """
    Static method to get the cpu temp
    """
    @staticmethod
    def get_cpu_temp():
        res = os.popen("vcgencmd measure_temp").readline()
        t = float(res.replace("temp=", "").replace("'C\n", ""))
        return(t)
