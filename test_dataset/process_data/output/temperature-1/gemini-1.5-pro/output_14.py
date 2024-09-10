def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
            j += 1
        prefix = prefix[:j]

    return prefix


# test

input1 = ["flower","flow","flight"] 
output1 = "fl"
input2 = ["dog","racecar","car"]
output2 = ""

print({"input 1": str(input1) == str(["flower","flow","flight"]),
        "output 1": str(longestCommonPrefix(input1)) == str(output1),
        "input 2": str(input2) == str(["dog","racecar","car"]),
        "output 2": str(longestCommonPrefix(input2)) == str(output2)
        })