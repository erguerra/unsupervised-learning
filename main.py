from algorithm.Distances import Distances
from algorithm.ElbowMethod import ElbowMethod
from algorithm.KMeans import KMeans
from utils.DAO import DAO


def main():
    #Elbow method for music and movies dataset
    # music = DAO('data/MusicAndMovies_Vars.tsv', delimiter='\t')
    # elbow = ElbowMethod(list(range(1, 13)), dataset=music.dataset, distance=Distances.EUCLIDEAN)
    # result = elbow.execute()
    # music.persist_data(result, 'data/results/elbow_music')

    # Elbow method for Sociodemographic dataset NOT WORKING
    # music = DAO('data/SocioDemographic_Vars.tsv', delimiter='\t')
    # elbow = ElbowMethod(list(range(1, 13)), dataset=music.dataset, distance=Distances.HAMMING)
    # result = elbow.execute()
    # music.persist_data(result, 'data/results/elbow_socio')

    # Execution for MusicAndMovies dataset using euclidean distance and Three clusters

    k_mean_euclidean = KMeans(3, Distances.EUCLIDEAN)
    hobbies_and_interests = DAO('data/MusicAndMovies_Vars.tsv', delimiter='\t')
    print(hobbies_and_interests.dataset.head(10))
    gl = k_mean_euclidean.execute(hobbies_and_interests.dataset)
    hobbies_and_interests.persist_clusters(gl, 'data/results/music')

    # k_mean_hamming = KMeans(3, Distances.HAMMING)
    # socio = DAO('data/SocioDemographic_Vars.tsv', delimiter='\t')
    # print(socio.dataset.head(10))
    # gl = k_mean_hamming.execute(socio.dataset)
    # socio.persist_clusters(gl, 'data/results/socio')



if __name__ == '__main__':
    main()
