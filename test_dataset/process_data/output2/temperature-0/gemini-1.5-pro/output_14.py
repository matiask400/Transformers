def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest


input_1 = ["flower", "flow", "flight"]
output_1 = "fl"
input_2 = ["dog", "racecar", "car"]
output_2 = ""

print(longestCommonPrefix(input_1) == output_1)
print(longestCommonPrefix(input_2) == output_2)