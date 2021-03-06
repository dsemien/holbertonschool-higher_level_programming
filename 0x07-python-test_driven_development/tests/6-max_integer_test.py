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

    def test_one_element(self):
        """Pass one element in list
        """
        self.assertEqual(max_integer([5]), 5)
        
    def test_max_in_mid(self):
        """Pass max in middle
        """
        self.assertEqual(max_integer([11, 32, 43, 84, 15, 56, 67]), 84)
            
    def test_nothing(self):
        """Pass Nothing
        """
        self.assertEqual(max_integer([]), None)

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
