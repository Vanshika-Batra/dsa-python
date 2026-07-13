# Problem: Given two strings s and t, determine if they are isomorphic. 
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.


# Example: 
# Input:
#  s = "paper", t = "title"
# Output:
#  true

# Input:
#  s = "foo", t = "bar"
# Output:
#  false

# link: https://takeuforward.org/data-structure/isomorphic-string


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    forward = {}
    backward = {}
    for c1, c2 in zip(s, t):
        if c1 in forward:
            if forward[c1] != c2:
                return False
        elif c2 in backward:
            return False
        else:
            forward[c1] = c2
            backward[c2] = c1
    return True

# s = 'ab'
# t = 'aa'
s, t = 'paper', 'title'
# s, t = 'nihaal', 'prabhu'
print(is_isomorphic(s,t))


# #COMPLEXITIES
# TIME: O(N)  # Iterate whole string once
# SPACE: O(K) # where K is the unique combinations. In worst case, when all characters mapping are diff then O(N), k =n