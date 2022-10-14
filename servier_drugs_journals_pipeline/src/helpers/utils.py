import csv
import json5

from datetime import datetime


def read_csv(file_path):
    """
    This function reads a csv file
    :param file_path: the path to the csv file
    :return: list of dicts that contains the csv rows (dict key is the first row name)
    """
    with open(file_path, encoding='utf-8') as in_file:
        data = csv.DictReader(in_file)
        return list(data)


def read_json(file_path):
    """
    This function reads a json file
    :param file_path: the path to the json file
    :return: the json file as a python dict
    """
    with open(file_path, encoding="utf-8") as in_file:
        data = json5.loads(in_file.read())
        return data


def date_parser(date_str):
    """
    checks if date corresponds to one of the known patters and returns a datetime object if yes
    a warning will appear if the date format is known
    :raises ValueError if the format is unknown
    :param date_str: string that contains date
    :return: date in datetime object
    """
    known_date_patterns = ["%d %B %Y", "%d/%m/%Y", "%Y-%m-%d"]
    result = None
    for pattern in known_date_patterns:
        try:
            result = datetime.strptime(date_str, pattern)
        except ValueError:
            continue
    if not result:
        raise ValueError(f"unknown date format : {date_str}")
    return result


def write_graph(result, file_path):
    """
    This function write object (dict, list of dicts) in json file
    :param result: object that will be written in json file
    :param file_path: output path
    :return: void
    """
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(json5.dumps(result))
