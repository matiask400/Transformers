def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other_str in strs:
            if other_str[i] != char:
                return shortest_str[:i]
    return shortest_str


input1 = ["flower","flow","flight"]
output1 = longestCommonPrefix(input1)
print(output1 == "fl")  # True

input2 = ["dog","racecar","car"]
output2 = longestCommonPrefix(input2)
print(output2 == "")  # True