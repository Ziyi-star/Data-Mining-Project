import json
import csv


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



