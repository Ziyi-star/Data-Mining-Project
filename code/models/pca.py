import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


def pca(df, name):
    # Perform PCA
    pca = PCA()
    pca.fit(df)
    # Get the explained variance ratio and the cumulative sums of the eigenvalues
    explained_variance_ratio = pca.explained_variance_ratio_
    cumulative_sums = np.cumsum(pca.explained_variance_)
    # Plot the results
    plt.plot(explained_variance_ratio, marker='o')
    plt.plot(cumulative_sums / cumulative_sums[-1], marker='o')
    plt.xlabel('Number of Components')
    plt.ylabel('Explained Variance Ratio / Cumulative Sum')
    plt.legend(['Explained Variance Ratio', 'Cumulative Sum'])
    plt.title(name)
    plt.show()





