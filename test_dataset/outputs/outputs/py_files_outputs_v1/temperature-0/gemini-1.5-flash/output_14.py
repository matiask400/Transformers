def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example 1
strs1 = ["flower","flow","flight"]
output1 = longestCommonPrefix(strs1)
print(f"Input 1: {strs1}")
print(f"Output 1: {output1}")

# Example 2
strs2 = ["dog","racecar","car"]
output2 = longestCommonPrefix(strs2)
print(f"Input 2: {strs2}")
print(f"Output 2: {output2}")

# Example 3 (Optional)
# strs3 = ["abc", "abcd", "abce"]
# output3 = longestCommonPrefix(strs3)
# print(f"Input 3: {strs3}")
# print(f"Output 3: {output3}")