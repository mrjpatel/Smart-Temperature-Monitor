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
        cls(date_time, temperature, humidity)

    def outside_config_range(self, range):
        if self.temperature < range.min_temperature or \
           self.temperature > range.max_temperature or \
           self.humidity < range.min_humidity or \
           self.humidity > range.max_humidity:
            return True
        return False

    # TODO Russell to write logic. Will need to change params once looked into
    def notify_pushbullet(self):
        pass

    # TODO Japan to write, change params to suit db setup.
    # Create class to store DB info and push/qury logic?
    def write_to_db(self, dbinfo):
        pass

    # TODO Japan to write, change params to suit db setup.
    # Create table to keep track of this.
    def notified_pushbullet_today(self, dbinfo):
        return False

    # TODO Japan to write, change params to suit db setup.
    def update_notify_today_status(self, dbinfo):
        pass
        