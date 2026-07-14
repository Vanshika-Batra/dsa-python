# Problem Statement: Roman numerals are represented by seven different symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# For example: 2 is written as II, 12 is written as XII, 27 is written as XXVII.
# Roman numerals are usually written largest to smallest from left to right. But in six special cases, subtraction is used instead of addition:
# I before V or X → 4 and 9,
# X before L or C → 40 and 90,
# C before D or M → 400 and 900
# Given a Roman numeral, convert it to an integer.


# link: https://takeuforward.org/data-structure/roman-numerals-to-integer


def roman_to_int(roman):
    roman_int_map = {'I':1, 'X':10, 'V':5, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    index = 0
    for index in range(len(roman)):
        if index +1 != len(roman) and roman_int_map[roman[index]] < roman_int_map[roman[index+1]]:
                integer -= roman_int_map[roman[index]]
        else:
            integer += roman_int_map[roman[index]]
    return integer


# roman_numeral = 'XL'
# roman_numeral = 'XLV'
roman_numeral = 'MCMXCIV'
# roman_numeral = 'LVIII'
print("resulting integer number: ", roman_to_int(roman_numeral))


# #COMPLEXITIES
# SPACE:  O(1)
# TIME:   O(N)