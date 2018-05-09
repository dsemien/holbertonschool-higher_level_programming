#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """A class of test cases for max_integer
    """

    def test_control(self):
        """Passing all correct elements
        """
        self.assertEqual(max_integer([1, -2, 30, 4, 100, 45, 101]), 101)

    def test_nothing(self):
        """Pass Nothing
        Pass one element
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)

    def test_negative(self):
        """Pass negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -30, -4, -100, -45, -101]), -1)

    def test_wrngtype(self):
        """Pass wrong types
        """
        with self.assertRaises(TypeError):
            max_integer([11, "hi", -30, "Holberton", {}])
            max_integer({'cat': 'meow', 'dog': 'bark' })

if __name__ == '__main__':
    unittest.main()
