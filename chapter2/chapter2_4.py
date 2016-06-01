"""
Author: Armao Thao

Description:
    Chapter 2: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 2.4
# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
#
# # Let's assume that the linked lists have the same length
# Example:
# Input: (3->1->5), (5->9->2)
# Output: (8 -> 0 -> 8) because 3+5, 1+9 carry 1, 5+2 plus carry
##############################################################################
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def read_linked_list(node):
    result = []
    while node is not None:
        result.append(node.value)
        node = node.next
    return result


def sum_nodes(node1, node2, carry):
    if node1 is None or node2 is None:
        return None

    result = Node(carry)
    result.value += node1.value
    result.value += node2.value

    carry = 0
    if result.value >= 10:
        carry = 1
    result.value %= 10

    result.next = sum_nodes(node1.next, node2.next, carry=carry)
    return result


if __name__ == "__main__":
    print("Cracking the coding interview chapter 2 exercises")
