"""
Author: Armao Thao

Description:
    Chapter 20: cracking the coding interview
"""


##############################################################################
# Cracking the coding exercise Chapter 20.10
# Given two words of equal length that are in a dictionary, write a method
# to transform one word into another word by changing only one letter at a time.
# The new word you get in each step must be in the dictionary.
#
# All words are assumed to be capitalized in this case.
##############################################################################
def find_link_words(startword, stopword, wordsdict):
    action = [startword]
    visited = [startword]

    while action:
        word = action.pop(0)
        posswords = possiblewords(word)
        for eachword in posswords:
            if eachword == stopword:
                visited.append(eachword)
                return visited[:]
            else:
                if eachword in wordsdict and eachword not in visited:
                    action.append(eachword)
                    visited.append(eachword)
    return []  # Return empty list to indicate no path was possible from startword to endword


def possiblewords(word):
    result = []
    for i in range(len(word)):
        temp = [char for char in word]
        for j in range(ord('A'), ord('Z')):
            newchar = chr(j)
            if newchar != temp[i]:
                temp[i] = newchar
                result.append("".join(temp))
    return result



# def find_link_words(startword, stopword, wordsdict):
#     action = [startword]
#     visited = [startword]
#     tracker = {}
#     while action:
#         word = action.pop(0)
#         for possword in possiblewords(word):
#             if possword == stopword:
#                 visited.append(possword)
#                 return visited
#             if possword in wordsdict:
#                 if possword not in visited:
#                     visited.append(possword)
#                     action.append(possword)
#                     tracker[possword] = word
#     return []  # Not possible
#
# def possiblewords(word):
#     result = []
#     for i in range(len(word)):
#         tempword = [char for char in word]
#         for j in range(ord('A'), ord('Z')):
#             newchar = chr(j)
#             if newchar != tempword[i]:
#                 tempword[i] = newchar
#                 result.append("".join(tempword))
#     return result


if __name__ == "__main__":
    print("Cracking the coding interview chapter 20 exercises")
