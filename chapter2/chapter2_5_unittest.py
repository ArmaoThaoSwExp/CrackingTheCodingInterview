"""
Author: Armao Thao

Description:
    Chapter 2: cracking the coding interview
"""

import unittest
from chapter2_5 import Node, find_circular_node


class TestUniqueCharStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _generate_list(self, values):
        root = Node(values[0])
        current = root
        for value in values[1:]:
            current.nextnode = Node(value)
            current = current.nextnode
        return root

    def _generate_duplicate(self, llist, duplicate_value):
        duplicate_node = None
        while llist.nextnode:
            if llist.value == duplicate_value:
                duplicate_node = llist
            llist = llist.nextnode
        llist.nextnode = duplicate_node
        return duplicate_node

    def test_simple_addition(self):
        llist = self._generate_list([1, 2, 3, 4, 5, 6, 7])
        expected_result = self._generate_duplicate(llist, 4)
        result = find_circular_node(llist)
        self.assertEqual(result, expected_result)

    def test_simple_addition(self):
        llist = self._generate_list([101, 150, 456465, 123, 64564, 897, 4654, 1321, 45645897, 9877878, 4545])
        expected_result = self._generate_duplicate(llist, 456465)
        result = find_circular_node(llist)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
