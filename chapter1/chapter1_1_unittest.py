"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""

import unittest
from chapter1_1 import unique_char_str, unique_char_str_using_dict


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_all_unique(self):
        mystr = "".join([chr(i) for i in range(ord('a'), ord('z') + 1)])
        self.assertEqual(unique_char_str(mystr), True)
        self.assertEqual(unique_char_str_using_dict(mystr), True)

    def test_one_non_unique(self):
        mystr = "".join([chr(i) for i in range(ord('a'), ord('z') + 1)])
        mystr += "a"
        self.assertEqual(unique_char_str(mystr), False)
        self.assertEqual(unique_char_str_using_dict(mystr), False)

if __name__ == "__main__":
    unittest.main()
