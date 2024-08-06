def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    maxLen = 1
    start = 0
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                if j - i == 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        start = i
    return s[start:start + maxLen]

# Example 1
s1 = "babad"
output1 = longestPalindrome(s1)
print(output1 == "bab")  # True or False

# Example 2
s2 = "cbbd"
output2 = longestPalindrome(s2)
print(output2 == "bb")  # True or False

# Example 3
s3 = "a"
output3 = longestPalindrome(s3)
print(output3 == "a")  # True or False

# Example 4
s4 = "ac"
output4 = longestPalindrome(s4)
print(output4 == "a")  # True or False