def isMatch(s, p):
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for j in range(2, m + 1):
        if p[j - 1] == '*' and dp[0][j - 2]:
            dp[0][j] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

    return dp[n][m]

# Example 1
s1 = "aa"
p1 = "a"
print(f"Example 1: {isMatch(s1, p1) == False}")

# Example 2
s2 = "aa"
p2 = "a*"
print(f"Example 2: {isMatch(s2, p2) == True}")

# Example 3
s3 = "ab"
p3 = ".*"
print(f"Example 3: {isMatch(s3, p3) == True}")

# Example 4
s4 = "aab"
p4 = "c*a*b"
print(f"Example 4: {isMatch(s4, p4) == True}")

# Example 5
s5 = "mississippi"
p5 = "mis*is*p*."
print(f"Example 5: {isMatch(s5, p5) == False}")