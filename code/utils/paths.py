from pathlib import Path

"""
Diese Datei dient zur Wiedergebung der path für alle Ordnen in der Data Ordner. Die Struktur für
die Daten ist gleich wie bei die Json Datei. csv Daten und die Daten nach dem Standardization werden
separate zur eingenen Ordnen zugeordnet. Dateiname bleiben gleich.
"""

def get_csv_path_1():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    csv_dir_1 = project_dir / 'data' / 'data' / 'csv' / '18_2_17'
    return csv_dir_1

def get_csv_path():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    csv_dir = project_dir / 'data' / 'data' / 'csv'
    return csv_dir

def get_json_path():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    json_dir = project_dir / 'data' / 'data'
    return json_dir

def get_json_path_1():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    json_dir_1 = project_dir / 'data' / 'data' / '18_2_17_8_15_19_20_17_4_18'
    return json_dir_1

def get_stan_path():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    stan_dir = project_dir / 'data' / 'data' / 'standardization'
    return stan_dir

def get_stan_path_1():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    stan_dir = project_dir / 'data' / 'data' / 'standardization' / '18_2_17'
    return stan_dir

def get_outlier_path():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    stan_dir = project_dir / 'data' / 'data' / 'outlier'
    return stan_dir

def get_outlier_path_1():
    current_dir = Path.cwd()
    project_dir = current_dir.parent
    stan_dir = project_dir / 'data' / 'data' / 'outlier' / '18_2_17'
    return stan_dir


