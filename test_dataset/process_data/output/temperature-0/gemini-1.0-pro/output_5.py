def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    maxLen = 1
    for i in range(n - 1, -1, -1):
        dp[i][i] = True
        for j in range(i + 1, n):
            if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i
    return s[start:start + maxLen]