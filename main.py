from algorithm.Distances import Distances
from algorithm.KMeans import KMeans
from utils.DAO import DAO


def main():

    k_mean_euclidean = KMeans(12, Distances.EUCLIDEAN)
    k_mean_hamming = KMeans(10, Distances.HAMMING)

    hobbies_and_interests = DAO('data/HobbiesAndInterests_Vars.tsv', delimiter='\t')
    # sociodemographic = DAO('data/SocioDemographic_Vars.tsv', delimiter='\t')

    gl = k_mean_euclidean.execute(hobbies_and_interests.dataset)
    hobbies_and_interests.persist_clusters(gl, 'data/results/Hobbies')
    # gl = k_mean_hamming.execute(sociodemographic.dataset)
    # sociodemographic.persist_clusters(gl, 'data/results/SocioDemographic_Vars')



if __name__ == '__main__':
    main()
