import json
import datetime
from sense_hat import SenseHat
import readingRanges
import climateReading


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
