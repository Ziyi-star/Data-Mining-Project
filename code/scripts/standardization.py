import pandas as pd
from sklearn.preprocessing import StandardScaler
import csv


def standardization(csv_data, new_stan_file_path):

    data = pd.read_csv(csv_data)
    # Standardize the features
    scaler = StandardScaler()
    standardizedData = scaler.fit_transform(data)

    # Open the CSV file in write mode
    with open(new_stan_file_path, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write data to the CSV file
        for row in standardizedData:
            writer.writerow(row)





