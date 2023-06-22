import pandas as pd

from datasets.convertData import json_to_csv
from datasets.decryptName import decryptName
from scripts.standardization import standardization
from models.chooseAttribut import chooseAttribut
from utils.paths import *
from models.pca import pca
from scripts.outlier import find_replace_outlier
from models.cMeans import clustering_cmeans

def json_all_file_to_csv():

    json_dir_1 = get_json_path_1()
    json_dir = get_json_path()
    csv_dir_1 = get_csv_path_1()
    csv_dir = get_csv_path()

    # 'data' / 'data' / '18_2_17_8_15_19_20_17_4_18'

    for json_file_path in json_dir_1.glob('*.json'):
        # Construct the output CSV file path
        # .stem attribute is used to get the filename stem (without the extension), which is then used to construct the output CSV file path.
        name = decryptName(json_file_path.stem)
        csv_file_path = csv_dir_1 / (name + '.csv')
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

def pca_for_all():
    # / 'data' / 'data' / 'standardization' / '18_2_17'
    stan_dir_1 = get_stan_path_1()
    # / 'data' / 'data' / 'standardization'
    stan_dir = get_stan_path()

    # Construct the output CSV file path in / 'data' / 'data' / 'standardization' / '18_2_17'
    for stan_file_path in stan_dir_1.glob('*.csv'):
        df = pd.read_csv(stan_file_path)
        pca(df, stan_file_path.name)

    for stan_file_path in stan_dir.glob('*.csv'):
        df = pd.read_csv(stan_file_path)
        pca(df, stan_file_path.name)

def find_replace_outlier_for_all():
    # / 'data' / 'data' / 'stan' / '18_2_17'
    stan_dir_1 = get_stan_path_1()
    # / 'data' / 'data' / 'stan'
    stan_dir = get_stan_path()
    # / 'data' / 'data' / 'outlier' / '18_2_17'
    outlier_dir_1 = get_outlier_path_1()
    # / 'data' / 'data' / 'outlier'
    outlier_dir = get_outlier_path()

    # Construct the output CSV file path in / 'data' / 'data' / 'standardization' / '18_2_17'
    for stan_file_path in stan_dir_1.glob('*.csv'):
        new_out_file_path = outlier_dir_1 / (stan_file_path.stem + '.csv')
        # Call the standardization function
        find_replace_outlier(stan_file_path, new_out_file_path)

    # Construct the output CSV file path in / 'data' / 'data' / 'csv'
    for stan_file_path in stan_dir.glob('*.*'):
        # Construct the output CSV file path
        new_out_file_path = outlier_dir / (stan_file_path.stem + '.csv')
        find_replace_outlier(stan_file_path, new_out_file_path)


def choose_attribut_for_all():
    # / 'data' / 'data' / 'outlier' / '18_2_17'
    outlier_dir_1 = get_outlier_path_1()
    #/ 'data' / 'data' / 'attributeSelection' / '18_2_17'
    selection_dir_1 = get_selection_path_1()

    # Construct the output CSV file path in / 'data' / 'data' / 'standardization' / '18_2_17'
    for outlier_file_path in outlier_dir_1.glob('*.csv'):
        new_outlier_file_path = selection_dir_1 / (outlier_file_path.stem + '.csv')
        # Call the standardization function
        chooseAttribut(outlier_file_path, new_outlier_file_path)

def cMeans_for_all():
    selection_dir_1 = get_selection_path_1()
    clustering_3_path = get_cmean_3_path_1()
    for selection_file_path in selection_dir_1.glob('*.csv'):
        print(selection_file_path)
        new_data_path = clustering_3_path / (selection_file_path.stem + '.csv')
        # Call the standardization function
        clustering_cmeans(selection_file_path, 3, clustering_3_path)


if __name__ == '__main__':
    json_all_file_to_csv()
    #standardization_for_all()
    #pca_for_all()
    #find_replace_outlier_for_all()
    #choose_attribut_for_all()
    #cMeans_for_all()


