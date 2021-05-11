import numpy as np

def find_closest_centroid_index(centroid_list, instance):
    pass


def euclidean_distance(centroid, series):
    c = np.squeeze(centroid.to_numpy())
    s = np.squeeze(series.to_numpy())
    summation = 0.0
    for i in range(len(centroid)):
        summation += np.square(c[i] - s[i])

    return np.sqrt(summation)


def hamming_distance(centroid, series):
    distance = 0
    c = centroid.squeeze().to_list()
    s = series.squeeze().to_list()
    for i in range(len(c)):
        if c[i] != s[i]:
            distance += 1
    return distance


class KMeans:
    def __init__(self, k, distance):
        self.k = k
        self.distance = distance

    def set_distance(self, distance):
        self.distance = distance

    def set_k(self, k):
        self.k = k

    def execute(self, dataset):
        centroids = []
        for i in range(self.k):
            centroids.append(dataset.sample())

        for i in range(len(dataset)):
            pass
