#!/usr/bin/python3

"""a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after a specific string"""
    with open(filename, 'r', encoding="utf-8") as file_1:
        text = ''
        for line in file_1:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w', encoding="utf-8") as file_1:
        file_1.write(text)
