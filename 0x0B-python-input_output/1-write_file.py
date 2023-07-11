#!/usr/bin/python3

"""a function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """function that writes to a text file and returns
    the number of characters written"""

    with open(filename, 'w', encoding="utf-8") as file_1:
        return file_1.write(text)
