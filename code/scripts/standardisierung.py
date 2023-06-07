import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import csv


def standisierung(csv_data, new_standardzialsierung_data_path):
    # Load the data
    data = pd.read_csv(csv_data)
    # Standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(data)
    print(X)

    # CSV-Datei öffnen
    with open(new_standardzialsierung_data_path, 'w', newline='') as csv_file:
        writer = csv.writer(new_standardzialsierung_data_path)

        # Daten aus JSON in CSV schreiben
        for item in data:
            writer.writerow(X)



