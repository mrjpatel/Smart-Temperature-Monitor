import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import MONDAY, RRuleLocator, rrulewrapper, WeekdayLocator, DayLocator


class LineGraph:
    @staticmethod
    def plot_and_save(time_data, temp_data_set, hum_data_set, file_name):
        converted_dates = list(map(datetime.datetime.strptime, time_data, len(time_data)*['%Y-%m-%d']))
        # rule = rrulewrapper(MO, TU, WE, TH, FR, SA, SU, byeaster=1, interval=1)
        # loc = WeekdayLocator(byweekday=MO,TU, WE, TH, FR, SA, SU, tz=tz)
        mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
        alldays = DayLocator()              	# minor ticks on the days
        x_axis = converted_dates
        formatter = dates.DateFormatter('%Y-%m-%d')
        fig, ax = plt.subplots()
        plt.scatter(x_axis, temp_data_set)
        ax.xaxis.set_major_locator(alldays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(formatter)
        ax.autoscale_view()
        plt.gcf().autofmt_xdate(rotation=25)
        ax.set_title('Temparture comparision for')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.savefig(file_name)
