"""
Author: Armao Thao

Description:
    Chapter 2: cracking the coding interview
"""

import unittest
from chapter2_1 import Node, read_linked_list, remove_duplicates, remove_duplicates_no_temp_buff


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
        remove_duplicates_no_temp_buff(None)
        # This test just proves that an exception doesn't happen when None is passed in

    def test_1_item_list(self):
        root = self._generate_list([102])
        remove_duplicates_no_temp_buff(root)
        result = read_linked_list(root)
        expected_result = [102]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

    def test_unique_list(self):
        root = self._generate_list([i for i in range(10)])
        remove_duplicates_no_temp_buff(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

    def test_single_duplicate(self):
        root = self._generate_list([i for i in range(10)] + [0])
        remove_duplicates_no_temp_buff(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        root = self._generate_list([i for i in range(10)] + [0])
        remove_duplicates(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

    def test_single_duplicate_robust(self):
        root = self._generate_list([i for i in range(10)] + [9])
        remove_duplicates_no_temp_buff(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        root = self._generate_list([i for i in range(10)] + [9])
        remove_duplicates(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

    def test_one_value_duplicated(self):
        root = self._generate_list([i for i in range(10)] + [1, 1, 1])
        remove_duplicates_no_temp_buff(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        root = self._generate_list([i for i in range(10)] + [1, 1, 1])
        remove_duplicates(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

    def test_one_value_duplicated_robust(self):
        root = self._generate_list([i for i in range(10)] + [5, 5, 5])
        remove_duplicates_no_temp_buff(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        root = self._generate_list([i for i in range(10)] + [5, 5, 5])
        remove_duplicates(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

    def test_multiple_value_duplicated(self):
        root = self._generate_list([i for i in range(10)] + [1, 2, 2, 5, 5, 5, 8, 8, 8, 8, 8, 9])
        remove_duplicates_no_temp_buff(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

        root = self._generate_list([i for i in range(10)] + [1, 2, 2, 5, 5, 5, 8, 8, 8, 8, 8, 9])
        remove_duplicates(root)
        result = read_linked_list(root)
        expected_result = [i for i in range(10)]
        print("         result: {}".format(result))
        print("expected_result: {}".format(expected_result))
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
