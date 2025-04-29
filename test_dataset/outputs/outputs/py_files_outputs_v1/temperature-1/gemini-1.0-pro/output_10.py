def isMatch(s, p):
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(p):
            return i == len(s)
        if p[j + 1] != '*':
            memo[(i, j)] = (i < len(s) and (s[i] == p[j] or p[j] == '.')) and dp(i + 1, j + 1)
            return memo[(i, j)]
        else:
            res = dp(i, j + 2) or (i < len(s) and (s[i] == p[j] or p[j] == '.') and dp(i + 1, j))
            memo[(i, j)] = res
            return res
    return dp(0, 0)