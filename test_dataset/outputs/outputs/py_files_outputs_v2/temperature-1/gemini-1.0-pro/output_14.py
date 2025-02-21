def longestCommonPrefix(strs):
    """ Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """
    if not strs:
        return ""
    shortest_str = min(strs, key=len)

    for i, ch in enumerate(shortest_str):
        for other_str in strs:
            if other_str[i] != ch:
                return shortest_str[:i]
    return shortest_str

print(longestCommonPrefix(["flower","flow","flight"]) == "fl")  # True
print(longestCommonPrefix(["dog","racecar","car"]) == "")  # True
print(longestCommonPrefix(["a"]) == "a")  # True
