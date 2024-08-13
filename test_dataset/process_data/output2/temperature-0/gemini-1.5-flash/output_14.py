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
strs_1 = ["flower","flow","flight"]
output_1 = longestCommonPrefix(strs_1)
print(f"Example 1: {output_1 == 'fl'}")

# Example 2
strs_2 = ["dog","racecar","car"]
output_2 = longestCommonPrefix(strs_2)
print(f"Example 2: {output_2 == ''}")

# Example 3 (No third example provided)
# strs_3 = ...
# output_3 = longestCommonPrefix(strs_3)
# print(f"Example 3: {output_3 == ...}")