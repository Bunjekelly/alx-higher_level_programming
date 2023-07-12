#!/usr/bin/python3

""" a class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defining the class square that inherits from Rectangle"""
    def __init__(self, size):
        """initializes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
