import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def cMeans_reduce_and_plot(data,name):
    # Extract features and cluster assignments
    features = data.iloc[:, :-1].values
    cluster_labels = data.iloc[:, -1].values

    # Apply PCA for dimensionality reduction to 2 dimensions
    pca = PCA(n_components=2)
    reduced_features = pca.fit_transform(features)

    # Plot the reduced data with color-coded clusters
    plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=cluster_labels, cmap='viridis')
    plt.title(name)
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.show()

