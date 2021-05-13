# unsupervised-learning

## Running the code
In order to execute this program you must have a configured python environment with numpy and pandas.
Then, you can simply execute the main.py file.

## Expected Results
By default the uncommented code in the main.py file executes the KMeans algorithm using 3 clusters and Euclidean Distance given the MusicAndMovies dataset.
After the execution you should find the clusters persisted inside the data/results folder.

## Elbow Method
In order to execute the elbow method, you can uncomment the indicated code sinpped. The result of the method execution is persisted at the results folder with the "elbow" prefix.
Remember that the algorithm is not working correctly for categorical arguments.
