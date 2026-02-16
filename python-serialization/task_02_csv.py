import csv
import json


def convert_csv_to_json(filename):
    file_content = None
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            file_content = list(csv.DictReader(csvfile))
        with open('data.json', mode='w', newline='', encoding='utf-8') as file:
            json.dump(file_content, file)
    except Exception:
        print(file_content)
        return False