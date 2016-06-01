"""
Author: Armao Thao

Description:
    Chapter 5: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 8.5
# Implement an algorithm to print all valid
# (e.g., properly opened and closed) combinations of n-pairs of parenthesis.
##############################################################################
def wellparenthesized(count):
    tracker = ["" for i in range(count * 2)]
    _wellparenthesized(left=count, right=count, tracker=tracker, count=0)

printcount = 0
def _wellparenthesized(left, right, tracker, count):
    global printcount
    if left < 0 or right < left:
        return  # Invalid state if left runs out or there are more rights than left brackets

    if left == 0 and right == 0:
        print("[" + str(printcount) + "]" + str(tracker))  # Found a well parenthesized expression
        printcount += 1
    else:
        if left > 0:
            tracker[count] = "("
            _wellparenthesized(left - 1, right, tracker=tracker, count=count+1)
        if right > 0:
            tracker[count] = ")"
            _wellparenthesized(left, right - 1, tracker=tracker, count=count+1)


if __name__ == "__main__":
    print("Cracking the coding interview chapter 5 exercises")
