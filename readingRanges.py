import json


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
            validate_range_json(data)
            cls.min_temperature = data["min_temperature"]
            cls.max_temperature = data["max_temperature"]
            cls.min_humidity = data["min_humidity"]
            cls.max_humidity = data["max_humidity"]
            print('Updated defaults: ' + cls.min_temperature + ',' + cls.max_temperature + ',' + cls.min_humidity + ',' + cls.max_humidity)

    @classmethod
    def from_json(cls, jsonFilePath):
        with open(jsonFilePath) as json_file:
            data = json.load(json_file)
            validate_range_json(data)
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
