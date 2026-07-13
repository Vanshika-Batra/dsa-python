# # Problem: Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# # A shift on s consists of moving the leftmost character of s to the rightmost position. 
# # For example, if s = "abcde", then it will be "bcdea" after one shift.

# # link: https://takeuforward.org/data-structure/check-if-one-string-is-rotation-of-another


def is_rotated(original, rotated):
    s = original + original
    return rotated in s

# goal = "rotation"
# input_str = "tionrota"
goal, input_str = 'aaaba', 'aabaa'
print(is_rotated(goal, input_str))

# #COMPLEXITIES
# TIME: O(N)
# SPACE: O(1)


## MY SOLUTION WILL NOT WORK FOR THE CASES WHEN THERE ARE MULTIPLE CHARACTERS THAT ARE SAME, AND IF THERE CAN BE MULTIPLE OPTIONS OF STRING ROTATION
## EX: original= aaab, rotated can be: abaa, aaba, abaa, baaa
## my solution will return false in the case of aaba.

# def is_rotated(original, rotated):
#     print("originaL: ", original, "rotated: ", rotated, len(rotated))
#     if len(rotated) != len(original):
#         return False
#     initial_index = -1
#     parsed_index = 0
#     if original == rotated:
#         return True

#     for i in range(len(rotated)):
#         if initial_index == -1 and original[parsed_index] == rotated[i]:
#             initial_index = i
#             parsed_index += 1
#         else:
#             if original[parsed_index] != rotated[i]:
#                 parsed_index = 0
#                 initial_index = -1
#             else:
#                 parsed_index += 1
    
#     print("rotated: ", rotated, len(rotated))
#     if parsed_index <len(rotated) and original[parsed_index:] == rotated[:initial_index]:
#         return True
#     return False


# # s, t = "rotated", "tetrota"
# s, t  = 'aaaba', 'aabaa'
# print(is_rotated(s, t))


# # COMPLEXITIES
# TIME: O(N^2)
# SPACE: O(1)
