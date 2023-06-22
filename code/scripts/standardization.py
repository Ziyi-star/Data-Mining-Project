import pandas as pd
from sklearn.preprocessing import StandardScaler
import csv


def standardization(csv_data, new_stan_file_path):

    data = pd.read_csv(csv_data, encoding = "utf-8", header=None)
    # Standardize the features
    scaler = StandardScaler()
    standardizedData = scaler.fit_transform(data)

    # Open the CSV file in write mode
    with open(new_stan_file_path, 'w', newline='') as file:
        writer = csv.writer(file)

        # add headers
        # Assuming you have a DataFrame called 'df' containing your data
        num_attributes = len(data.columns)
        # Generate default headers
        headers = ['Attribut ' + str(i + 1) for i in range(num_attributes)]
        # Assign headers to the DataFrame
        data.columns = headers
        writer.writerow(headers)
        # Write data to the CSV file

        for row in standardizedData:
            writer.writerow(row)





