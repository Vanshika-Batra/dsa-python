# Problem: Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
# The number returned should not have leading zero's. But the given input string may have leading zero.

# link: https://takeuforward.org/data-structure/largest-odd-number-in-a-string

def remove_leading_zeroes(no):
    for index in range(len(no)):
        if no[index]!='0':
            return no[index::]
    return ""

def find_largest_odd(no):
    no = remove_leading_zeroes(no)
    print("no after removing zeros: ", no)
    for index in range(len(no)-1, -1, -1):
        print("no[index: ]", no[index], type(no[index]))
        print("int(no[index]): ", int(no[index]), type(int(no[index])))
        if no[index] in '1359':
            return no[0: index+1]
    return "None"


def find_largest_odd_no_in_one_go(no):
    i, j,k  = 0, len(no)-1, 0
    while i< len(no) and j >= 0 and k <= len(no):
        if no[i]=='0':
            i +=1
        if int(no[j]) %2 ==0:
            j -=1
        k+=1
    if i<=j:
        return no[i:j+1]
    return None

no = "98724152"
# no = "00000001"
# no = "0000202"
# print(find_largest_odd(no))
print(find_largest_odd_no_in_one_go(no))
