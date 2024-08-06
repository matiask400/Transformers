def longestCommonPrefix(strs):
    prefix = ""
    if len(strs) == 0:
        return prefix
    for i in range(len(min(strs))):
        c = strs[0][i]
        if all(s[i] == c for s in strs):
            prefix += c
        else:
            break