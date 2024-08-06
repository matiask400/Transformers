def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
            j += 1
        prefix = prefix[:j]
        if not prefix:
            return ""
    return prefix


input1 = ["flower","flow","flight"]
output1 = "fl"
print(f"Input 1: {input1}, Output: {output1 == longestCommonPrefix(input1)}")

input2 = ["dog","racecar","car"]
output2 = ""
print(f"Input 2: {input2}, Output: {output2 == longestCommonPrefix(input2)}")