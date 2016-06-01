"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""

import unittest
from chapter1_7 import zero_row_and_col


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_replace_empty(self):
        pass

    def test_3by3_one_zero(self):
        matrix = [[1 for i in range(3)],
                  [1 for i in range (3)],
                  [1 for i in range(2)] + [0]]
        expected_result = [[1 for i in range(2)] + [0],
                           [1 for i in range(2)] + [0],
                           [0 for i in range(3)]]
        zero_row_and_col(matrix)
        print("   input matrix: {}".format(matrix))
        print("expected matrix: {}".format(expected_result))
        self.assertEqual(matrix, expected_result)

    def test_3by3_one_zero_middle(self):
        matrix = [[1 for i in range(3)],
                  [1, 0, 1],
                  [1 for i in range (3)]]
        expected_result = [[1, 0, 1],
                           [0, 0, 0],
                           [1, 0, 1]]
        zero_row_and_col(matrix)
        print("   input matrix: {}".format(matrix))
        print("expected matrix: {}".format(expected_result))
        self.assertEqual(matrix, expected_result)

    def test_3by3_one_zero_top(self):
        matrix = [[0, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
        expected_result = [[0, 0, 0],
                           [0, 1, 1],
                           [0, 1, 1]]
        zero_row_and_col(matrix)
        print("   input matrix: {}".format(matrix))
        print("expected matrix: {}".format(expected_result))
        self.assertEqual(matrix, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
