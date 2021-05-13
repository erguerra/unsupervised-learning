from algorithm.Distances import Distances
from algorithm.KMeans2 import KMeans2
from utils.DAO import DAO


def main():
    # k_mean_euclidean = KMeans(3, Distances.EUCLIDEAN)
    # k_mean_hamming = KMeans(8, Distances.HAMMING)
    #
    # hobbies_and_interests = DAO('data/HobbiesAndInterests_Vars.tsv', delimiter='\t')
    # sociodemographic = DAO('data/SocioDemographic_Vars.tsv', delimiter='\t')
    #
    # gl = k_mean_euclidean.execute(hobbies_and_interests.dataset)
    # hobbies_and_interests.persist_clusters(gl, 'data/results/Hobbies')
    # gl = k_mean_hamming.execute(sociodemographic.dataset)
    # sociodemographic.persist_clusters(gl, 'data/results/SocioDemographic_Vars')

    hobbies_and_interests = DAO('data/HobbiesAndInterests_Vars.tsv', delimiter='\t')
    k_mean_euclidean = KMeans2(8)
    gl = k_mean_euclidean.execute(hobbies_and_interests.dataset)

    for i in range(len(gl)):
        hobbies_and_interests.persist_cluster(gl[i].get_neighbors_df(), f'data/results/Hobbies{i+1}')


if __name__ == '__main__':
    main()
