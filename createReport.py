from database import Database
from readingRanges import ReadingRanges
from climateReading import ClimateReading
import csv


class CreateReport:
    def __init__(self, range_config):
        self.range_config = range_config
        ReadingRanges.update_defaults_from_json(self.range_config)

    """
    Gets data from database and segregates them into same days list
    """
    def get_database_data(self):
        rows = Database.getAllSenseHatData()
        currentDate = ''
        allDays = []
        day = []
        for row in rows:
            if currentDate == Database.getDateFromTimestamp(
               Database.getLocalTime(row[0])):
                day.append(row)
            else:
                currentDate = Database.getDateFromTimestamp(
                    Database.getLocalTime(row[0]))
                allDays.append(day)
                day = []
                day.append(row)
        allDays.append(day)
        return allDays

    """
    Returns a list of days with status of the day
    """
    def get_all_status(self, allData):
        csvlist = []
        for data in allData:
            temp = []
            humidity = []
            date = " "
            for dayData in data:
                date = dayData[0]
                temp.append(dayData[1])
                humidity.append(dayData[2])

            date = Database.getDateFromTimestamp(date)
            status = self.generate_day_status(
                date, temp, humidity, ReadingRanges)
            if len(date) > 0:
                full_day_status = []
                full_day_status.append(date)
                full_day_status.append(status)
                csvlist.append(full_day_status)
            temp = []
            humidity = []
        return csvlist

    """
    Geneartes status for a single day
    """
    def generate_day_status(self, date, temp, humidity, range):
        min_error = " "
        max_error = " "
        if len(temp) > 0 and len(humidity) > 0:
            temp_max_value = max(temp)
            temp_min_value = min(temp)
            hum_max_value = max(humidity)
            hum_min_value = min(humidity)
            min_reading = ClimateReading(date, temp_min_value, hum_min_value)
            min_error = min_reading.outside_config_range(range)
            if min_error.startswith("Temp") or min_error.startswith("Hum"):
                min_error = "BAD: " + min_error

            max_reading = ClimateReading(date, temp_max_value, hum_max_value)
            max_error = max_reading.outside_config_range(range)
            if max_error.startswith("Temp") or max_error.startswith("Hum"):
                max_error = "BAD: " + max_error

        if min_error.startswith("BAD"):
            error = min_error + max_error.split("BAD: ", 1)[1]
        else:
            error = min_error + max_error
        if error.startswith("BAD"):
            return error
        else:
            return "OK"

    """
    Genetaes a csv file for the given data
    """
    def generate_csv_file(self, name, data):
        with open(name, mode='w', newline='') as csv_file:
            fieldnames = ['Date', 'Status']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for d in data:
                writer.writerow({'Date': d[0], 'Status': str(d[1])})

    def generate_report(self, report_file_name):
        print("Generating " + report_file_name + " file ...")
        temp_hum_data_list = self.get_database_data()
        report_list = self.get_all_status(temp_hum_data_list)
        self.generate_csv_file("report.csv", report_list)
        print("Successfully generated: " + report_file_name)


def main():
    report = CreateReport("config.json")
    report.generate_report("report.csv")

if __name__ == '__main__':
    main()
