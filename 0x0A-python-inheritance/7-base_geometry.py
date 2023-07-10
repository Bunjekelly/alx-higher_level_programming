#!/usr/bin/python3

"""a geometry class with area method and instance validator"""


class BaseGeometry:
    """defining the BaseGeometry class"""

    def area(self):
        """public instance method area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Args: name, value
        validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
