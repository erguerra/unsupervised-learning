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

    def persist_data(self, dataset, output_file):
        dataset.to_csv(output_file, sep=self.delimiter)
