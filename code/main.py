from datasets.convertData import json_to_csv
from pathlib import Path

def json_all_file_to_csv():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    json_dir_1 = project_dir/'data'/'data'/'18_2_17_8_15_19_20_17_4_18'
    json_dir = project_dir/'data'/'data'
    csv_dir_1 = project_dir/'data'/'data'/'csv'/'18_2_17'
    csv_dir = project_dir/'data'/'data'/'csv'

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


if __name__ =='__main__':

    json_all_file_to_csv()