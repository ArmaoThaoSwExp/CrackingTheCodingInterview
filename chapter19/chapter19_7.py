"""
Author: Armao Thao

Description:
    Chapter 19: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 19.5
# You are given an array of integers (both positive and negative).
# Find the continuous sequence with the largest sum.  Return the sum.
#
# EXAMPLE
# Input: {2, -8, 3, -2, 4, -10}
# Output: 5 (i.e., {3, -2, 4})
##############################################################################
def contsum(arr):
    assert isinstance(arr, list) and arr, "Expected arr to be of type list and not empty, but received {0}".format(arr)
    maxsum = 0
    sum = 0
    for val in arr:
        sum += val
        if sum > maxsum:
            maxsum = sum
        elif sum < 0:
            sum = 0
    return maxsum


if __name__ == "__main__":
    print("Cracking the coding interview chapter 19 exercises")
