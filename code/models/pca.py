import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


def pca(df, name):
    # Get the attribute names
    attribute_names = df.columns.tolist()

    # Perform PCA
    pca = PCA( )
    pca.fit(df)
    # Get the explained variance ratio and the cumulative sums of the eigenvalues
    explained_variance_ratio = pca.explained_variance_ratio_
    cumulative_sums = np.cumsum(pca.explained_variance_)

    # Get the attribute names in the order of the PCs
    sorted_indices = np.argsort(np.abs(pca.components_[0]))
    sorted_attribute_names = [attribute_names[i] for i in sorted_indices]

    # Plot the results
    plt.plot(explained_variance_ratio, marker='o')
    plt.plot(cumulative_sums / cumulative_sums[-1], marker='o')
    plt.xlabel('Number of Components')
    plt.ylabel('Explained Variance Ratio / Cumulative Sum')
    plt.legend(['Explained Variance Ratio', 'Cumulative Sum'])
    plt.axhline(y=0.85, color='r', linestyle='-')
    plt.title(name)
    # Set the x-ticks with attribute names for each principal component
    #plt.xticks(range(len(attribute_names)), attribute_names, rotation=45, ha='right')

    # Show attribute names for each principal component
    for i, (x, y) in enumerate(zip(range(len(sorted_attribute_names)), explained_variance_ratio)):
        plt.text(x, y, sorted_attribute_names[i], rotation=90, ha='center', va='bottom')

    plt.show()







