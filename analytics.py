from database import Database
from lineGraph import LineGraph


class Analytics:
    heatmap_file_name = "heatmap.png"
    histogram_file_name = "histogram.png"

    def __init__(self):
        pass

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

    def drawHistogram(self):
        print("Drawing Histogram...")
        list_timestamp = Database.get_all_timestamp_data()
        list_temps = Database.get_all_temperature_data()
        list_humidities = Database.get_all_humidity_data()
        timestamp = []
        temps = []
        humidities = []

        for item in list_timestamp:
            timestamp.append(Database.get_date_from_timestamp(
                Database.get_local_time(item[0])))
        for item in list_temps:
            temps.extend(list(item))
        for item in list_humidities:
            humidities.extend(list(item))

        LineGraph.plot_and_save(
            timestamp,
            temps,
            humidities,
            self.histogram_file_name
        )
        print("Saved Histogram as: {}".format(self.histogram_file_name))
        pass

    def draw_plots(self):
        print("Drawing Plots...")
        # self.draw_heatmap()
        self.drawHistogram()


def main():
    analytics = Analytics()
    analytics.draw_plots()

if __name__ == '__main__':
    main()
