#!/usr/bin/python3

"""unittest for base class"""

import unittest
import os
from mmodels.rectangle import Rectangle
from models.square import Square
from models.base import Base

class BaseTest(unittest.TestCase):
    """test cases"""

    def test_correct_id(self):
        """test cases to check id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(23)
        self.assertEqual(b2.id, 23)

        b3 = Base(9)
        self.assertEqual(b3.id, 9)

        b4 = Base(None)
        self.assertEqual(b4.id, 2)

        b5 = Base()
        self.assertEqual(b5.id, 3)

    def test_to_json(self):
        """test cases for json string"""
        r = Rectangle(10, 5, 6, 9)
        dic = r.to_dictionary()
        json_dic = Base.to_json_string([dic])
        result = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dic, result)

    def test_save_file(self):
        """test for saving to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file1:
            self.assertEqual(file1.read(), "[]")

        r1 = Rectangle(4, 5)
        Rectangle.save_to_file([r1])
        result = '[{"id": 1, "width": 4, "height": 5, "x": 0, "y": 0}]'
        with open("Rectangle.json", "r") as file1:
            self.assertEqual(f.read(), result)



    if __name__ == "__main__":
        unittest.main()
