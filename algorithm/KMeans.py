import copy

import numpy as np
import pandas as pd

from algorithm.Distances import Distances

MAX_ITERATIONS = 100
MIN_EUCLIDEAN_CENTROID_DISTANCE = 0.01


# def get_average_variance():
#     big_v = 0.0
#     for i in range(len())
#
#
# def mount_dataframes(centroids_neighbors, dataset):
#     group_list = []
#     for i in range(len(centroids_neighbors)):
#         group = []
#         for n in centroids_neighbors[i]:
#             group.append(dataset.iloc[n])
#         group = pd.DataFrame(group)
#         group_list.append(group)
#     return group_list
#
#
# def should_stop_by_convergence(distance, k, old_centroids, new_centroids):
#     diff = []
#     for i in range(k):
#         diff.append(compare_centroids(old_centroids[i], new_centroids[i], distance))
#     dist = sum(diff)
#     if distance == Distances.EUCLIDEAN:
#         return dist <= MIN_EUCLIDEAN_CENTROID_DISTANCE * len(old_centroids[1])
#     elif distance == Distances.HAMMING:
#         return dist == 0
#
#
# def compare_centroids(old_centroid, new_centroid, distance):
#     if distance == Distances.EUCLIDEAN:
#         return euclidean_distance(old_centroid, new_centroid)
#     elif distance == Distances.HAMMING:
#         return hamming_distance(old_centroid, new_centroid)
#
#
# def initialize_centroids(k, dataset):
#     new_dataset = copy.deepcopy(dataset)
#     centroids = []
#     centroids_neighbors = []
#     for i in range(k):
#         centroids.append(new_dataset.sample())
#         centroids_neighbors.append([])
#     return centroids, centroids_neighbors
#
#
# def update_centroid_categorical(centroid, neighbors_indices, dataset):
#     for column in centroid.columns:
#         column_values = []
#         for n in neighbors_indices:
#             column_values.append(dataset.iloc[n][column])
#         centroid[column] = max(set(column_values), key=column_values.count)
#
#     return centroid
#
#
# def update_centroid_numerical(centroid, neighbors_indices, dataset):
#     for column in centroid.columns:
#         summ = 0
#         for n in neighbors_indices:
#             summ += dataset.iloc[n][column]
#         centroid[column] = round((summ / len(neighbors_indices)), 4)
#     return centroid
#
#
# def update_centroid(centroid, neighbors_indices, dataset, distance):
#     if len(neighbors_indices) == 0:
#         return centroid
#     if distance == Distances.EUCLIDEAN:
#         centroid = update_centroid_numerical(centroid, neighbors_indices, dataset)
#     elif distance == Distances.HAMMING:
#         centroid = update_centroid_categorical(centroid, neighbors_indices, dataset)
#     return centroid
#
#
# def find_closest_centroid_index(centroid_list, instance, distance):
#     if distance == Distances.EUCLIDEAN:
#         distances = []
#         for i in centroid_list:
#             distances.append(euclidean_distance(i, instance))
#         return distances.index(min(distances))
#     elif distance == Distances.HAMMING:
#         distances = []
#         for i in centroid_list:
#             distances.append(hamming_distance(i, instance))
#         return distances.index(min(distances))
#
#
# def euclidean_distance(centroid, instance):
#     centroid = np.squeeze(centroid.to_numpy())
#     instance = np.squeeze(instance.to_numpy())
#     summation = 0.0
#     for i in range(len(centroid)):
#         summation += np.square(centroid[i] - instance[i])
#
#     return np.sqrt(summation)
#
#
# def hamming_distance(centroid, instance):
#     distance = 0
#     centroid = centroid.squeeze().to_list()
#     instance = instance.squeeze().to_list()
#
#     for i in range(len(centroid)):
#         if centroid[i] != instance[i]:
#             distance += 1
#     return distance
#
#
# class KMeans:
#     def __init__(self, k, distance):
#         self.k = k
#         self.distance = distance
#
#     def set_distance(self, distance):
#         self.distance = distance
#
#     def set_k(self, k):
#         self.k = k
#
#     def execute(self, dataset):
#         group_list = []
#         centroids, centroids_neighbors = initialize_centroids(self.k, dataset)
#
#         should_repeat = True
#         max_iterations = MAX_ITERATIONS
#         while should_repeat:
#             print(f'Starting {max_iterations} iteration')
#             max_iterations -= 1
#             for i in range(len(dataset)):
#                 closest_centroid = find_closest_centroid_index(centroid_list=centroids, instance=dataset.iloc[i],
#                                                                distance=self.distance)
#                 centroids_neighbors[closest_centroid].append(i)
#
#             old_centroids = copy.deepcopy(centroids)
#             for i in range(len(centroids)):
#                 centroids[i] = update_centroid(centroids[i], centroids_neighbors[i], dataset, self.distance)
#
#             group_list = mount_dataframes(centroids_neighbors, dataset)
#
#             average_variance = get_average_variance(group_list)
#
#             print(average_variance)
#
#             if should_stop_by_convergence(self.distance, self.k, old_centroids=old_centroids,
#                                           new_centroids=centroids) or max_iterations == 0:
#                 should_repeat = False
#
#         return group_list
