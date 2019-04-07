from kdePlot import KDEPlot
from database import Database
from scatterPlot import ScatterPlot


class Analytics:
    heatmap_file_name = "heatmap.png"
    scatter_plot_file_name = "scatterplot.png"

    def __init__(self):
        pass

    """
    Draws the heatmap
    """
    def draw_heatmap(self):
        print("Drawing HeatMap...")
        list_temps = Database.get_all_temperature_data()
        list_humidities = Database.get_all_humidity_data()
        temps = []
        humidities = []

        for item in list_temps:
            temps.extend(list(item))
        for item in list_humidities:
            humidities.extend(list(item))

        KDEPlot.plot_and_save(
            temps,
            humidities,
            self.heatmap_file_name
        )
        print("Saved Plot as: {}".format(self.heatmap_file_name))

    """
    Draws scatter plot
    """
    def draw_scatter_plot(self):
        print("Drawing Scatter Plot...")
        list_timestamp = Database.get_all_timestamp_data()
        list_temps = Database.get_all_temperature_data()
        timestamp = []
        temps = []

        for item in list_timestamp:
            timestamp.append(Database.get_local_time(item[0]))
        for item in list_temps:
            temps.extend(list(item))

        ScatterPlot.plot_and_save(
            timestamp,
            temps,
            self.scatter_plot_file_name
        )
        print("Saved Scatter Plot as: {}".format(self.scatter_plot_file_name))

    """
    excutes plot drawing functions
    """
    def draw_plots(self):
        print("Drawing Plots...")
        self.draw_heatmap()
        self.draw_scatter_plot()


def main():
    analytics = Analytics()
    analytics.draw_plots()

if __name__ == '__main__':
    main()
