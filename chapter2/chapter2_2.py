"""
Author: Armao Thao

Description:
    Chapter 2: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 2.2
# Implement an algorithm to find the nth to last element of a singly linked list.
#
# To do this, we have two pointers: one that points to the current location and the other to the
# (current + (nth - 1)) position.
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


def find(node, value):
    assert isinstance(node, Node) or node is None, \
        "Expecting node of type Node or None, but received {}".format(type(node))
    while node is not None:
        if node.value == value:
            return node
        node = node.next
    return None


def find_nth_to_end_element(head, n):
    p1 = head
    p2 = head
    for i in range(n):
        if p2 is None:
            return None  # Not found since p2 hasn't reached nth element distance from p1
        p2 = p2.next

    if p2 is None:
        return p2

    # Loop until p2 reaches the end
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next

    # Since p1 and p2 are nth apart and p2 has reached the end, p1 is the desired value
    return p1


if __name__ == "__main__":
    print("Cracking the coding interview chapter 2 exercises")
