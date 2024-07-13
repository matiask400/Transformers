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
    return s[start:start + max_len]


# Test the function with the provided examples
print(longestPalindrome("babad") == "bab" or longestPalindrome("babad") == "aba")  # Example 1. Should return True
print(longestPalindrome("cbbd") == "bb")  # Example 2. Should return True
print(longestPalindrome("a") == "a")  # Example 3. Should return True