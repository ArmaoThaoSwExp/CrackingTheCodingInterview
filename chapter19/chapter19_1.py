"""
Author: Armao Thao

Description:
    Chapter 19: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 19.1
# Write a function to swap a number in place without temporary variables.
##############################################################################
def swapvars(var1, var2):
    var1 = var1 ^ var2
    var2 = var1 ^ var2
    var1 = var1 ^ var2
    return (var1, var2)


if __name__ == "__main__":
    print("Cracking the coding interview chapter 19 exercises")
