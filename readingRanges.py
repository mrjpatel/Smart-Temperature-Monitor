import json

"""
This class is for the reading ranges.
"""


class ReadingRanges:
    min_temperature = 20
    max_temperature = 30
    min_humidity = 50
    max_humidity = 60

    """
    Method to create custom instance
    """
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

    """
    This method updates the ranges from a json file
    Params: file path for json file
    """
    @classmethod
    def update_defaults_from_json(cls, json_file_path):
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            ReadingRanges.validate_range_json(data)
            cls.min_temperature = data["min_temperature"]
            cls.max_temperature = data["max_temperature"]
            cls.min_humidity = data["min_humidity"]
            cls.max_humidity = data["max_humidity"]
        print("Updated Defaults from {}".format(json_file_path))

    """
    This creates a ranges instance from a json file
    Params: file path for json file
    """
    @classmethod
    def from_json(cls, json_file_path):
        with open(jsonFilePath) as json_file:
            data = json.load(json_file)
            ReadingRanges.validate_range_json(data)
            cls(
                data["min_temperature"],
                data["max_temperature"],
                data["min_humidity"],
                data["max_humidity"]
            )

    """
    This method validates the json object
    """
    @staticmethod
    def validate_range_json(data):
        if 'min_temperature' in data and \
           'max_temperature' in data and \
           'min_humidity' in data and \
           'max_humidity' in data:
            return True
        raise Exception('JSON Range file is not valid!')
