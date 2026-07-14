# Problem Statement: Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer (similar to the C/C++ atoi function).

# Steps to Implement: 1. First, ignore any leading whitespace characters ' ' until the first non-whitespace character is found.
# 2. Check the next character to determine the sign. If it’s a '-', the number should be negative. If it’s a '+', the number should be positive. If neither is found, assume the number is positive.
# 3. Read the digits and convert them into a number. Stop reading once a non-digit character is encountered or the end of the string is reached. Leading zeros should be ignored during conversion.
# 4. The result should be clamped within the 32-bit signed integer range: [-2147483648, 2147483647]. If the computed number is outside this range, return -2147483648 if the number is less than -2147483648, or return 2147483647 if the number is greater than 2147483647.
# 5. Finally, return the computed number after applying all the above steps.


# link: https://takeuforward.org/data-structure/recursive-implementation-of-atoi


def my_atoi(s):
    maximum = 2147483647
    minimum = -2147483648

    i = 0
    n = len(s)
    while i < n and s[i] == ' ':
        i += 1
    sign = 1

    if i < n and s[i] in ('+', '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    result = 0
    while i < n and s[i].isdigit():     # checks if the character is a digit -> 0, 1, 2,3,4,5,6,7,8,9
        digit = ord(s[i]) - ord('0')    # convert character to the integer
        if result > maximum // 10 or (      # if the result is: 214748364, then 2147483647 > 2147483647 is false, but the 2nd codition checks if the current digit
                                        # is < 7 so when result *10+ digit is done then it should not exceed the MAXIMUM number. Similar is for the negative case
            result == maximum // 10 and digit > (7 if sign == 1 else 8)
        ):
            return maximum if sign == 1 else minimum
        result = result * 10 + digit

        i += 1
    return sign * result



# string = " -12345" 
# string = "4193 with words" 
# string = " 2147483649   "
string = '+-124' 
print("integer conversion: ", atoi(string))

# #COMPLEXITITES
# TIME:  O(N)
# SPACE:  O(N)