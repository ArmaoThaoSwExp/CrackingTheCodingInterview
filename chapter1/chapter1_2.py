"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""


###############################################################################
# Question 1.2
# Write code to reverse a C-Style string
###############################################################################
def reverse_str(instr):
    for i in range(len(instr) / 2):
        temp = instr[i]
        instr[i] = instr[len(instr) - 1 - i]
        instr[len(instr) - 1 - i] = temp


if __name__ == "__main__":
    print("Cracking the coding interview chapter 1 exercises")

