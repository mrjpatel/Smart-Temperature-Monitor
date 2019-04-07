from kdePlot import KDEPlot
from database import Database


class Analytics:
    kdeFileName = "kdePlot.png"
    histogramFileName = "histogram.png"

    def __init__(self):
        # TODO get DB Data
        self.data_set = Database.getAllSenseHatData

    def drawkdePlot(self):
        print(*self.data_set)
        print("Drawing KDE Plot...")
        KDEPlot.plot_and_save(
            self.data_set['temperature'],
            self.data_set['humidity'],
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
