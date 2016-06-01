"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""

import unittest
from chapter1_3 import remove_duplicates_in_str, remove_duplicates_in_str_cstyle, remove_duplicates_additional_buffer


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_duplicate(self):
        instr = [each_char for each_char in "aa"]
        result = remove_duplicates_in_str(instr)
        result2 = remove_duplicates_in_str_cstyle(instr)
        self.assertEqual(result, [each_char for each_char in "a"])
        self.assertEqual(result2, [each_char for each_char in "a"])
        result3 = remove_duplicates_additional_buffer(instr)
        self.assertEqual(result3, [each_char for each_char in "a"])

    def test_no_duplicate(self):
        instr = [each_char for each_char in "ab"]
        result = remove_duplicates_in_str(instr)
        result2 = remove_duplicates_in_str_cstyle(instr)
        self.assertEqual(result, [each_char for each_char in "ab"])
        self.assertEqual(result2, [each_char for each_char in "ab"])
        result3 = remove_duplicates_additional_buffer(instr)
        self.assertEqual(result3, [each_char for each_char in "ab"])

    def test_duplicates_sequential(self):
        instr = [each_char for each_char in "aaa"]
        result = remove_duplicates_in_str(instr)
        result2 = remove_duplicates_in_str_cstyle(instr)
        self.assertEqual(result, [each_char for each_char in "a"])
        self.assertEqual(result2, [each_char for each_char in "a"])
        result3 = remove_duplicates_additional_buffer(instr)
        self.assertEqual(result3, [each_char for each_char in "a"])

    def test_duplicates_non_sequential_double(self):
        instr = [each_char for each_char in "abcabc"]
        result = remove_duplicates_in_str(instr)
        result2 = remove_duplicates_in_str_cstyle(instr)
        self.assertEqual(result, [each_char for each_char in "abc"])
        self.assertEqual(result2, [each_char for each_char in "abc"])
        result3 = remove_duplicates_additional_buffer(instr)
        self.assertEqual(result3, [each_char for each_char in "abc"])

    def test_duplicates_non_sequential_multiple(self):
        instr = [each_char for each_char in "abcabcabcabc"]
        result = remove_duplicates_in_str(instr)
        result2 = remove_duplicates_in_str_cstyle(instr)
        self.assertEqual(result, [each_char for each_char in "abc"])
        self.assertEqual(result2, [each_char for each_char in "abc"])
        result3 = remove_duplicates_additional_buffer(instr)
        self.assertEqual(result3, [each_char for each_char in "abc"])

    def test_duplicates_a_thru_z_uniq_char(self):
        instr = [each_char for each_char in range(ord('a'), ord('z'))]
        result = remove_duplicates_in_str(instr)
        result2 = remove_duplicates_in_str_cstyle(instr)
        self.assertEqual(result, instr)
        self.assertEqual(result2, instr)
        result3 = remove_duplicates_additional_buffer(instr)
        self.assertEqual(result3, instr)

    def test_empty_str(self):
        result = remove_duplicates_in_str([""])
        result2 = remove_duplicates_in_str_cstyle([""])
        self.assertEqual(result, [""])
        self.assertEqual(result2, [""])
        result3 = remove_duplicates_additional_buffer([""])
        self.assertEqual(result3, [""])

    def test_one_char_str(self):
        result = remove_duplicates_in_str(["d"])
        result2 = remove_duplicates_in_str_cstyle(["d"])
        self.assertEqual(result, ["d"])
        self.assertEqual(result2, ["d"])
        result3 = remove_duplicates_additional_buffer(["d"])
        self.assertEqual(result3, ["d"])

if __name__ == "__main__":
    unittest.main()
