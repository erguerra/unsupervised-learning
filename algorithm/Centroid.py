import numpy as np
import pandas as pd

from algorithm.Distances import euclidean_distance


class Centroid:
    def __init__(self, instance):
        self.centroid = instance
        self.neighbors = []
        self.avg_v = 0.0

    def update_centroid(self):
        neighbors = pd.DataFrame(self.neighbors)
        for column in neighbors.columns:
            self.centroid[column] = neighbors[column].mean()

    # def update_centroid(self):
    #     for column in self.centroid.columns:
    #         column_mean = 0.0
    #         for i in self.neighbors:
    #             column_mean += i[column]
    #         self.centroid[column] = column_mean/len(self.neighbors)

    def update_avg_v(self):
        distance = 0.0
        for i in range(len(self.neighbors)):
            distance += (euclidean_distance(self.centroid, self.neighbors[i]) ** 2)
        self.avg_v = round(distance, 3)

    def clean_neighbors(self):
        self.neighbors = []

    def get_neighbors_df(self):
        return pd.DataFrame(self.neighbors)
