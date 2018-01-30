"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

Richa --> True 
Apple --> False
Dud --> False

"""


# 1 way is to sort the string and then compare the items next to each other

def unique_chars_1(word):
    sorted_word = sorted(word)
    l =  len(sorted_word)
    i = 0
    while i < l - 1:
        if sorted_word[i] == sorted_word[i+1]:
            return False
        i = i + 1

    return True


# 2 way is to compare the length of the two string where one is as is, and the second is a set. Set is a list of unique elements in the given list.


def unique_chars_2(word):
    if len(word) == len(set(word)):
        return True
    return False

# 3 for each given letter check if the count of that is > 1.

def unique_chars_3(word):
    for i in word:
        if word.count(i) > 1:
            return False

    return True


if __name__ == "__main__":
    word = str(raw_input("Input the word: ")).lower()
    print "unique_chars_1 ==> ", unique_chars_1(word)
    print "unique_chars_2 ==> ", unique_chars_2(word)
    print "unique_chars_3 ==> ", unique_chars_3(word)







