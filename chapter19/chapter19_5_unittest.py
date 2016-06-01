"""
Author: Armao Thao

Description:
    Chapter 19: cracking the coding interview
"""

import unittest
from chapter19_5 import mastermind_guess


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        solution = "RGGB"
        guess = "YRGB"
        result = mastermind_guess(guess, solution)
        self.assertEqual(result, (2, 1))

if __name__ == "__main__":
    unittest.main()
