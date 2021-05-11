from algorithm.Distances import Distances
from algorithm.KMeans import KMeans
from utils.DAO import DAO


def main():

    k_mean_euclidean = KMeans(3, Distances.EUCLIDEAN)
    k_mean_hamming = KMeans(3, Distances.HAMMING)

    hobbies_and_interests = DAO('data/HobbiesAndInterests_Vars.tsv', delimiter='\t')
    sociodemographic = DAO('data/SocioDemographic_Vars.tsv', delimiter='\t')
    # hobbies_and_interests = DAO('data/HobbiesAndInterests_Vars.tsv', delimiter='\t')
    # hobbies_and_interests = DAO('data/HobbiesAndInterests_Vars.tsv', delimiter='\t')
    # hobbies_and_interests = DAO('data/HobbiesAndInterests_Vars.tsv', delimiter='\t')

    k_mean_euclidean.execute(sociodemographic.dataset)


if __name__ == '__main__':
    main()
