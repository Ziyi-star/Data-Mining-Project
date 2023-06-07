from pathlib import Path

def get_csv_path_1():
    current_dir = Path.cwd()
    project_dir = current_dir.parent.parent
    csv_dir_1 = project_dir / 'data' / 'data' / 'csv' / '18_2_17'
    return csv_dir_1

def get_csv_path():
    current_dir = Path.cwd()
    project_dir = current_dir.parent.parent
    csv_dir = project_dir / 'data' / 'data' / 'csv'
    return csv_dir

def get_json_path():
    current_dir = Path.cwd()
    project_dir = current_dir.parent.parent
    json_dir = project_dir / 'data' / 'data'
    return json_dir

def get_json_path_1():
    current_dir = Path.cwd()
    project_dir = current_dir.parent.parent
    json_dir_1 = project_dir / 'data' / 'data' / '18_2_17_8_15_19_20_17_4_18'
    return json_dir_1

