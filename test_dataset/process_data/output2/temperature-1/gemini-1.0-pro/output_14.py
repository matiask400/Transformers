def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other_str in strs:
            if other_str[i] != char:
                return shortest_str[:i]
    return shortest_str

# Example 1
input_1 = ["flower","flow","flight"]
output_1 = longestCommonPrefix(input_1)
print(output_1 == "fl")

# Example 2
input_2 = ["dog","racecar","car"]
output_2 = longestCommonPrefix(input_2)
print(output_2 == "")