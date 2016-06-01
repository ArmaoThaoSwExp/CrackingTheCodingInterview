"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""

import unittest
from chapter1_4 import anagrams_count, anagrams_sort


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_anagram_empty(self):
        instr1 = ""
        instr2 = ""
        result = anagrams_sort(instr1, instr2)
        self.assertEqual(result, True)
        result = anagrams_count(instr1, instr2)
        self.assertEqual(result, True)

    def test_anagram_one_char(self):
        instr1 = "a"
        instr2 = "a"
        result = anagrams_sort(instr1, instr2)
        self.assertEqual(result, True)
        result = anagrams_count(instr1, instr2)
        self.assertEqual(result, True)

    def test_anagram_one_char_false(self):
        instr1 = "a"
        instr2 = "b"
        result = anagrams_sort(instr1, instr2)
        self.assertEqual(result, False)
        result = anagrams_count(instr1, instr2)
        self.assertEqual(result, False)

    def test_anagram_one_char_true(self):
        instr1 = "a"
        instr2 = "a"
        result = anagrams_sort(instr1, instr2)
        self.assertEqual(result, True)
        result = anagrams_count(instr1, instr2)
        self.assertEqual(result, True)

    def test_anagram_two_char_false(self):
        instr1 = "aa"
        instr2 = "bb"
        result = anagrams_sort(instr1, instr2)
        self.assertEqual(result, False)
        result = anagrams_count(instr1, instr2)
        self.assertEqual(result, False)

    def test_anagram_two_char_false(self):
        instr1 = "south"
        instr2 = "shout"
        result = anagrams_sort(instr1, instr2)
        self.assertEqual(result, True)
        result = anagrams_count(instr1, instr2)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()
