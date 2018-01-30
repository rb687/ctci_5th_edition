"""
Write a method to replace all spaces in a string with'%20'. You may assume that
the string has sufficient space at the end of the string to hold the additional
characters, and that you are given the "true" length of the string. (Note: if implementing
in Java, please use a character array so that you can perform this operation
in place.)
EXAMPLE
Input: "Mr John Smith"
Output: "Mr%20Dohn%20Smith"

"""

def replace_str_1(word):
    len_word = len(word)
    replaced_word = []
    for i in range(0, len_word):
        if word[i] == ' ':
            replaced_word.append("%20")
        else:
            replaced_word.append(word[i])

    return ''.join(replaced_word)


def replace_str_2(s):
    return '%20'.join(s.split())

def replace_str_3(string, size):
    return string[:size].replace(' ', '%20')


if __name__ == "__main__":
    word = str(raw_input("Input the word: ")).lower()
    print "Word is ==> ", replace_str_1(word)