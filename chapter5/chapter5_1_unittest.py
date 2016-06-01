"""
Author: Armao Thao

Description:
    Chapter 5: cracking the coding interview
"""

import unittest
from chapter5_1 import setbits


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        n = int("10000000000", 2)
        m = int("10101", 2)
        result = setbits(n, m, 2, 6)
        self.assertEqual(result, int("10001010100", 2))

if __name__ == "__main__":
    unittest.main()
