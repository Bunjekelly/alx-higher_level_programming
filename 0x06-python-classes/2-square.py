#!/usr/bin/python3
# 2-square.py
"""creates a square with size which must be an int
else raises error"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """initializes the square with attribute size
        and raises type error if size is not int or value
        error is it is < 0"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
