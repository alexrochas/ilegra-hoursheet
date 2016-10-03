import csv


def parse_csv(file):
    return list(csv.DictReader(file, delimiter=";"))
