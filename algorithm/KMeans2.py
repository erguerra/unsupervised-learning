import copy

from algorithm.Centroid import Centroid
from algorithm.Distances import euclidean_distance

MAX_ITERATIONS = 50
MIN_VARIANCE_IMPROVEMENT = 0.001


def initialize_centroids(k, dataset):
    new_dataset = copy.deepcopy(dataset)
    centroids = []
    for i in range(k):
        centroids.append(Centroid(new_dataset.sample().squeeze()))
    return centroids


def find_closest_centroid_index(centroid_list, instance):
    distances = []
    for i in centroid_list:
        distances.append(euclidean_distance(i.centroid, instance))
    return distances.index(min(distances))


class KMeans2:
    def __init__(self, k):
        self.k = k

    def set_k(self, k):
        self.k = k

    def execute(self, dataset):
        centroids = initialize_centroids(self.k, dataset)
        should_repeat = True
        max_iterations = MAX_ITERATIONS

        while should_repeat:
            print(f'Starting {max_iterations} iteration')
            for c in centroids:
                c.clean_neighbors()

            for i in range(len(dataset)):
                instance = copy.deepcopy(dataset.iloc[i])
                closest_centroid = find_closest_centroid_index(centroid_list=centroids, instance=instance)
                centroids[closest_centroid].neighbors.append(copy.deepcopy(instance))

            for centroid in centroids:
                centroid.update_centroid()
                centroid.update_avg_v()



            total_variance = sum(c.avg_v for c in centroids) / len(centroids)

            # print(f'new variance {total_variance}')

            max_iterations -= 1
            '''abs(total_variance - old_total_variance) < MIN_VARIANCE_IMPROVEMENT or'''
            if max_iterations == 0:
                return centroids

