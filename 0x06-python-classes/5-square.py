#!/usr/bin/python3
# 5-square.py
"""creates a square with size which must be an int
else raises error and also creates a property to
retrieve it, also returns the area. It also prints
the square in stdout with #."""


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

    def area(self):
        """returns the current square area"""
        return (self.__size)**2

    def my_print(self):
        """that prints in stdout the square
        with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def size(self):
        """returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
