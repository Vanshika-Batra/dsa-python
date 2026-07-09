# Problem: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. 
# Return a string with the words in reverse order, concatenated by a single space.

def reverse_words(s):
    length = len(s)
    result = []
    for index in range(length):
        index = length -1 - index
        if s[index] == ' ':
            continue
        else:
            if (index == length -1) or s[index + 1] == ' ':
                end = index
            if index == 0 or s[index -1 ] == ' ':
                start = index
                if start <= end:
                    result.append(s[start: end+1])
    return " ".join(result)

s = "   wolf    is in the woods     "
# s = "    "
# s = "r  "
# s = "   hey"
output = reverse_words(s)
print("reversed words: ",output , "length: ", len(output))


# #COMPLEXITY: 
# TIME: O(N)      # traverse whole string
# SPACE: O(N)     #list of the s