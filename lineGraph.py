import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import DayLocator


class LineGraph:
    @staticmethod
    def plot_and_save(time_data, temp_data_set, hum_data_set, file_name):
        converted_dates = []
        for timestamp in time_data:
            converted_dates.append(datetime.datetime.strptime(
                timestamp, '%Y-%m-%d %H:%M:%S.%f'))
        fig, ax = plt.subplots()
        formatter = dates.DateFormatter('%Y-%m-%d')
        plt.plot_date(converted_dates, temp_data_set, 'b-')
        ax.xaxis.set_major_locator(DayLocator())
        ax.xaxis.set_major_formatter(formatter)
        ax.autoscale_view()
        plt.gcf().autofmt_xdate()
        ax.set_title('Temparture Trend comparison')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.savefig(file_name)
