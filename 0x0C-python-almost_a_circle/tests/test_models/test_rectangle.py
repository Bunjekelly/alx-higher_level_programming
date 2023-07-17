#!/usr/bin/python3

"""unittest for rectangle"""
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base

class RectangleTest(unittest.TestCase):
    """rectanle test class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_inheritance(self):
        """rectangle test inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle_id(self):
        """rectange id test"""
        r0 = Rectangle(2, 4)
        r1 = Rectangle(2, 4, 5, 9, 23)
        self.assertEqual(r0.id, 1)
        self.assertEqual(r1.id, 23)

    def test_rectangle_width(self):
        """rectangle width test"""
        r2 = Rectangle(3, 8)
        self.assertEqual(r2.width, 3)

    def test_rectangle_height(self):
        """rectangle height test"""
        r3 = Rectangle(2, 12)
        self.assertEqual(r3.height, 12)

    def test_rectangle_x(self):
        """rectangle x test"""
        r4 = Rectangle(2, 4, 5, 6)
        self.assertEqual(r4.x, 5)

    def test_rectangle_y(self):
        """rectangle y test"""
        r5 = Rectangle(3, 13, 6, 9)
        self.assertEqual(r5.y, 9)

    def test_rectangle_raises(self):
        """testing for error raises"""
        with self.assertRaises(TypeError):
            r6 = Rectangle(0.5, 3)
        with self.assertRaises(ValueError):
            r7 = Rectangle(-4, 5)
        with self.assertRaises(ValueError):
            r8 = Rectangle(3, -8)
        with self.assertRaises(TypeError):
            r8 = Rectangle(3, "str")
        with self.assertRaises(TypeError):
            r9 = Rectangle(3, 5, "str", 3)
        with self.assertRaises(TypeError):
            r10 = Rectangle(3, 6, 7, True)
        with self.assertRaises(ValueError):
            r11 = Rectangle(3, 7, -5, 7)
        with self.assertRaises(ValueError):
            r12 = Rectangle(1, 8, 3, -23)

    def test_rectangle_area(self):
        """testing for rectangle area"""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)
        r1 = Rectangle( 2, 4, 3, 8)
        self.assertEqual(r1.area(), 8)
        r2 = Rectangle(3, 2, 5, 8, 15)
        self.assertEqual(r2.area(), 6)

    if __name__ == "__main__":
        unittest.main()
