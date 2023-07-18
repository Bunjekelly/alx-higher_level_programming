#!/usr/bin/python3

"""unittest for the square class"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class SquareTest(unittest.TestCase):
    """test class for square"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_str(self):
        """testing printing str method"""
        s1 = Square(2, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/0 - 2")

    def test_square_area(self):
        """testing for area"""
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)

    def test_square_errors(self):
        """testing for error raises"""
        with self.assertRaises(TypeError):
            s3 = Square(1, "3")
        with self.assertRaises(TypeError):
            s4 = Square("3", 10)
        with self.assertRaises(TypeError):
            s5 = Square(4.8, 3, 9, 3)
        with self.assertRaises(TypeError):
            s6 = Square(4, 5, 4.5, 1)
        with self.assertRaises(TypeError):
            s7 = Square(4, True, 6, 8)
        with self.assertRaises(TypeError):
            s8 = Square(None, 4)
        with self.assertRaises(ValueError):
            s9 = Square(-4, 9)
        with self.assertRaises(ValueError):
            s10 = Square(7, -9)
        with self.assertRaises(ValueError):
            s11 = Square(0)

    def test_square_args(self):
        """testing for arg updates"""
        S = Square(10, 10, 10)
        s.update(2)
        self.assertEqual(s.update(), "[Square] (2) 10/10 - 10")

        s.update(2, 5)
        self.assertEqual(s.update(), "[Square] (2) 10/10 - 5")

    def test_square_kwargs(self):
        """testing for kwargs update"""
        s1 = Square(10, 10, 10)
        s1.update(size=2, x=2)
        self.assertEqual(s1.update(), "[Square] (1) 2/10 - 2")

        s1.update(y=3, size=4, x=5, id=45)
        self.assertEqual(s1.update(), "[Square] (45) 5/3 - 4")
    
    def test_square_dictionary(self):
        """testing for dictionary"""
        s2 = Square(12, 2, 1, 19)
        self.assertEqual(s2.to_dictionary(), {'x': 2, 'y': 1, 'id': 19, 'size': 12})
    
    if __name__ == "__main__":
        unittest.main()
