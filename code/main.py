import pandas as pd

from datasets.convertData import *
from datasets.decryptName import decryptName
from scripts.standardization import standardization
from models.chooseAttribut import chooseAttribut
from utils.paths import *
from models.pca import pca
from scripts.outlier import find_replace_outlier
from models.cMeans import *
from visualization.cMeansPlot import cMeans_reduce_and_plot
from visualization.cMeans3DPlot import cMeans_reduce_and_plot_3D

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

def convert_rows_into_colums_for_all() -> object:
    label_csv_dir = get_label_path()

    for stan_file_path in label_csv_dir.glob('*.csv'):
        df = pd.read_csv(stan_file_path,header=None)
        label_colums_file_path = label_csv_dir / (stan_file_path.stem + 'column.csv')
        convert_row_to_columns(df, label_colums_file_path)

def merge_labels_with_data_for_all():
    data_csv_dir = get_csv_path()
    label_csv_dir = get_label_path()
    data_csv_all_dir = get_klassifikation_path()

    dataList = ['x1.csv','x2.csv']
    labelList = ['y1column.csv','y2column.csv']

    for dataName, labelName in zip(dataList, labelList):
        pathData = Path.joinpath(data_csv_dir, dataName)
        pathLabel = Path.joinpath(label_csv_dir,labelName)
        merge_labels_with_data(pathData, pathLabel, data_csv_all_dir)


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




def cMeans3_for_all():
    selection_dir_1 = get_selection_path_1()
    clustering_3_path = get_cmean_3_path_1()
    for selection_file_path in selection_dir_1.glob('*.csv'):
        print(selection_file_path)
        # Call the standardization function
        clustering_cmeans(selection_file_path, 3, clustering_3_path)


def cMeans_reduce_and_plot_for_all():
    # 'data' / 'data' / 'cMeans3' / '18_2_17'
    stan_dir_1 = get_cmean_3_path_1()

    # Construct the output CSV file path in 'data' / 'data' / 'cMeans3' / '18_2_17'
    for stan_file_path in stan_dir_1.glob('*.csv'):
        df = pd.read_csv(stan_file_path)
        cMeans_reduce_and_plot(df, stan_file_path.name)

def cMeans_reduce_and_plot_for_all_3D():
    # 'data' / 'data' / 'cMeans3' / '18_2_17'
    stan_dir_1 = get_cmean_3_path_1()

    # Construct the output CSV file path in 'data' / 'data' / 'cMeans3' / '18_2_17'
    for stan_file_path in stan_dir_1.glob('*.csv'):
        df = pd.read_csv(stan_file_path)
        cMeans_reduce_and_plot_3D(df, stan_file_path.name)

def cMeans4_for_all():
    selection_dir_1 = get_selection_path_1()
    clustering_4_path = get_cmean_4_path_1()
    for selection_file_path in selection_dir_1.glob('*.csv'):
        print(selection_file_path)
        # Call the standardization function
        clustering_cmeans(selection_file_path, 4, clustering_4_path)

def cMeans4_reduce_and_plot_for_all_3D():
    # 'data' / 'data' / 'cMeans4' / '18_2_17'
    stan_dir_1 = get_cmean_4_path_1()

    # Construct the output CSV file path in 'data' / 'data' / 'cMeans4' / '18_2_17'
    for stan_file_path in stan_dir_1.glob('*.csv'):
        df = pd.read_csv(stan_file_path)
        cMeans_reduce_and_plot_3D(df, stan_file_path.name)
def cMeans5_for_all():
    selection_dir_1 = get_selection_path_1()
    clustering_5_path = get_cmean_5_path_1()
    for selection_file_path in selection_dir_1.glob('*.csv'):
        print(selection_file_path)
        # Call the standardization function
        clustering_cmeans(selection_file_path, 5, clustering_5_path)

def cMeans5_reduce_and_plot_for_all_3D():
    # 'data' / 'data' / 'cMeans4' / '18_2_17'
    stan_dir_1 = get_cmean_5_path_1()

    # Construct the output CSV file path in 'data' / 'data' / 'cMeans4' / '18_2_17'
    for stan_file_path in stan_dir_1.glob('*.csv'):
        df = pd.read_csv(stan_file_path)
        cMeans_reduce_and_plot_3D(df, stan_file_path.name)

#18_2_17
def evalutation_for_all_1():
    selection_dir_1 = get_selection_path_1()

    for selection_file_path in selection_dir_1.glob('*.csv'):
        # Call the standardization function
        clustering_evaluation(selection_file_path, 41)

def evaluation_for_all():
    outlier_dir = get_outlier_path()
    for outlier_dir_path in outlier_dir.glob('*.csv'):
        print(outlier_dir_path)
        clustering_evaluation(outlier_dir_path, 6)


def cMeans_withK():
    #list for ks
    kList = [10, 13, 7, 13, 13, 33, 20, 15, 19, 9, 14]
    kList_1 = [5, 31, 18]

    # list for name
    nameList= ["rosetta.csv", "salt.csv", "hobbit.csv", "earth.csv", "nks.csv", "einstein.csv", "symmetric.csv", "fibonacci.csv", "hitchhiker.csv", "lorem.csv", "sun.csv"]
    nameList_1 = ["x0.csv", "x1.csv", "x2.csv"]

    selection = get_selection_path_1()
    new_path = get_cmean_path()
    outlier = get_outlier_path()


    for name, clusterNummer in zip(nameList, kList):
        path = Path.joinpath(selection, name)
        clustering_cmeans_without(path, clusterNummer, new_path)


    for name, clusterNummer in zip(nameList_1, kList_1):
        path = Path.joinpath(outlier, name)
        clustering_cmeans_without(path, clusterNummer, new_path)

def plot_for_all():
    cmeans_dir = get_cmean_path()
    for cmeans_dir_path in cmeans_dir.glob('*.csv'):
        df = pd.read_csv(cmeans_dir_path)
        cMeans_reduce_and_plot_3D(df, cmeans_dir_path.stem)


if __name__ == '__main__':
    #json_all_file_to_csv()
    #standardization_for_all()
    # pca_for_all()
    #find_replace_outlier_for_all()
    #choose_attribut_for_all()
    #cMeans3_for_all()
    #cMeans_reduce_and_plot_for_all()
    #cMeans_reduce_and_plot_for_all_3D()
    #cMeans4_for_all()
    #cMeans5_for_all()
    #cMeans5_reduce_and_plot_for_all_3D()
    #evalutation_for_all_1()
    #evaluation_for_all()
    #cMeans_for_all()
    #cMeans_withK()
    #plot_for_all()
    #convert_rows_into_colums_for_all()
    merge_labels_with_data_for_all()


