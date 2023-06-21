import pandas as pd
import csv

def chooseAttribut(csv_data, new_stan_file_path):
    data = pd.read_csv(csv_data)

    attribut_selected = data[['Attribut 1','Attribut 2','Attribut 4','Attribut 5','Attribut 6','Attribut 10','Attribut 11','Attribut 16','Attribut 20','Attribut 21','Attribut 23','Attribut 24']]

    # Open the CSV file in write mode
    with open(new_stan_file_path, 'w', newline='') as file:
        writer = csv.writer(file)

        for row in attribut_selected:
            writer.writerow(row)

