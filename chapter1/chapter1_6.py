"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""


###############################################################################
# Question 1.6
# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees.  CAn you do this in place?
#
# Rotate corner, rotate item at corner + 1, corner + 2, all to the end for top layer/outer shell.
# Go down each layer, and repeat until layer n - 1 - layer
###############################################################################
def matrix_print(matrix, justify_space_for_each_value=4):
    n_len = len(matrix)
    for row in matrix:
        print(str([str(item).rjust(justify_space_for_each_value) for item in row]))


# def rotate_n_by_n_matrix_90deg(matrix):
#     for layer in range(int(len(matrix) / 2)):
#         last = (len(matrix) - 1 - layer)
#         for i in range(layer, last):
#             print("Matrix before")
#             matrix_print(matrix)
#             offset = i - layer
#             top = matrix[layer][i]
#
#             # Move left to top
#             matrix[layer][i] = matrix[last - offset][layer]
#
#             # Move bottom to left
#             matrix[last - offset][layer] = matrix[last][last - offset]
#
#             # Move right to bottom
#             matrix[last][last - offset] = matrix[i][last]
#
#             # Move top to right
#             matrix[i][last] = top
#
#             print("")
#             print("Matrix after")
#             matrix_print(matrix)

def rotate_n_by_n_matrix_90deg(matrix):
    for layer in range(len(matrix) / 2):
        last = len(matrix) - 1 - layer
        for i in range(layer, last):
            print("")
            print("Matrix Before")
            matrix_print(matrix)

            # Calculate offset
            offset = i - layer

            # Save top left
            top_left = matrix[layer][i]

            # Set top left = bottom left
            matrix[layer][i] = matrix[last - offset][layer]

            # Set bottom left = bottom right
            matrix[last - offset][layer] = matrix[last][last - offset]

            # Set bottom right = top right
            matrix[last][last - offset] = matrix[i][last]

            # Set top right = top left
            matrix[i][last] = top_left

            print("")
            print("Matrix After")
            matrix_print(matrix)

if __name__ == "__main__":
    print("Cracking the coding interview chapter 1 exercises")



























