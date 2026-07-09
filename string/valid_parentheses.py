# Problem: A valid parentheses string is defined by the following rules:

# It is the empty string "".
# If A is a valid parentheses string, then so is "(" + A + ")".
# If A and B are valid parentheses strings, then A + B is also valid.

# A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.
# Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return the resulting string.

# url: https://takeuforward.org/data-structure/remove-outermost-parentheses


def remove_outermost_parantheses(s):
    paranthesis_count = 0
    start_brace_index = end_brace_index = 0
    result=[]
    for index in range(len(s)):
        # if start<=end
        print("letter: ", s[index], "index: ", index)
        if s[index]=='(':
            print("in open")
            if paranthesis_count ==0: 
                start = index
            paranthesis_count +=1
        else:
            print("in close")
            paranthesis_count -=1
            if paranthesis_count == 0:
                end = index
                if start + 1 < end -1:
                    result.append(s[start +1: end])

    return "".join(result)
# s = ""
# s = "((()))"
# s = "()()()(())"
s = "(()())((()))"
print(remove_outermost_parantheses(s))


#COMPLEXITY
TIME - O(N)
SPACE - O(N)    #list of length N, and a new string is being returned
