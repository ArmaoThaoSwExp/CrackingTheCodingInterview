"""
Author: Armao Thao

Description:
    Chapter 19: cracking the coding interview
"""

import unittest
from chapter19_7 import contsum


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        arr = [2, -8, 3, -2, 4, -10]
        result = contsum(arr)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
