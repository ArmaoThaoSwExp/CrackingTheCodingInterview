"""
Author: Armao Thao

Description:
    Chapter 1: cracking the coding interview
"""


###############################################################################
# Question 1.5
# Write a method to replace all spaces in a string with '%20'
###############################################################################
def replace_space_with_percent20(instr):
    return "%20".join(instr.split(" "))


def replace_space_with_percent20_cstyle(instr):
    assert isinstance(instr, list), "Expected type list for instr, but received {0}".format(type(instr))
    orig_len = len(instr)
    space_cnt = instr.count(" ")

    # Create additional buffer space for '%20', since an empty char means we have 1 space,
    # we only need to allocate 2 more char space for each space char we found.
    instr += ["" for i in range(space_cnt * 2)]

    ind = len(instr) - 1
    # To replace the spaces with '%20', we need to work backwards in our string with the
    # additional allocated buffer space.
    for i in range((orig_len - 1), -1, -1):
        if instr[i] == " ":
            # If space is found, replace the space with %20 in the instr at its new location
            instr[ind-2:ind+1] = ["%", "2", "0"]
            ind -= 3
        else:
            # If space is not found, copy the char to its new location
            instr[ind] = instr[i]
            ind -= 1
    return instr


if __name__ == "__main__":
    print("Cracking the coding interview chapter 1 exercises")

