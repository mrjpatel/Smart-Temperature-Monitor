import json
import datetime
from sense_hat import SenseHat


class ReadingRanges:
    default_min_temperature = 15
    default_max_temperature = 25
    default_min_humidity = 45
    default_max_humidity = 55

    def __init__(
            self,
            min_temperature,
            max_temperature,
            min_humidity,
            max_humidity
    ):
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity

    @classmethod
    def update_defualts_from_json(cls, jsonFilePath):
        with open(jsonFilePath) as json_file:
            data = json.load(json_file)
            cls.min_temperature = data["min_temperature"]
            cls.max_temperature = data["max_temperature"]
            cls.min_humidity = data["min_humidity"]
            cls.max_humidity = data["max_humidity"]

    @classmethod
    def from_json(cls, jsonFilePath):
        with open(jsonFilePath) as json_file:
            data = json.load(json_file)
            cls(
                data["min_temperature"],
                data["max_temperature"],
                data["min_humidity"],
                data["max_humidity"]
            )

    @staticmethod
    def validate_range_json(data):
        if 'min_temperature' in data and \
           'max_temperature' in data and \
           'min_humidity' in data and \
           'max_humidity' in data:
            return True
        raise Exception('JSON Range file is not valid!')


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

# TODO DB class details can go in a seperate py file
# as analytics needs to use the same info.
# Adds reuseability. Just need to import the module

sense = SenseHat()
ReadingRanges.update_defualts_from_json("config.json")
current_reading = ClimateReading.from_sensehat(sense)

# TODO Change based on DB implementation
# This goes for all the db function calls
current_reading.write_to_db("db_info")

if current_reading.outside_config_range(ReadingRanges):
    if not current_reading.notified_pushbullet_today("db_info"):
        current_reading.notify_pushbullet()
        current_reading.update_notify_today_status("db_info")
