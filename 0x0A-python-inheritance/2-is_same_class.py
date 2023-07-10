#!usr/bin/python3

"""Write a function that returns True if the object is exactly
an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """
    Args: obj, a_class
    Returns true is object is an instance of class otherwise false
    """
    if obj.__class__ is a_class:
        return True
    else:
        return False
