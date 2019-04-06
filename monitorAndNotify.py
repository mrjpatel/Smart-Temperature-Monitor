from readingRanges import ReadingRanges
from climateReading import ClimateReading
from pushBullet import PushBullet
from database import Database


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

        Database.logTempHumData(
                                current_reading.current_date_time,
                                round(current_reading.temperature, 1),
                                round(current_reading.max_humidity, 1)
                                )

        error = current_reading.outside_config_range(ReadingRanges)
        if error != "":
            print("Outside Configured Ranages!")
            print("Error: {}".format(error))
            if not Database.hasNotified(current_reading.current_date_time):
                PushBullet.notify(error)
                Database.logNotificationData(
                    current_reading.current_date_time)

PushBullet.loadToken("accessToken.json")
monitorAndNotify = MonitorAndNotify("config.json")
monitorAndNotify.run()
