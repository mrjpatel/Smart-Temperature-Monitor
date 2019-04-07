from kdePlot import KDEPlot
from database import Database


class Analytics:
    kdeFileName = "heatmap.png"
    histogramFileName = "histogram.png"

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
            self.kdeFileName
        )
        print("Saved Plot as: {}".format(self.kdeFileName))

    def drawHistogram(self):
        print("Drawing Histogram...")

        print("Saved Histogram as: {}".format(self.histogramFileName))
        pass

    def draw_plots(self):
        print("Drawing Plots...")
        self.draw_heatmap()
        self.drawHistogram()


def main():
    analytics = Analytics()
    analytics.draw_plots()

if __name__ == '__main__':
    main()
