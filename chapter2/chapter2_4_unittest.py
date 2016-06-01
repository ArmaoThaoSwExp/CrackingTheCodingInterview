"""
Author: Armao Thao

Description:
    Chapter 2: cracking the coding interview
"""

import unittest
from chapter2_4 import Node, sum_nodes, read_linked_list


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

    def test_simple_addition(self):
        list1 = self._generate_list([3, 1, 5])
        list2 = self._generate_list([5, 9, 2])
        sumlist = sum_nodes(list1, list2, carry=0)
        result = read_linked_list(sumlist)
        self.assertEqual(result, [8, 0, 8])

    def test_simple_addition(self):
        list1 = self._generate_list([9, 0, 9, 0, 0, 0, 9, 0, 9, 0, 1, 0, 1, 0])
        list2 = self._generate_list([0, 0, 1, 0, 9, 0, 2, 0, 9, 0, 0, 0, 1, 1])
        sumlist = sum_nodes(list1, list2, carry=0)
        result = read_linked_list(sumlist)
        self.assertEqual(result, [9, 0, 0, 1, 9, 0, 1, 1, 8, 1, 1, 0, 2, 1])


if __name__ == "__main__":
    unittest.main()
