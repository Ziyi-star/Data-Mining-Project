import pandas as pd
import numpy as np

def find_replace_outlier(csv_data, new_stan_file_path):
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_data, encoding="utf-8")

    # find and replace outliers
    # Calculate the mean and standard deviation of the data
    mean = np.mean(data)
    std = np.std(data)
    # Define the threshold for determining outliers
    threshold = 2

    # Identify outliers above the mean
    outliers_above = data[data > mean + threshold * std]
    # Replace outliers above the mean with mean + 2 * std
    data[outliers_above.columns] = np.where(data[outliers_above.columns] > mean + 2 * std, mean + 2 * std, data[outliers_above.columns])

    # Identify outliers below the mean
    outliers_below = data[data < mean - threshold * std]
    # Replace outliers below the mean with mean - 2 * std
    data[outliers_below.columns] = np.where(data[outliers_below.columns] < mean - 2 * std, mean - 2 * std, data[outliers_below.columns])

    data.to_csv(new_stan_file_path, index=None, sep=',', mode='w+')

