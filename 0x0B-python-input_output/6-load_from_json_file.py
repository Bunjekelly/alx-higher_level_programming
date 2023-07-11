#!/usr/bin/python3

"""a function that creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename, encoding="utf-8") as file_1:
        file_content = file_1.read()
        obj = json.loads(file_content)
        return obj
