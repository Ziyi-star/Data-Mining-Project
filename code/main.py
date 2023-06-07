from datasets.convertData import json_to_csv
from scripts.standardisierung import standisierung
from pathlib import Path
from utils.paths import *

def json_all_file_to_csv():
    json_dir_1 = get_json_path_1()
    json_dir = get_json_path()
    csv_dir_1 = get_csv_path_1()
    csv_dir = get_csv_path()

    for json_file_path in json_dir_1.glob('*.json'):
        # Construct the output CSV file path
        csv_file_path = csv_dir_1 / (json_file_path.stem + '.csv')

        # Convert JSON to CSV
        json_to_csv(json_file_path, csv_file_path)

    for json_file_path in json_dir.glob('*.json'):
        # Construct the output CSV file path
        csv_file_path = csv_dir / (json_file_path.stem + '.csv')

        # Convert JSON to CSV
        json_to_csv(json_file_path, csv_file_path)

def standarisierung_for_all():
    csv_dir_1 = get_csv_path_1()
    csv_dir = get_csv_path()
    stan_dir_1 = get_stan_path_1()
    stan_dir = get_stan_path()

    for csv_file_path in csv_dir_1.glob('*.*'):
        # Construct the output CSV file path
        print(csv_file_path)
        stan_file_path = stan_dir_1 / (csv_file_path.stem + '.csv')
        standisierung(csv_file_path, stan_file_path)

    for csv_file_path in csv_dir.glob('*.*'):
        # Construct the output CSV file path
        stan_file_path = stan_dir / (csv_file_path.stem + '.csv')
        standisierung(csv_file_path, stan_file_path)

if __name__ =='__main__':

    json_all_file_to_csv()

    standarisierung_for_all()
