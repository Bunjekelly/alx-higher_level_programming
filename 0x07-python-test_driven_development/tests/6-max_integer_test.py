#!usr/bin/python3

"""unittest for the function def max_integer(list=[]):"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """deining unittests for Max integer"""

    def test_ascending(self):
        """Testing a list with values in ascending order"""
        test_list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer(test_list), 6)

    def test_descending(self):
        """Testing a list with values in descending order"""
        test_list = [6, 5, 4, 3, 2, 1]
        self.assertEqual(max_integer(test_list), 6)

    def test_unordered(self):
        """Testing an unordered list"""
        test_list = [7, 2, 4, 1, 9, 3]
        self.assertEqual(max_integer(test_list), 9)

    def test_empty(self):
        """Testing an empty list."""
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_single(self):
        """Testing a list with a single element."""
        test_list = [9]
        self.assertEqual(max_integer(test_list), 9)


if __name__ == '__main__':
    unittest.main()
