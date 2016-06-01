"""
Author: Armao Thao

Description:
    Chapter 5: cracking the coding interview
"""

import unittest
from chapter5_2 import printbin


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        instr = "1.625"
        result = printbin(instr)
        print("result: {}".format(result))
        self.assertEqual(result, "1.101")

if __name__ == "__main__":
    unittest.main()
