"""
Author: Armao Thao

Description:
    Chapter 2: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 2.5
# Given a circular linked list, implement an algorithm which returns the node at the beginning
# of the loop.
#
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
# so as to make a loop in the linked list.
#
# Example
# Input: A->B->C->D->E->C [the same as C as earlier]
# Output: C
##############################################################################
class Node(object):
    def __init__(self, value, nextnode=None):
        self.value = value
        self.nextnode = nextnode


def find_circular_node(node):
    assert isinstance(node, Node) or node is None, \
        "Expecting node of type Node or None, but received {}".format(type(node))
    if node is None or node.nextnode is None:
        return node
    tortoise = node
    hare = node

    while hare.nextnode is not None:
        tortoise = tortoise.nextnode
        hare = hare.nextnode.nextnode
        if tortoise == hare:
            break

    if hare.nextnode is None:
        return None  # No meeting point

    tortoise = node
    while tortoise != hare:
        tortoise = tortoise.nextnode
        hare = hare.nextnode

    return hare


if __name__ == "__main__":
    print("Cracking the coding interview chapter 2 exercises")
