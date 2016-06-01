"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""


###############################################################################
# Question 1.4
# Write a method to decide if two strings are anagrams or not.
###############################################################################
def anagrams_sort(instr1, instr2):
    return True if sorted(instr1) == sorted(instr2) else False


def anagrams_count(instr1, instr2):
    instr1_chars = {}
    instr2_chars = {}

    # Count occurrence of each char in instr1
    for item in instr1:
        if item in instr1_chars:
            instr1_chars[item] += 1
        else:
            instr1_chars[item] = 1

    # Count occurrence of each char in instr2
    for item in instr2:
        if item in instr2_chars:
            instr2_chars[item] += 1
        else:
            instr2_chars[item] = 1

    # There must be the same number of unique chars in instr1 as in instr2,
    # and also the number of occurence of each unique char must match between the two input strings.
    for item in instr1_chars:
        if (item not in instr2_chars) or (instr1_chars[item] != instr2_chars[item]):
            return False
    return True


if __name__ == "__main__":
    print("Cracking the coding interview chapter 1 exercises")

