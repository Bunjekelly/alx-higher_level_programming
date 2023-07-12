#!/usr/bin/python3

""" a class Student that defines a student """


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """initializing the class with age, first and last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs and isinstance(attrs, list):
            return {attr: getattr(self, attr) for
                    attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__
