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

# Example 1
s1 = "aa"
p1 = "a"
output1 = isMatch(s1, p1)
print(output1 == False)  # True

# Example 2
s2 = "aa"
p2 = "a*"
output2 = isMatch(s2, p2)
print(output2 == True)  # True

# Example 3
s3 = "ab"
p3 = ".*"
output3 = isMatch(s3, p3)
print(output3 == True)  # True

# Example 4
s4 = "aab"
p4 = "c*a*b"
output4 = isMatch(s4, p4)
print(output4 == True)  # True

# Example 5
s5 = "mississippi"
p5 = "mis*is*p*."
output5 = isMatch(s5, p5)
print(output5 == False)  # True