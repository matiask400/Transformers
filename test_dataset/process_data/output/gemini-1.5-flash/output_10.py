def isMatch(s: str, p: str) -> bool:
    n = len(s)
    m = len(p)
    
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    
    for j in range(2, m + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
    
    return dp[n][m]

# Test cases
print(isMatch("aa", "a"))  # Output: False
print(isMatch("aa", "a*"))  # Output: True
print(isMatch("ab", ".*"))  # Output: True
print(isMatch("aab", "c*a*b"))  # Output: True
print(isMatch("mississippi", "mis*is*p*."))  # Output: False