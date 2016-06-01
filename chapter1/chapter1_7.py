"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 1.7
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
#
# We have to do two separate loops because if started settings rows and columns to zero on the first pass,
# pretty soon, we would have nothing but 0s.
# The idea is to mark all the rows and columns with 0s.  Then do a second pass and set each item equal to one or zero.
##############################################################################
def zero_row_and_col(matrix):
    zero_row = []
    zero_col = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                zero_row.append(row)
                zero_col.append(col)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in zero_row or col in zero_col:
                matrix[row][col] = 0


if __name__ == "__main__":
    print("Cracking the coding interview chapter 1 exercises")



























