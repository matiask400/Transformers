s = "babad"
print(longestPalindrome(s) == "bab" or longestPalindrome(s) == "aba")
s = "cbbd"
print(longestPalindrome(s) == "bb")
s = "a"
print(longestPalindrome(s) == "a")
s = "ac"
print(longestPalindrome(s) == "a")

def longestPalindrome(s):
    if not s:
        return ""
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    max_len = 1
    start = 0
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if l == 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
            if dp[i][j] and l > max_len:
                max_len = l
                start = i
    return s[start:start + max_len]