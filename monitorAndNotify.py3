import json
import datetime
from sense_hat import SenseHat

class ReadingRanges:
    default_min_temperature = 15
    default_max_temperature = 25
    default_min_humidity = 45
    default_max_humidity = 55

    def __init__(self, min_temperature, max_temperature, min_humidity, max_humidity):
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
            cls(data["min_temperature"], data["max_temperature"], data["min_humidity"], data["max_humidity"])

    @staticmethod
    def validate_range_json(data):
        if 'min_temperature' in data and 'max_temperature' in data and 'min_humidity' in data and 'max_humidity' in data:
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
    
    def write_to_db(self, dbinfo):
        pass

sense = SenseHat()
ReadingRanges.update_defualts_from_json("config.json")
current_reading = ClimateReading.from_sensehat(sense)
current_reading.write_to_db("some_info")
#Push notification command