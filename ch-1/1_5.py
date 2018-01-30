"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2b1c5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.

"""

"""
aabcccccaaa  = a2b1c5a3 = [  [a, a],
                             [b], 
                             [c, c, c, c, c]
                             [a, a, a]
                           ]

"""

def str_compress_1(word):
    letters = []
    for i in word:
        if 




#Incomplete
def str_compress_2(word):
    compressed = []
    count = 1
    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            if count == 1:
                compressed.append(word[i])
            count = count + 1
        else:
            compressed.append(str(count))
            count = 1
            compressed.append(word[i])

    compressed_str = ''.join(compressed)
    if len(compressed_str) >= len(word):
        return word

    return compressed_str


if __name__ == "__main__":
    word = str(raw_input("Input word: ")).lower()
    print str_compress(word)