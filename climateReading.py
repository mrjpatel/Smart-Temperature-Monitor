from sense_hat import SenseHat
import datetime


class ClimateReading:
    def __init__(self, current_date_time, temperature, humidity):
        self.current_date_time = current_date_time
        self.temperature = temperature
        self.humidity = humidity

    @classmethod
    def from_sensehat(cls, sense):
        date_time = datetime.datetime.now()
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        return cls(date_time, temperature, humidity)

    def outside_config_range(self, range):
        if self.temperature < range.min_temperature:
            return "Temp: {}*C, {}*C Below the minimum temperature".format(
                round(self.temperature, 1),
                round((range.min_temperature - self.temperature), 1))
        if self.temperature > range.max_temperature:
            return "Temp: {}*C, {} *C Above the maximum temperature".format(
                round(self.temperature, 1),
                round((self.temperature - range.max_temperature), 1))
        if self.humidity < range.min_humidity:
            return "Humidity: {}%, {}% Below the minimum humidity".format(
                round(self.humidity, 1),
                round((range.min_humidity - self.humidity), 1))
        if self.humidity > range.max_humidity:
            return "Humidity: {}%, {}% Above the maximum humidity".format(
                round(self.humidity, 1),
                round((self.humidity - range.max_humidity), 1))
        return ""

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
