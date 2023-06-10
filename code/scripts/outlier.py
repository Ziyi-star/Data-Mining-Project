import pandas as pd
import numpy as np
import csv

def find_replace_outlier(csv_data, new_stan_file_path):
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_data)

    # find and replace outliers
    # Calculate the mean and standard deviation of the data
    mean = data.mean()
    std = data.std()

    # Define the threshold for determining outliers
    threshold = 2

    # Identify outliers above the mean
    outliers_above = data[data > mean + threshold * std]
    # Replace outliers above the mean with mean + 2 * std
    data.update(outliers_above, value=mean + 2 * std)

    # Identify outliers below the mean
    outliers_below = data[data < mean - threshold * std]
    # Replace outliers below the mean with mean - 2 * std
    data.update(outliers_below, value=mean - 2 * std)

    # Open the CSV file in write mode
    with open(new_stan_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)






# Save the modified DataFrame to a new CSV file
data.to_csv('modified_file.csv', index=False)