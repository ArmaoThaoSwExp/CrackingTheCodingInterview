"""
Author: Armao Thao

Description:
    Chapter 5: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 5.2
# Given a (decimal - e.g. 3.72) number that is passed in as a string,
# print the binary representation. If the number can not be represented
# accurately in binary, print "Error"
##############################################################################
def printbin(instr):
    intpart = int(instr.split(".")[0])
    decpart = float("." + instr.split(".")[1])
    int_str = ""
    while intpart:
        if intpart % 2:
            int_str += "1"
        else:
            int_str += "0"
        intpart >>= 1

    dec_str = ""
    while decpart > 0:
        if len(dec_str) > 32:
            return "Error"
        if decpart == 1:
            dec_str += "1"
            break

        r = decpart * 2
        if r >= 1:
            dec_str += "1"
            decpart = r - 1
        else:
            dec_str += "0"
            decpart = r
    return int_str + "." + dec_str


if __name__ == "__main__":
    print("Cracking the coding interview chapter 5 exercises")
