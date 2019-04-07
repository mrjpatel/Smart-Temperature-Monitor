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
            print(item)
            temp = item
            print(temp)
            temps.insert(temp)
        for item in list_humidities:
            humiditiy, blank = item
            humidities.insert(humidity)

        print("Temps:")
        print(*list_temps)
        print("Humidities:")
        print(*list_humidities)

        KDEPlot.plot_and_save(
            temps,
            humidities,
            self.kdeFileName
        )
        print("Saved Plot as: {}".format(self.kdeFileName))

    def drawHistogram(self):
        print("Drawing Histogram...")

        print("Saved Histogram as: {}".format(histogramFileName))
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
