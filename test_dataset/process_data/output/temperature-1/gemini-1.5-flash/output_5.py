def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    max_len = 1
    start = 0
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    start = i
                    max_len = k
    return s[start:start + max_len]