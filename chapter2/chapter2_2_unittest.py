"""
Author: Armao Thao

Description:
    Chapter 2: cracking the coding interview
"""

import unittest
from chapter2_2 import Node, find, find_nth_to_end_element


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _generate_list(self, values):
        root = Node(values[0])
        current = root
        for value in values[1:]:
            current.next = Node(value)
            current = current.next
        return root

    def test_empty_list(self):
        result = find_nth_to_end_element(None, 1)
        self.assertEqual(result, None)

    def test_1_item_list(self):
        root = self._generate_list([102])
        result = find_nth_to_end_element(root, 0).value
        expected_result = 102
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        root = self._generate_list([102])
        result = find_nth_to_end_element(root, 1)
        expected_result = None
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        root = self._generate_list([102])
        result = find_nth_to_end_element(root, 2)
        expected_result = None
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

    def test_1_item_list(self):
        root = self._generate_list([10, 15, 35, 45, 100, 5200, 3000, 9000, 16, 21])
        result = find_nth_to_end_element(root, 0).value
        expected_result = 21
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        result = find_nth_to_end_element(root, 9).value
        expected_result = 10
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        result = find_nth_to_end_element(root, 4).value
        expected_result = 5200
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
