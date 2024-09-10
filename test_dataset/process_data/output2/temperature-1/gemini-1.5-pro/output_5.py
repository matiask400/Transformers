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
                max_len = 2
            elif s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if l > max_len:
                    start = i
                    max_len = l
    return s[start : start + max_len]


s1 = "babad"
o1 = "bab"
s2 = "cbbd"
o2 = "bb"
s3 = "a"
o3 = "a"

print(f"Input 1: {s1 == s1}, Output 1: {o1 == longestPalindrome(s1)}")
print(f"Input 2: {s2 == s2}, Output 2: {o2 == longestPalindrome(s2)}")
print(f"Input 3: {s3 == s3}, Output 3: {o3 == longestPalindrome(s3)}")