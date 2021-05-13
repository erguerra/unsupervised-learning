from enum import Enum

import numpy as np


class Distances(Enum):
    EUCLIDEAN = 1
    MANHATTAN = 2
    HAMMING = 3


def euclidean_distance(first_instance, second_instance):
    first_instance = np.squeeze(first_instance.to_numpy())
    second_instance = np.squeeze(second_instance.to_numpy())
    summation = 0.0
    for i in range(len(first_instance)):
        summation += np.square(first_instance[i] - second_instance[i])

    return np.sqrt(summation)


def hamming_distance(first_instance, second_instance):
    distance = 0
    centroid = first_instance.squeeze().to_list()
    instance = second_instance.squeeze().to_list()

    for i in range(len(centroid)):
        if centroid[i] != instance[i]:
            distance += 1
    return distance
