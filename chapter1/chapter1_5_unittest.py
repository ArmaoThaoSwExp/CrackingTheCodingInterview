"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""

import unittest
from chapter1_5 import replace_space_with_percent20, replace_space_with_percent20_cstyle


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_replace_empty(self):
        pass

    def test_replace_no_space(self):
        instr = ""
        result = replace_space_with_percent20(instr)
        self.assertEqual(result, instr)
        instr = [each_char for each_char in instr]
        result = replace_space_with_percent20_cstyle(instr)
        self.assertEqual(result, instr)

    def test_replace_single_space(self):
        instr = " "
        result = replace_space_with_percent20(instr)
        expected_result = "%20"
        self.assertEqual(result, expected_result)
        instr = [each_char for each_char in instr]
        expected_result = [each_char for each_char in expected_result]
        result = replace_space_with_percent20_cstyle(instr)
        self.assertEqual(result, expected_result)

    def test_replace_space_beginning(self):
        instr = " a"
        result = replace_space_with_percent20(instr)
        expected_result = "%20a"
        self.assertEqual(result, expected_result)
        instr = [each_char for each_char in instr]
        expected_result = [each_char for each_char in expected_result]
        result = replace_space_with_percent20_cstyle(instr)
        self.assertEqual(result, expected_result)

    def test_replace_space_middle(self):
        instr = "a b"
        result = replace_space_with_percent20(instr)
        expected_result = "a%20b"
        self.assertEqual(result, expected_result)
        instr = [each_char for each_char in instr]
        expected_result = [each_char for each_char in expected_result]
        result = replace_space_with_percent20_cstyle(instr)
        self.assertEqual(result, expected_result)

    def test_replace_space_end(self):
        instr = "a "
        result = replace_space_with_percent20(instr)
        expected_result = "a%20"
        self.assertEqual(result, expected_result)
        instr = [each_char for each_char in instr]
        expected_result = [each_char for each_char in expected_result]
        result = replace_space_with_percent20_cstyle(instr)
        self.assertEqual(result, expected_result)

    def test_replace_multiple_space_non_sequential(self):
        instr = "a b c d"
        result = replace_space_with_percent20(instr)
        expected_result = "a%20b%20c%20d"
        self.assertEqual(result, expected_result)
        instr = [each_char for each_char in instr]
        expected_result = [each_char for each_char in expected_result]
        result = replace_space_with_percent20_cstyle(instr)
        self.assertEqual(result, expected_result)

    def test_replace_multiple_space_sequential(self):
        instr = "a  b  c  d"
        result = replace_space_with_percent20(instr)
        expected_result = "a%20%20b%20%20c%20%20d"
        self.assertEqual(result, expected_result)
        instr = [each_char for each_char in instr]
        expected_result = [each_char for each_char in expected_result]
        result = replace_space_with_percent20_cstyle(instr)
        self.assertEqual(result, expected_result)

    def test_replace_multiple_space_permutations(self):
        instr = " a  b  c   d  "
        result = replace_space_with_percent20(instr)
        expected_result = "%20a%20%20b%20%20c%20%20%20d%20%20"
        self.assertEqual(result, expected_result)
        instr = [each_char for each_char in instr]
        expected_result = [each_char for each_char in expected_result]
        result = replace_space_with_percent20_cstyle(instr)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
