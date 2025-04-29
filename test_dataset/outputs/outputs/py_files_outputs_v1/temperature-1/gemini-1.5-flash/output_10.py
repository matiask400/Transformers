def isMatch(s: str, p: str) -> bool:
    n = len(s)
    m = len(p)
    
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    
    dp[0][0] = True
    
    for j in range(2, m + 1):
        if p[j - 1] == '*' and dp[0][j - 2]:
            dp[0][j] = True
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
    
    return dp[n][m]

# Test cases
s1 = "aa"
 p1 = "a"

s2 = "aa"
 p2 = "a*"

s3 = "ab"
 p3 = ".*"

s4 = "aab"
 p4 = "c*a*b"

s5 = "mississippi"
 p5 = "mis*is*p*."

print(f"Input 1: s = {s1}, p = {p1}, Output: {isMatch(s1, p1)}")
print(f"Input 2: s = {s2}, p = {p2}, Output: {isMatch(s2, p2)}")
print(f"Input 3: s = {s3}, p = {p3}, Output: {isMatch(s3, p3)}")
print(f"Input 4: s = {s4}, p = {p4}, Output: {isMatch(s4, p4)}")
print(f"Input 5: s = {s5}, p = {p5}, Output: {isMatch(s5, p5)}")