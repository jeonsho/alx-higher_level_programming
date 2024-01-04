#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        """Test when max integer is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test when max integer is at the beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_middle(self):
        """Test when max integer is in the middle"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test a single element list"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_identical_elements(self):
        """Test a list where all elements are the same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_none_input(self):
        """Test passing None as input"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integers(self):
        """Test a list with non-integer types"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

if __name__ == "__main__":
    unittest.main()
