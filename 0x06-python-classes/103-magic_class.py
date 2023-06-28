#!/usr/bin/python3
"""a magic class that imitates a given byte code"""
import math


class MagicClass:
    """the magicclass"""
    def __init__(self, radius=0):
        """initializing the class"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
        return

    def area(self):
        """Disassembly of area"""
        return ((self.__radius) ** 2) * math.pi

    def circumference(self):
        """Disassembly of circumference"""
        return ((2 * math.pi) * self.__radius)
