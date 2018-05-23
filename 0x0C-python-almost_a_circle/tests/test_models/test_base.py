#!/usr/bin/python3
""" Unittest for Base Class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """A test cases for Base Class"""

    def test_control(self):
        """ Testing the standard id output"""
        testid_0 = Base(42)
        self.assertEqual(testid_0.id, 42)
        testid_1 = Base(-42)
        self.assertEqual(testid_1.id, -42)
        testid_2 = Base(4.2)
        self.assertEqual(testid_2.id, 4.2)
        testid_3 = Base(-4.2)
        self.assertEqual(testid_3.id, -4.2)

    def test_noarg(self):
        """Testing no argument"""
        test_noarg0 = Base(None)
        test_noarg1 = Base()
        with self.assertRaises(AssertionError):
            self.assertEqual(test_noarg0.id, None)
        with self.assertRaises(TypeError):
            self.assertEqual(test_noarg1.id,)

    def test_type(self):
        """ Testing Type is int"""
        test_type0 = Base(42)
        test_type1 = Base("42")
        self.assertEqual(type(test_type0.id), int)
        with self.assertRaises(AssertionError):
            self.assertEqual(type(test_type1.id), int)
