from kdePlot import KDEPlot
from database import Database


class Analytics:
    kdeFileName = "kdePlot.png"
    histogramFileName = "histogram.png"

    def __init__(self):
        pass

    def drawkdePlot(self):
        temps = Database.get_all_temperature_data()
        humidities = Database.get_all_humidity_data()
        print(*temps)
        print(*humidities)
        print("Drawing KDE Plot...")
        KDEPlot.plot_and_save(
            temps,
            humidities,
            kdeFileName
        )
        print("Saved Plot as: {}".format(kdeFileName))

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
