#!/usr/bin/python3

# 0-add_integer.py
"""a function that adds 2 integers"""


def add_integer(a, b=98):
    """accepts integers or float values
    and returns the sum of integer addition"""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer or float")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer or float")
    return (int(a) + int(b))
