#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer_test').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_max_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [3, 1, 6, 2]
        self.assertEqual(max_integer(unordered), 6)

    def test_max_begining_list(self):
        """Test at begining list of integers."""
        begining = [10, 2, 3, 4]
        self.assertEqual(max_integer(begining), 10)

    def test_max_end_list(self):
        """Test at the end list of integers."""
        end = [1, 2, 3, 45]
        self.assertEqual(max_integer(end), 45)

    def test_max_middle_list(self):
        """Test at the middle list of integers."""
        middle = [1, 2, 30, 4, 9]
        self.assertEqual(max_integer(middle), 30)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)


