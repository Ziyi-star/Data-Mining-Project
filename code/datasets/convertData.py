import json
import csv
from pathlib import Path
import pandas as pd


def json_to_csv(json_data, csv_path):
    # JSON-Daten laden
    with open(json_data, 'r') as json_file:
        data = json.load(json_file)

    # CSV-Datei öffnen
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Daten aus JSON in CSV schreiben
        for item in data:
            writer.writerow(item)


def convert_row_to_columns(input_file, output_file):
    # Transpose the data to convert rows into columns
    transposed_data = input_file.transpose()
    # Write transposed data to the output CSV file
    transposed_data.to_csv(output_file, index=False, header=False)


def merge_labels_with_data(pathData, pathLabel, data_csv_all_dir):
    # Read data from the first CSV file
    df1 = pd.read_csv(pathData)

    # Read data from the second CSV file
    df2 = pd.read_csv(pathLabel)

    # Merge the two DataFrames based on a common column
    #merged_df = pd.merge(df1, df2, on='label')
    merged_df = pd.concat([df1,df2],axis=1)
####
    saveName = pathData.stem
    merged_filename = Path.joinpath(data_csv_all_dir, saveName)
    # Write merged data to the generated CSV file
    merged_df.to_csv(merged_filename, index=False)