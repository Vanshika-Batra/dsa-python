# Problem: The beauty of a string is defined as the difference between the frequency of the most frequent character and the least frequent character (excluding characters that do not appear) in that string.
# Given a string s, return the sum of beauty values of all possible substrings of s.

# link: https://takeuforward.org/data-structure/sum-of-beauty-of-all-substring

def total_beautiful_strings(input_string):
    total = 0
    for i in range(len(input_string)):
        freq = {}

        for j in range(i, len(input_string)):
            freq[input_string[j]] = freq.get(input_string[j],0 ) + 1

            values = freq.values()
            total += (max(values) - min(values))
    return total

# s = 'xyx'
# s = 'aabcbaa'
s = 'abcab'
print("Total beautiful strings: ", total_beautiful_strings(s))


# #COMPLEXITIES
# TIME: O(N^2 * D),  where D is the number of distinct characters is the current substring
# SPACE: O(D), in the worst case D = N 



# ## OPTIMIZED
# USE FIXED SIZE OF ARRAY FOR 26 CHARACTERS IN PLACE OF UNKNOWN SIZED DICTIONARY (freq) - ONLY FOR KNOWN CHARACTERS (lowercase/uppercase/digits and not unicode etc)


print("secondddd")
def total_beautiful_strings_with_array(s):
    n = len(s)
    result = 0

    for index in range(n):
        freq = [0]*26
        for i in range(index, n):
            freq[ord(s[i]) - ord('a')] += 1
            
            minimum = float('inf')
            maximum = 0
            for f in freq:
                if f:
                    maximum = max(maximum, f)
                    minimum = min(minimum, f)
            result += (maximum - minimum)
    return result

print("Total beautiful strings: ", total_beautiful_strings_with_array(s))


# # COMPLEXITIES
# TIME:   O(N^2 * 26) ~~ O(N^2) because max and min functions take O(N) if they are given the whole array to find min and max. But, the comparison operation is O(!)   
# SPACE:  O(26) ~~ O(1) -constant space