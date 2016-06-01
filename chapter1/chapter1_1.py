"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""


###############################################################################
# Question 1.1
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# The assumption is that the input can be lowercase 'a' - 'z' or convert
# to lowercase if it isn't already lower cased.
###############################################################################
def unique_char_str(instr):
    assert isinstance(instr, str), "instr must be of type string, but received type {0}".format(type(instr))
    char_tracker = 0x00000000
    for each_char in instr:
        if ((char_tracker >> (ord(each_char.lower()) - ord('a')) & 1)):
            return False
        char_tracker |= (1 << (ord(each_char.lower()) - ord('a')))
    return True


def unique_char_str_using_dict(instr):
    assert isinstance(instr, str), "instr must be of type string, but received type {0}".format(type(instr))
    char_tracker = {}
    for char in instr:
        if char in char_tracker:
            return False
        else:
            char_tracker[char] = True
    return True

if __name__ == "__main__":
    print("Cracking the coding interview chapter 1 exercises")
