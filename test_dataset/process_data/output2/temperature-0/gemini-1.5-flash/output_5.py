def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s
    
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    maxLen = 1
    start = 0
    
    for i in range(n):
        dp[i][i] = True
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        start = i
    
    return s[start:start + maxLen]

# Example 1
s = "babad"
output_1 = longestPalindrome(s)
print(output_1 == "bab")  # True

# Example 2
s = "cbbd"
output_2 = longestPalindrome(s)
print(output_2 == "bb")  # True

# Example 3
s = "a"
output_3 = longestPalindrome(s)
print(output_3 == "a")  # True

# Example 4
s = "ac"
output_4 = longestPalindrome(s)
print(output_4 == "a")  # True