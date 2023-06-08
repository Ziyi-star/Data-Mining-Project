import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import csv


def standardization(csv_data, new_stan_file_path):
    # Load the data
    data = pd.read_csv(csv_data)
    # Standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(data)

    # CSV-Datei öffnen
    with open(new_stan_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(new_stan_file_path)

        # Daten aus JSON in CSV schreiben
        for item in data:
            writer.writerow(X)



