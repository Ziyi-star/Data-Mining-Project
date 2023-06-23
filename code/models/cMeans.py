import pandas as pd
import csv
from sklearn.cluster import KMeans
import numpy as np

"""
n_cluster: Anzahl der Cluster Zentrum
init = kmeans++, selects initial cluster centroids using sampling based on an empirical probability distribution of the points’ contribution to the overall inertia.
n_init= Several runs are recommended for sparse high-dimensional problems

"""

def clustering_cmeans(csv_data, cluster_number, clustering_dir_path):
    # Load the CSV file into a pandas DataFrame, skipping the header row
    data = pd.read_csv(csv_data, encoding="utf-8")


    for seed in range(5):
        kmeans = KMeans(n_clusters=cluster_number, init='k-means++', n_init=5, max_iter=300, random_state=seed)
        kmeans.fit(data)

        cluster_ids, cluster_sizes = np.unique(kmeans.labels_, return_counts=True)
        print(f"Number of elements assigned to each cluster: {cluster_sizes}")
        predict = kmeans.predict(data)

        data['Predict'] = pd.Series(predict, index=data.index)

        new_data_path = clustering_dir_path / (csv_data.stem + '__' + str(seed) + '.csv')
        data.to_csv(new_data_path, index=None, sep=',', mode='w+')

    #perform KMeans

    #calculate the size of every cluster, print
