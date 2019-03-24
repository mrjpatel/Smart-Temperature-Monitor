from readingRanges import ReadingRanges
from climateReading import ClimateReading
from pushBullet import PushBullet


# TODO DB class details can go in a seperate py file
# as analytics needs to use the same info.
# Adds reuseability. Just need to import the module

class MonitorAndNotify:
    def __init__(self, range_config):
        self.range_config = range_config

    def run(self):
        print("Default: MinTemp: {} MaxTemp: {} MinHum: {} MaxHum: {}".format(
            ReadingRanges.min_temperature,
            ReadingRanges.max_temperature,
            ReadingRanges.min_humidity,
            ReadingRanges.max_humidity))

        ReadingRanges.update_defaults_from_json(self.range_config)
        current_reading = ClimateReading.from_sensehat()

        print("MinTemp: {} MaxTemp: {} MinHum: {} MaxHum: {}".format(
            ReadingRanges.min_temperature,
            ReadingRanges.max_temperature,
            ReadingRanges.min_humidity,
            ReadingRanges.max_humidity))

        # TODO Change based on DB implementation
        # This goes for all the db function calls
        current_reading.write_to_db("db_info")
        error = current_reading.outside_config_range(ReadingRanges)
        if error != "":
            print("Outside Configured Ranages!")
            print("Error: {}".format(error))
            if not current_reading.notified_pushbullet_today("db_info"):
                PushBullet.notify(error)
                current_reading.update_notify_today_status("db_info")

PushBullet.loadToken("accessToken.json")
monitorAndNotify = MonitorAndNotify("config.json")
monitorAndNotify.run()
