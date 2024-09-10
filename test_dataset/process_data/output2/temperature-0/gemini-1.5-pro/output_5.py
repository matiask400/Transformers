def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    max_len = 1
    start = 0
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if l == 2 and s[i] == s[j]:
                dp[i][j] = True
                start = i
                max_len = l
            elif s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = l
    return s[start : start + max_len]


s1 = "babad"
e1 = "bab"
s2 = "cbbd"
e2 = "bb"
s3 = "a"
e3 = "a"

print(f'Input: {s1}, Output: {longestPalindrome(s1)}, Expected: {e1}, Result: {longestPalindrome(s1) == e1}')
print(f'Input: {s2}, Output: {longestPalindrome(s2)}, Expected: {e2}, Result: {longestPalindrome(s2) == e2}')
print(f'Input: {s3}, Output: {longestPalindrome(s3)}, Expected: {e3}, Result: {longestPalindrome(s3) == e3}')