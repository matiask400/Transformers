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


# Test cases
input1 = ["flower", "flow", "flight"]
output1 = "fl"
result1 = longestCommonPrefix(input1) == output1

input2 = ["dog", "racecar", "car"]
output2 = ""
result2 = longestCommonPrefix(input2) == output2

print({"Input 1": input1, "Output 1": output1, "Result 1": result1, "Input 2": input2, "Output 2": output2, "Result 2": result2})