# Problem: find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
#example: str = ["flower", "flow", "flight"], Output: "fl"

# link: https://takeuforward.org/data-structure/longest-common-prefix

def longest_common_prefix(strings):
    strings.sort()
    last_element = strings[len(strings)-1]
    first_element = strings[0]
    for index in range(min(len(first_element), len(last_element))):
        if first_element[index] != last_element[index]:
            if index == 0:
                return ""
            return first_element[:index]

# strings = ["flower", "flow", "flight"]
strings = ["pen", "paper", "eraser"]
print(longest_common_prefix(strings))