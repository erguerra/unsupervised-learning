import copy

from algorithm.KMeans import KMeans


class ElbowMethod:
    def __init__(self, list_of_k, dataset, distance):
        self.list_of_k = list_of_k
        self.dataset = copy.deepcopy(dataset)
        self.distance = distance

    def execute(self):
        results = {}
        for i in self.list_of_k:
            k_means = KMeans(i, self.distance)
            k_means.execute(copy.deepcopy(self.dataset))
            results[i] = k_means.avg_total_wss

        return results
