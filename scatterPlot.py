import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import DayLocator


class ScatterPlot:
    @staticmethod
    def plot_and_save(time_data, temp_data_set, file_name):
        matplotlib.pyplot.switch_backend('Agg')
        converted_dates = []
        for timestamp in time_data:
            converted_dates.append(datetime.datetime.strptime(
                timestamp, '%Y-%m-%d %H:%M:%S.%f'))
        fig, ax = plt.subplots()
        formatter = dates.DateFormatter('%Y-%m-%d')
        formatter2 = dates.DateFormatter('%H:%M')
        plt.plot_date(converted_dates, temp_data_set)
        ax.xaxis.set_major_locator(DayLocator())
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_minor_locator(dates.HourLocator(interval=6))
        ax.xaxis.set_minor_formatter(formatter2)
        ax.autoscale_view()
        plt.gcf().autofmt_xdate()
        ax.set_title('Temparture vs Time')
        plt.xlabel('Time')
        plt.ylabel('Temperature (C)')
        plt.savefig(file_name)
