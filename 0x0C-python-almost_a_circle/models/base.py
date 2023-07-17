#!/usr/bin/python3
"""defining a class base"""
import json
import csv
import os
import os.path

class Base:
    """defining class Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initializing the class"""
        if id != None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """"writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list1 = []
        with open(filename, 'w', encoding="utf-8") as file1:
            if list_objs is None:
                file1.write("[]")
            else:
                for obj in list_objs:
                    dic = obj.to_dictionary()
                    list1.append(dic)
                file1.write(cls.to_json_string(list1))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                class_ins = cls(3, 6)
            elif cls.__name__ == "Square":
                class_ins = cls(3)
            else:
                return
            class_ins.update(**dictionary)
            return class_ins

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list1 = []
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding="utf-8") as file1:
            json_str = file1.read()
            loaded_list = cls.from_json_string(json_str)
            for dict in loaded_list:
                instance = cls.create(**dict)
                list1.append(instance)
        return list1
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as file1:
            if list_objs is None or len(list_objs) == 0:
                file1.write("[]")
                return
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]
        writer = csv.DictWriter(file1, fieldnames=fields)
        for obj in list_objs:
            writer.writerows(obj.to_dictionary())
