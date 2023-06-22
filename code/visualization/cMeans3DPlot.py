import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def cMeans_reduce_and_plot_3D(data,name):
    # Extract features and cluster assignments
    features = data.iloc[:, :-1].values
    cluster_labels = data.iloc[:, -1].values

    # Apply PCA for dimensionality reduction to 3 dimensions
    pca = PCA(n_components=3)
    reduced_features = pca.fit_transform(features)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter(reduced_features[:, 0], reduced_features[:, 1], reduced_features[:, 2], c=cluster_labels)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.title(name)
    plt.show()