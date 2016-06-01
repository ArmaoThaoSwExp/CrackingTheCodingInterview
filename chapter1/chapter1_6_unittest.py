"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""

import unittest
from chapter1_6 import rotate_n_by_n_matrix_90deg


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_replace_empty(self):
        pass

    def test_6by6_matrix(self):
        matrix = [[315, 301, 755, 542, 955,  33],
                  [943, 613, 233, 880, 945, 280],
                  [908, 609, 504,  61, 849, 551],
                  [933, 251, 706, 707, 913, 917],
                  [479, 785, 634,  97, 851, 745],
                  [472, 348, 104, 645,  17, 273]]
        expected_result = [[472, 479, 933, 908, 943, 315],
                           [348, 785, 251, 609, 613, 301],
                           [104, 634, 706, 504, 233, 755],
                           [645,  97, 707,  61, 880, 542],
                           [ 17, 851, 913, 849, 945, 955],
                           [273, 745, 917, 551, 280,  33]]
        rotate_n_by_n_matrix_90deg(matrix)
        self.assertEqual(matrix, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
