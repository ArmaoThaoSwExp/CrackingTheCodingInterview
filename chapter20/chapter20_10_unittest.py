"""
Author: Armao Thao

Description:
    Chapter 20: cracking the coding interview
"""

import unittest
from chapter20_10 import find_link_words


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        wordsdict = {"LAMP", "LIMP", "LIME", "LIKE", "NIGHT", "DONE", "ZONE",
                     "ARCS", "BONE", "BOWL", "CORN", "CARS", "CATS"}
        expected = ["DAMP", "LAMP", "LIMP", "LIME", "LIKE"]
        result = find_link_words("DAMP", "LIKE", wordsdict)
        self.assertEqual(expected, result)

    # def test_example_2(self):
    #     wordsdict = {"DAMP", "DUMP", "DAMN", "LAMP", "LIMP", "LIME", "LIKE", "NIGHT", "DONE", "ZONE", \
    #                  "ARCS", "BONE", "BOWL", "CORN", "CARS", "CATS"}
    #     expected = ["DAMP", "LIMP", "DUMP", "DAMN"]
    #     result = find_link_words("DAMP", "LIKE", wordsdict)
    #     self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
