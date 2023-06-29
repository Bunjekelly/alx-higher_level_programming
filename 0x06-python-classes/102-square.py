#!/usr/bin/python3

"""a class Square that defines a square by size
gets area and does comparison"""


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

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

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
