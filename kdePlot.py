import seaborn as sns


class KDEPlot:
    @staticmethod
    def plot_and_save(x_data_set, y_data_set, output_file_name):
        graph = sns.kdeplot(x_data_set, y_data_set, shade=True, legend=True)
        figure = graph.get_figure()
        figure.savefig(output_file_name, dpi=400)
