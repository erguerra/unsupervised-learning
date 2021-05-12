import copy

import numpy as np
import pandas as pd

from algorithm.Distances import Distances


def initialize_centroids(k, dataset):
    centroids = []
    centroids_neighbors = []
    for i in range(k):
        centroids.append(dataset.sample())
        centroids_neighbors.append([])
    return centroids, centroids_neighbors


def update_centroid_categorical(centroid, neighbors_indices, dataset):
    for column in centroid.columns:
        column_values = []
        for n in neighbors_indices:
            column_values.append(dataset.iloc[n][column])
        centroid[column] = max(set(column_values), key=column_values.count)

    return centroid


def update_centroid_numerical(centroid, neighbors_indices, dataset):
    for column in centroid.columns:
        summ = 0
        for n in neighbors_indices:
            summ += dataset.iloc[n][column]
        centroid[column] = summ / len(neighbors_indices)

    return centroid


def update_centroid(centroid, neighbors_indices, dataset, distance):
    if len(neighbors_indices) == 0:
        return centroid
    if distance == Distances.EUCLIDEAN:
        centroid = update_centroid_numerical(centroid, neighbors_indices, dataset)
    elif distance == Distances.HAMMING:
        centroid = update_centroid_categorical(centroid, neighbors_indices, dataset)
    return centroid


def find_closest_centroid_index(centroid_list, instance, distance):
    if distance == Distances.EUCLIDEAN:
        distances = []
        for i in centroid_list:
            distances.append(euclidean_distance(i, instance))
        return distances.index(min(distances))
    elif distance == Distances.HAMMING:
        distances = []
        for i in centroid_list:
            distances.append(hamming_distance(i, instance))
        return distances.index(min(distances))


def euclidean_distance(centroid, instance):
    centroid = np.squeeze(centroid.to_numpy())
    instance = np.squeeze(instance.to_numpy())
    summation = 0.0
    for i in range(len(centroid)):
        summation += np.square(centroid[i] - instance[i])

    return np.sqrt(summation)


def hamming_distance(centroid, instance):
    distance = 0
    centroid = centroid.squeeze().to_list()
    instance = instance.squeeze().to_list()

    for i in range(len(centroid)):
        if centroid[i] != instance[i]:
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
        group_list = []
        centroids, centroids_neighbors = initialize_centroids(self.k, dataset)

        should_repeat = True
        while should_repeat:
            for i in range(len(dataset)):
                closest_centroid = find_closest_centroid_index(centroid_list=centroids, instance=dataset.iloc[i],
                                                               distance=self.distance)
                centroids_neighbors[closest_centroid].append(i)

            old_centroids = copy.deepcopy(centroids)
            diff_list = []

            for i in range(len(centroids)):
                centroids[i] = update_centroid(centroids[i], centroids_neighbors[i], dataset, self.distance)
                diff_list.append(hamming_distance(centroids[i], old_centroids[i]))

            if sum(diff_list) > 0:
                should_repeat = False

            if not should_repeat:
                for i in range(self.k):
                    group = []
                    for n in centroids_neighbors[i]:
                        group.append(dataset.iloc[n])
                    group = pd.DataFrame(group)
                    group_list.append(group)

        return group_list
