#!/usr/bin/python3

"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """defining the add attribute function"""

    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
