from database import Database
from readingRanges import ReadingRanges
from climateReading import ClimateReading
import csv


class CreateReport:

    """
    Controls the data given from databse to the segregated list
    and passes it to generate csv
    """
    def generate_report(self, range_config_file, report_file_name):
        ReadingRanges.update_defaults_from_json(range_config_file)
        print("Generating " + report_file_name + " file ...")
        temp_hum_data_list = self.get_database_data()
        report_list = self.get_all_status(temp_hum_data_list)
        self.generate_csv_file(report_file_name, report_list)
        print("Successfully generated: " + report_file_name)

    """
    Gets data from database and segregates them into same days list
    """
    def get_database_data(self):
        rows = Database.get_all_sensehat_data()
        currentDate = ''
        allDays = []
        day = []
        for row in rows:
            if currentDate == Database.get_date_from_timestamp(
               Database.get_local_time(row[0])):
                day.append(row)
            else:
                currentDate = Database.get_date_from_timestamp(
                    Database.get_local_time(row[0]))
                allDays.append(day)
                day = []
                day.append(row)
        allDays.append(day)
        print(*allDays)
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

            date = Database.get_date_from_timestamp(date)
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
        min_error = ""
        max_error = ""
        if len(temp) > 0 and len(humidity) > 0:
            temp_max_value = max(temp)
            temp_min_value = min(temp)
            hum_max_value = max(humidity)
            hum_min_value = min(humidity)
            min_reading = ClimateReading(date, temp_min_value, hum_min_value)
            min_error = min_reading.outside_config_range(range)

            if (temp_max_value != temp_min_value or
                    hum_min_value != hum_max_value):
                max_reading = ClimateReading(
                    date, temp_max_value, hum_max_value)
                max_error = max_reading.outside_config_range(range)

        if max_error.startswith("Temp") and min_error.startswith("Hum"):
            error = (max_error + min_error).strip()
        else:
            error = (min_error + max_error).strip()

        if error != "":
            return "BAD: " + error
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


def main():
    range_config_file = "config.json"
    report_file = "report.csv"
    report = CreateReport()
    report.generate_report(range_config_file, report_file)

if __name__ == '__main__':
    main()
