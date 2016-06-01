"""
Author: Armao Thao

Description:
    Chapter 8: cracking the coding interview
"""

import unittest
from chapter8_5 import wellparenthesized


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        wellparenthesized(3)
        print("\n\n")
        wellparenthesized(5)
        print("\n\n")
        wellparenthesized(8)


if __name__ == "__main__":
    unittest.main()
