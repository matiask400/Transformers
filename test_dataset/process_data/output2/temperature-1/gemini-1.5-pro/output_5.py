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
            end = i + l - 1
            if l == 2 and s[i] == s[end]:
                dp[i][end] = True
                start = i
                max_len = l
            elif s[i] == s[end] and dp[i + 1][end - 1]:
                dp[i][end] = True
                start = i
                max_len = l
    return s[start:start + max_len]


# Test the solution
inputs = [
    "babad",
    "cbbd",
    "a",
    "ac"
]
outputs = [
    "bab",
    "bb",
    "a",
    "a"
]

for i in range(len(inputs)):
    output = longestPalindrome(inputs[i])
    print(output == outputs[i])