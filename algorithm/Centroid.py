import numpy as np
import pandas as pd

from algorithm.Distances import euclidean_distance, hamming_distance, Distances


class Centroid:
    def __init__(self, instance):
        self.centroid = instance
        self.neighbors = []
        self.total_wss = 0.0

    def update_centroid(self, distance):
        if distance == Distances.EUCLIDEAN:
            self.update_centroid_euclidean()
        elif distance == Distances.HAMMING:
            self.update_centroid_hamming()

    def update_centroid_hamming(self):
        neighbors = pd.DataFrame(self.neighbors)
        for column in neighbors.columns:
            self.centroid[column] = neighbors[column].value_counts().idxmax()

    def update_centroid_euclidean(self):
        neighbors = pd.DataFrame(self.neighbors)
        for column in neighbors.columns:
            self.centroid[column] = neighbors[column].mean()

    def update_wss(self, distance):
        if distance == Distances.EUCLIDEAN:
            self.update_wss_euclidean()
        elif distance == Distances.HAMMING:
            self.update_wss_hamming()

    def update_wss_euclidean(self):
        distance = 0.0
        for i in range(len(self.neighbors)):
            distance += (euclidean_distance(self.centroid, self.neighbors[i]) ** 2)
        self.total_wss = round(distance, 3)

    def update_wss_hamming(self):
        distance = 0
        for i in range(len(self.neighbors)):
            distance += (hamming_distance(self.centroid, self.neighbors[i]) ** 2)
        self.total_wss = round(distance, 3)

    def clean_neighbors(self):
        self.neighbors = []

    def get_neighbors_df(self):
        return pd.DataFrame(self.neighbors)
