# Problem: Given two strings, check if two strings are anagrams of each other or not.
# Example: 
# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.


# link: https://takeuforward.org/data-structure/check-if-two-strings-are-anagrams-of-each-other

def is_anagram_by_sorting(s, t):
    if len(s) != len(t):
        return False
    if sorted(s) == sorted(t):
        return True
    return False

def is_anagram_by_freq(s, t):
    if len(s) != len(t):
        return False
    mapping = {}
    for i in range(len(s)):
        mapping[s[i]] = mapping.get(s[i], 0) + 1
        mapping[t[i]] = mapping.get(t[i], 0) -1
    
    for values in mapping.values():
        if values !=0:
            return False
    return True


def is_anagram_by_fixed_freq_map(s, t):
    freq = [0]*26   # fixed frequency array to store character counts - 26 alphabets
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 0
        freq[ord(t[i]) - ord ('a')] -=0
    for i in freq:
        if i != 0:
            return False
    return True


# s, t = 'act', 'tac'
s, t = 'govindaa', 'aoginadva'
print(is_anagram_by_sorting(s, t))
print(is_anagram_by_freq(s, t))
print(is_anagram_by_fixed_freq_map(s, t))


# COMPLEXITIES:
# 1) BY SORTING:
# TIME: O(N log N), where N is the length of the strings. This is due to the sorting step performed on both strings.
# SPACE: O(1), as the sorting is done in-place and no extra space proportional to input size is used

# 2) BY DICT/MAP:
# TIME: O(N)
# SPACE: O(N)

# 3) BY FIXED SIZE MAP:
# TIME: O(N) where N is the length of the strings. Each string is traversed once, and the frequency array is checked in constant time (26 iterations).
# SPACE: O(1) as a fixed-size array of 26 elements is used regardless of the input size.