from datasets.convertData import json_to_csv
from scripts.standardization import standardization
from utils.paths import *


def json_all_file_to_csv():
    # current_dir = Path.cwd()
    # # print(current_dir)
    # project_dir = current_dir.parent
    # # print(project_dir)
    # # 'data' / 'data' / '18_2_17_8_15_19_20_17_4_18'
    # json_dir_1 = project_dir / 'data' / 'data' / '18_2_17_8_15_19_20_17_4_18'
    # # / 'data' / 'data'
    # json_dir = project_dir / 'data' / 'data'
    # # / 'data' / 'data' / 'csv' / '18_2_17'
    # csv_dir_1 = project_dir / 'data' / 'data' / 'csv' / '18_2_17'
    # # / 'data' / 'data' / 'csv'
    # csv_dir = project_dir / 'data' / 'data' / 'csv'

    json_dir_1 = get_json_path_1()
    json_dir = get_json_path()
    csv_dir_1 = get_csv_path_1()
    csv_dir = get_csv_path()

    # 'data' / 'data' / '18_2_17_8_15_19_20_17_4_18'

    for json_file_path in json_dir_1.glob('*.json'):
        # Construct the output CSV file path
        # .stem attribute is used to get the filename stem (without the extension), which is then used to construct the output CSV file path.
        csv_file_path = csv_dir_1 / (json_file_path.stem + '.csv')
        # Convert JSON to CSV
        json_to_csv(json_file_path, csv_file_path)

    # / 'data' / 'data'
    for json_file_path in json_dir.glob('*.json'):
        # Construct the output CSV file path
        csv_file_path = csv_dir / (json_file_path.stem + '.csv')

        # Convert JSON to CSV
        json_to_csv(json_file_path, csv_file_path)


def standardization_for_all():
    # / 'data' / 'data' / 'csv' / '18_2_17'
    csv_dir_1 = get_csv_path_1()
    # / 'data' / 'data' / 'csv'
    csv_dir = get_csv_path()
    # / 'data' / 'data' / 'standardization' / '18_2_17'
    stan_dir_1 = get_stan_path_1()
    # / 'data' / 'data' / 'standardization'
    stan_dir = get_stan_path()

    # Construct the output CSV file path in / 'data' / 'data' / 'standardization' / '18_2_17'
    for csv_file_path in csv_dir_1.glob('*.csv'):
        new_stan_file_path = stan_dir_1 / (csv_file_path.stem + '.csv')
        # Call the standardization function
        standardization(csv_file_path, new_stan_file_path)

    # Construct the output CSV file path in / 'data' / 'data' / 'csv'
    for csv_file_path in csv_dir.glob('*.*'):
        # Construct the output CSV file path
        new_stan_file_path = stan_dir / (csv_file_path.stem + '.csv')
        standardization(csv_file_path, new_stan_file_path)


if __name__ == '__main__':
    json_all_file_to_csv()
    standardization_for_all()
