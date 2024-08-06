def longestPalindrome(s: str) -> str:
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
            if l == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
            if dp[i][j] and l > max_len:
                max_len = l
                start = i
    return s[start:start + max_len]


# Test cases
input1 = "babad"
output1 = "bab"
input2 = "cbbd"
output2 = "bb"
input3 = "a"
output3 = "a"

print(longestPalindrome(input1) == output1)
print(longestPalindrome(input2) == output2)
print(longestPalindrome(input3) == output3)