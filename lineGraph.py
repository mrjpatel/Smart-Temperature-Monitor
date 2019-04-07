import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import YEARLY, RRuleLocator, rrulewrapper


class LineGraph:
    @staticmethod
    def plot_and_save(time_data, temp_data_set, hum_data_set, file_name):
        converted_dates = list(map(datetime.datetime.strptime, time_data, len(time_data)*['%Y-%m-%d']))
        rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
        loc = RRuleLocator(rule)
        x_axis = converted_dates
        formatter = dates.DateFormatter('%Y-%m-%d')
        fig, ax = plt.subplots()
        plt.plot(x_axis, temp_data_set, '-')
        ax.xaxis.set_major_locator(loc)
        plt.gcf().autofmt_xdate(rotation=25)
        ax.set_title('Volume and percent change')
        plt.xlabel('Humidity')
        plt.ylabel('Temperature')
        plt.savefig(file_name)
