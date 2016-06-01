"""
Author: Armao Thao

Description:
    Chapter 5: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 5.1
#
# You are given two 32-bit numbers, N and M, and two bit positions, i and j.
# Write a method to set all bits between i and j in N equal to M.
# (e.g., M becomes a substring of N located at i and starting at j).
# EXAMPLE:
# Input: N = 10000000000, M = 10101, i = 2, j = 6
# Output: N = 10001010100
##############################################################################
def setbits(n, m, i, j):
    # For the purpose of this exercise, let's assume that n is of size unsigned int 32
    mask = ((0xFFFFFFFF << j) & 0xFFFFFFFF) | (0xFFFFFFFF >> (32 - i))
    result = (n & mask) | (m << i)
    return result


if __name__ == "__main__":
    print("Cracking the coding interview chapter 5 exercises")
