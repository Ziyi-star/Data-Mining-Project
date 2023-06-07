from datasets.convertData import json_to_csv


if __name__ =='__main__':
    # Beispielaufruf
    json_file_path = 'input.json'  # Pfad zur JSON-Datei
    csv_file_path = 'output.csv'  # Pfad zur CSV-Datei

    json_to_csv(json_file_path, csv_file_path)