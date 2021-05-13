import copy

import numpy as np

from algorithm.Centroid import Centroid
from algorithm.Distances import Distances, euclidean_distance, hamming_distance

MAX_ITERATIONS = 100
MIN_EUCLIDEAN_CENTROID_DISTANCE = 0.01


def get_mean_wss(centroid_list):
    wss = []
    for c in centroid_list:
        wss.append(c.total_wss)
    return round(sum(wss) / len(centroid_list), 3)


def initialize_centroids(k, dataset):
    new_dataset = copy.deepcopy(dataset)
    centroids = []
    for i in range(k):
        centroids.append(new_dataset.sample())
    return centroids


def find_closest_centroid_index(centroid_list, instance, distance):
    if distance == Distances.EUCLIDEAN:
        distances = []
        for i in centroid_list:
            distances.append(euclidean_distance(i.centroid, instance))
        return distances.index(min(distances))
    elif distance == Distances.HAMMING:
        distances = []
        for i in centroid_list:
            distances.append(hamming_distance(i.centroid, instance))
        return distances.index(min(distances))


class KMeans:
    def __init__(self, k, distance):
        self.k = k
        self.distance = distance
        self.avg_total_wss = 0.0

    def set_distance(self, distance):
        self.distance = distance

    def set_k(self, k):
        self.k = k

    def execute(self, dataset):
        group_list = []

        centroids = initialize_centroids(self.k, dataset)

        for i in range(self.k):
            centroids[i] = Centroid(centroids[i])

        should_repeat = True
        max_iterations = MAX_ITERATIONS

        while should_repeat:
            print(f'Starting {max_iterations} iteration')
            max_iterations -= 1
            for i in range(len(dataset)):
                instance = dataset.iloc[i]
                closest_centroid = find_closest_centroid_index(centroid_list=centroids, instance=instance,
                                                               distance=self.distance)
                centroids[closest_centroid].neighbors.append(instance)

            for i in range(len(centroids)):
                centroids[i].update_centroid(self.distance)
                centroids[i].update_wss(self.distance)

            new_avg = get_mean_wss(copy.deepcopy(centroids))

            if max_iterations == 0 or new_avg == self.avg_total_wss:
                for i in centroids:
                    group_list.append(i.get_neighbors_df())
                should_repeat = False

            self.avg_total_wss = new_avg

            for i in range(len(centroids)):
                centroids[i].clean_neighbors()

        return group_list
