#!/usr/bin/python3

"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """defining a function that reads a text file and print to stdout"""
    with open(filename, encoding="utf-8") as file_1:
        print(file_1.read())
