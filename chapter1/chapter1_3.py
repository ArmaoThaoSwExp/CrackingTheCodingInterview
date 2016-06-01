"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""


###############################################################################
# Question 1.3
# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer.  NOTE: One or two additional variables are fine.
# An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.
# Note: because of how python handles memory, I'm returning the string
#   instead of deleting items from the array or putting in a null pointer.
###############################################################################
def remove_duplicates_in_str(instr):
    # Note that for the purpose of this exercise, we are making instr a c-style str
    assert isinstance(instr, list), "expected instr to be of type list, but received type {0}".format(type(instr))
    if instr is [] or len(instr) == 1:
        return instr
    tail = 1
    for i in range(1, len(instr)):
        if instr[i] not in instr[:tail]:
            instr[tail] = instr[i]
            tail += 1
    return instr[:tail]


def remove_duplicates_in_str_cstyle(instr):
    assert isinstance(instr, list), "expected instr to be of type list, but received type {0}".format(type(instr))
    if len(instr) <= 1:
        return instr
    tail = 1
    for i in range(1, len(instr)):
        duplicate = False
        for j in range(0, tail):
            if instr[i] == instr[j]:
                duplicate = True
                break
        if not duplicate:
            instr[tail] = instr[i]
            tail += 1
    return instr[:tail]


def remove_duplicates_additional_buffer(instr):
    assert isinstance(instr, list), "expected instr to be of type list, but received type {0}".format(type(instr))
    if len(instr) <= 1:
        return instr
    duplicate = {instr[0]: 1}
    resultind = 1  # Results index
    for i in range(1, len(instr)):
        if instr[i] not in duplicate:
            duplicate[instr[i]] = 1
            instr[resultind] = instr[i]
            resultind += 1
    return instr[:resultind]


if __name__ == "__main__":
    print("Cracking the coding interview chapter 1 exercises")

