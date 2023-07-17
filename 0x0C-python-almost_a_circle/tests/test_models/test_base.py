#!/usr/bin/python3

"""unittest for base class"""

import unittest
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

    if __name__ == "__main__":
        unittest.main()
