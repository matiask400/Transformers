def isMatch(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
    return dp[len(s)][len(p)]

# Example 1
s1 = "aa"
p1 = "a"
output1 = isMatch(s1, p1)
print(output1 == False)

# Example 2
s2 = "aa"
p2 = "a*"
output2 = isMatch(s2, p2)
print(output2 == True)

# Example 3
s3 = "ab"
p3 = ".*"
output3 = isMatch(s3, p3)
print(output3 == True)