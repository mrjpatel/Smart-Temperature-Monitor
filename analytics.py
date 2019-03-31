from kdePlot import KDEPlot
from database import Database


class Analytics:
    kdeFileName = "kdePlot.png"
    histogramFileName = "histogram.png"

    def __init__(self):
        # TODO get DB Data
        self.data_set = data_set

    def drawkdePlot(self):
        print("Drawing KDE Plot...")
        KDEPlot.plot_and_save(
            data_set['temperature'],
            data_set['humidity'],
            kdeFileName
        )
        print("Saved Plot as: {}".format(kdeFileName))
        pass

    def drawHistogram(self):
        print("Drawing Histogram...")

        print("Saved Histogram as: {}".format(histogramFileName))
        pass

    def drawPlots(self):
        print("Drawing Plots...")
        self.drawkdePlot()
        self.drawHistogram()

analytics = Analytics()
analytics.drawPlots()
