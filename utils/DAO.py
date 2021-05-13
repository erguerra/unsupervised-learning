import pandas as pd


class DAO:
    def __init__(self, input_file, delimiter):
        self.input_file = input_file
        self.delimiter = delimiter
        self.dataset = self.read_data()

    def read_data(self):
        df = pd.read_csv(self.input_file, delimiter=self.delimiter)
        df.drop('id', axis='columns', inplace=True)
        return df

    def persist_clusters(self, cluster_list, output_file):
        for i in range(len(cluster_list)):
            cluster_list[i].to_csv(f'{output_file}{i+1}.csv', sep=self.delimiter)

    def persist_cluster(self, cluster, output_file):
        cluster.to_csv(f'{output_file}.csv', sep=self.delimiter)

    def persist_data(self, series, output_file):
        series = pd.Series(series)
        series.to_csv(f'{output_file}.csv', sep=self.delimiter)
