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
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            dic = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dic.update({attr: getattr(self, attr)})
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for attr in json:
            setattr(self, attr, json[attr])
