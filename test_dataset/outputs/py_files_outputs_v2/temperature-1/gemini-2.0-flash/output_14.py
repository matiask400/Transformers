def longestCommonPrefix(strs):
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string `""`.
    """
    if not strs:
        return ""
    
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix