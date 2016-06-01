"""
Author: Armao Thao

Description:
    Chapter 19: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 19.5
# Write a method that, given a guess and a solution, returns the number
# of hits and pseudo hits.
##############################################################################
def mastermind_guess(guess, solution):
    hits = 0
    pseudohits = 0
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            hits += 1
        elif guess[i] in solution:
            pseudohits += 1
    return (hits, pseudohits)


if __name__ == "__main__":
    print("Cracking the coding interview chapter 19 exercises")
