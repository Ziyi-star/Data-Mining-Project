import pandas as pd
import csv
from sklearn.cluster import KMeans
import numpy as np

"""
n_cluster: Anzahl der Cluster Zentrum
init = kmeans++, selects initial cluster centroids using sampling based on an empirical probability distribution of the points’ contribution to the overall inertia.
n_init= Several runs are recommended for sparse high-dimensional problems

"""

def clustering_cmeans(csv_data, cluster_number):
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_data, skiprows=1)
    print(data)
    for seed in range(5):

        kmeans = KMeans(n_clusters=cluster_number, init='k-means++', n_init=5, max_iter=300, random_state=seed)

        # Fit the model to the data
        kmeans.fit(data)

        cluster_ids, cluster_sizes = np.unique(kmeans.labels_, return_counts=True)
        print(f"Number of elements asigned to each cluster: {cluster_sizes}")

    #perform KMeans

    #calculate the size of every cluster, print
