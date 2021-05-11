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

        for i in centroids:
            print(i)
