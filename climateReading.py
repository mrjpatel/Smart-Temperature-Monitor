from sense_hat import SenseHat
import datetime
import os


class ClimateReading:
    def __init__(self, current_date_time, temperature, humidity):
        self.current_date_time = current_date_time
        self.temperature = temperature
        self.humidity = humidity

    @classmethod
    def from_sensehat(cls):
        sense = SenseHat()
        date_time = datetime.datetime.now()
        sense_temp = sense.get_temperature()
        cpu_temp = ClimateReading.get_cpu_temp()
        humidity = sense.get_humidity()
        calculated_temp = sense_temperature - (
            (cpu_temp - sense_temperature)/0.5923)

        return cls(date_time, calculated_temp, humidity)

    def outside_config_range(self, range):
        rstr = ""
        if self.temperature < range.min_temperature:
            rstr += "Temp: {}*C, {}*C Below the minimum temperature. ".format(
                round(self.temperature, 1),
                round((range.min_temperature - self.temperature), 1))
        if self.temperature > range.max_temperature:
            rstr += "Temp: {}*C, {} *C Above the maximum temperature. ".format(
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

    # TODO Japan to write, change params to suit db setup.
    # Create class to store DB info and push/qury logic?
    def write_to_db(self, dbinfo):
        print('Time: {}'.format(self.current_date_time))
        print('Temp: {}'.format(self.temperature))
        print('Humidity: {}'.format(self.humidity))

    # TODO Japan to write, change params to suit db setup.
    # Create table to keep track of this.
    def notified_pushbullet_today(self, dbinfo):
        return False

    # TODO Japan to write, change params to suit db setup.
    def update_notify_today_status(self, dbinfo):
        pass

    @staticmethod
    def get_cpu_temp():
        res = os.popen("vcgencmd measure_temp").readline()
        t = float(res.replace("temp=", "").replace("'C\n", ""))
        return(t)
