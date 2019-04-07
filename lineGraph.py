import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class LineGraph:
    @staticmethod
    def plot_and_save(time_data, temp_data_set, hum_data_set, file_name):

        fig, ax = plt.subplots()
        ax.plot(time_data, temp_data_set, label="temperature")
        ax.plot(time_data, hum_data_set, label="humidity")
        ax.legend()
        plt.xlabel('Time')
        plt.ylabel('Number')
        plt.savefig(file_name)
