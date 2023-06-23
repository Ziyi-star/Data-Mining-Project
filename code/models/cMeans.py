import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



"""
n_cluster: Anzahl der Cluster Zentrum
init = kmeans++, selects initial cluster centroids using sampling based on an empirical probability distribution of the points’ contribution to the overall inertia.
n_init= Several runs are recommended for sparse high-dimensional problems

"""

def clustering_cmeans(csv_data, cluster_number, clustering_dir_path):
    # Load the CSV file into a pandas DataFrame, skipping the header row
    print('cluster number'+ str(cluster_number))
    data = pd.read_csv(csv_data, encoding="utf-8")
    for seed in range(5):
        kmeans = KMeans(n_clusters=cluster_number, init='k-means++', n_init=5, max_iter=300, random_state=seed)
        kmeans.fit(data)

        cluster_ids, cluster_sizes = np.unique(kmeans.labels_, return_counts=True)
        #print(f"Number of elements assigned to each cluster: {cluster_sizes}")
        predict = kmeans.predict(data)

        data['Predict'] = pd.Series(predict, index=data.index)

        new_data_path = clustering_dir_path / (csv_data.stem + '__' + str(seed) + '.csv')
        data.to_csv(new_data_path, index=None, sep=',', mode='w+')

        # Calculate Silhouette coefficients
        silhouette_avg = silhouette_score(data, predict)
        print(f"Silhouette coefficient for seed {seed}: {silhouette_avg}")

    #perform KMeans

    #calculate the size of every cluster, print

def clustering_evaluation(csv_data, max):
    data = pd.read_csv(csv_data, encoding="utf-8")
    silhouette_list = []
    davies_bouldin_list = []

    for c in range(3, max):
        kMeans = KMeans(n_clusters=c, init='k-means++', n_init=5, max_iter=300, random_state=0)
        kMeans.fit(data)

        predict = kMeans.predict(data)
        silhouette_avg = silhouette_score(data, predict)
        silhouette_list.append(silhouette_avg)
        davies_bouldin_avg = davies_bouldin_score(data, predict)
        davies_bouldin_list.append(davies_bouldin_avg)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

    ax1.plot(range(3, max), silhouette_list, marker='o', linestyle='-', color='blue')
    ax1.set_xlabel('Number of Clusters')
    ax1.set_ylabel('Silhouette Score')
    ax1.set_title(csv_data.stem + 'Silhouette Score vs. Number of Clusters')
    ax1.grid(True)
    ax1.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # Set x-axis tick labels as integers

    ax2.plot(range(3, max), davies_bouldin_list, marker='o', linestyle='-', color='red')
    ax2.set_xlabel('Number of Clusters')
    ax2.set_ylabel('Davies-Bouldin Index')
    ax2.set_title('Davies-Bouldin Index vs. Number of Clusters')
    ax2.grid(True)
    ax2.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # Set x-axis tick labels as integers

    plt.subplots_adjust(hspace=0.4)

    plt.show()

