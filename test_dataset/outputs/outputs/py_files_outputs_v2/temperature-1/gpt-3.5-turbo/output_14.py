def longestCommonPrefix(strs):
    if not strs:
        return ""
    min_len = min([len(s) for s in strs])
    prefix = ""
    for i in range(min_len):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    return prefix

# Test the solution with example inputs
input1 = ["flower","flow","flight"]
output1 = longestCommonPrefix(input1)
print(output1 == "fl")

input2 = ["dog","racecar","car"]
output2 = longestCommonPrefix(input2)
print(output2 == "")
