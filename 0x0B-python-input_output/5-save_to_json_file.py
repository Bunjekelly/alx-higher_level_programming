#!/usr/bin/python3

""" a function that writes an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using json representation"""
    with open(filename, 'w', encoding="utf-8") as file_1:
        json.dump(my_obj, file_1)
