def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    return shortest_str

strs1 = ["flower","flow","flight"]
output1 = "fl"
print(longest_common_prefix(strs1) == output1)

strs2 = ["dog","racecar","car"]
output2 = ""
print(longest_common_prefix(strs2) == output2)