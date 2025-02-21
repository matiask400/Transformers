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
input_1 = "babad"
output_1 = "bab"
print(longestPalindrome(input_1) == output_1)

# Example 2
input_2 = "cbbd"
output_2 = "bb"
print(longestPalindrome(input_2) == output_2)

# Example 3
input_3 = "a"
output_3 = "a"
print(longestPalindrome(input_3) == output_3)