import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_5_10_returns_5_is_less_than_10(self):
        self.assertEqual("5 is less than 10", compare (5,10))

    def test_compare_7_7_returns_7_is_the_same_as_7(self):
        self.assertEqual("7 is the same as 7", compare(7, 7))