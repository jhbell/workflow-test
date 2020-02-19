import unittest

from add_numbers import add, add_many

class TestAddNumbers(unittest.TestCase):
    """ Test the add_numbers module functionality """
    def test_positive(self):
        self.assertEqual(add(152, 383), 535)

    def test_negative(self):
        self.assertEqual(add(-15, -989), -1004)

    def test_mixed(self):
        self.assertEqual(add(-55, 102), 47)

    def test_add_many_zero(self):
        self.assertEqual(add_many(), 0)

    def test_add_many_simple(self):
        self.assertEqual(add_many(152, 383), 535)

    def test_add_many_many(self):
        self.assertEqual(add_many(10, 12, -7, 400), 415)
