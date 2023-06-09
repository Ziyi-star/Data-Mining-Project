import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def accumulate(var_ration):
    acc = 0
    r = np.empty(len(var_ration))
    for idx, value in enumerate(var_ration):
        acc += value
        r[idx] = acc
    return r

def pca(df, name):
    cov = df.cov(numeric_only=True)
    cov_num = cov.apply(pd.to_numeric, errors='coerce')
    eigenvalues = np.linalg.eigvals(cov_num)
    explained_var_ratio = eigenvalues / np.sum(eigenvalues)
    acc = accumulate(explained_var_ratio)

    #plot the diagramm
    plt.bar(range(0, len(explained_var_ratio)), explained_var_ratio, alpha=0.5,
            align='center', label='Individual explained variance')
    plt.step(range(0, len(acc)), acc, where='mid',
             label='Cumulative explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal component index')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.title(name)
    plt.show()