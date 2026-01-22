#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer
suite = unittest.TestSuite()

class TestMaxInteger(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1,5,2,3,4]), 5)
        self.assertEqual(max_integer("qwerty"), 'y')

    def test_invalid(self):
        with self.assertRaises(TypeError):
            max_integer(None)
