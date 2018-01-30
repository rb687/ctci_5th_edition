"""
Given two strings, write a method to decide if one is a permutation of the other.


Return True, if they are permutation of each other else false
"""

# 1 sort the two strings and compare letter by letter

def permutation_1(word_1, word_2):
    if len(word_1) != len(word_2):
        return False

    sorted_word_1 = sorted(word_1)
    sorted_word_2 = sorted(word_2)

    if sorted_word_1 != sorted_word_2:
        return False

    return True


if __name__ == "__main__":
    word_1 = str(raw_input("Input 1st word: ")).lower()
    word_2 = str(raw_input("Input 2nd word: ")).lower()
    print "permutation_1 ==> ", permutation_1(word_1, word_2)