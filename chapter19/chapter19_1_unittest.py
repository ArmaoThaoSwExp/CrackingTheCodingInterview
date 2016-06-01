"""
Author: Armao Thao

Description:
    Chapter 19: cracking the coding interview
"""

import unittest
from chapter19_1 import swapvars


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        result = swapvars(0x0000, 0xFFFF)
        self.assertEqual(result, (0xFFFF, 0x0000))
        result = swapvars(0x8888, 0x1111)
        self.assertEqual(result, (0x1111, 0x8888))


if __name__ == "__main__":
    unittest.main()
