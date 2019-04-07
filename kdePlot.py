import seaborn as sns
import matplotlib.pyplot as plt

"""
This class is to plot the KDE Plot
"""


class KDEPlot:
    """
    This method plots the kde plot as a heat map and saves it
    Params: x data, y data and output file name
    """
    @staticmethod
    def plot_and_save(x_data_set, y_data_set, output_file_name):
        graph = sns.kdeplot(x_data_set, y_data_set, shade=True, legend=True)
        figure = graph.get_figure()
        plt.xlabel('Temperature')
        plt.ylabel('Humidity')
        figure.savefig(output_file_name, dpi=400)
