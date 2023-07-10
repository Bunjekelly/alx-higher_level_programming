#!/usr/bin/python3

"""a class MyList that inherits from list"""

class MyList(list):
    """defining a class MyList that inherits from base class list"""

    def print_sorted(self):
        """public instance method that prints the sorted list"""
        print(sorted(self))
