"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""

import unittest
from chapter1_2 import reverse_str

class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_reverse_unique_str_odd_len(self):
        instr = [each_char for each_char in "apple"]
        instr_reverse = instr[::-1]
        reverse_str(instr)
        self.assertEqual(instr, instr_reverse)

    def test_reverse_unique_str_even_len(self):
        instr = [each_char for each_char in "banana"]
        instr_reverse = instr[::-1]
        reverse_str(instr)
        self.assertEqual(instr, instr_reverse)

    def test_reverse_palandrone(self):
        instr = [each_char for each_char in "racecar"]
        instr_reverse = instr[:]
        reverse_str(instr)
        self.assertEqual(instr, instr_reverse)

    def test_reverse_empty_str(self):
        instr = [""]
        reverse_str(instr)
        self.assertEqual(instr, [""])


if __name__ == "__main__":
    unittest.main()
