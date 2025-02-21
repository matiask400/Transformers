def is_match(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for j in range(2, len(p) + 1):
        dp[0][j] = dp[0][j - 2] if p[j - 1] == '*' else False

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') else False)
            else:
                dp[i][j] = dp[i - 1][j - 1] if s[i - 1] == p[j - 1] or p[j - 1] == '.' else False

    return dp[len(s)][len(p)]

# Test inputs
tests = [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True)
]

for s, p, expected in tests:
    print("Test with s=", s, "and p=", p, "Result=", is_match(s, p) == expected)
