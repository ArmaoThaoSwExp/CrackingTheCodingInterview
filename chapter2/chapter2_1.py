"""
Author: Armao Thao

Description:
    Chapter 2: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 2.1
# Write code to remove duplicates from an unsorted linked list.
#
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
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


def remove_duplicates(node):
    nodetracker = {}
    previous = None
    while node is not None:
        if node.value in nodetracker:
            previous.next = node.next
        else:
            nodetracker[node.value] = 1
            previous = node
        node = node.next


def remove_duplicates_no_temp_buff(head):
    runner = None
    previous = None
    current = head
    while current is not None:
        runner = head
        duplicate = False
        while runner != current:
            if runner.value == current.value:
                previous.next = current.next
                duplicate = True
                break
            runner = runner.next
        if not duplicate:
            previous = current
        current = current.next


if __name__ == "__main__":
    print("Cracking the coding interview chapter 2 exercises")
