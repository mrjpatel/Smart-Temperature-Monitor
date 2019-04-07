from kdePlot import KDEPlot
from database import Database


class Analytics:
    kdeFileName = "kdePlot.png"
    histogramFileName = "histogram.png"

    def __init__(self):
        pass

    def drawkdePlot(self):
        print("Drawing KDE Plot...")
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

    def drawPlots(self):
        print("Drawing Plots...")
        self.drawkdePlot()
        self.drawHistogram()


def main():
    analytics = Analytics()
    analytics.drawPlots()

if __name__ == '__main__':
    main()
