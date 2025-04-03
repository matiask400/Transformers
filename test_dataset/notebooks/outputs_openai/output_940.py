def countDistinctSubseq(S):
    MOD = 10**9 + 7
    n = len(S)
    dp = [0] * (n + 1)
    dp[0] = 1
    last = {}
    for i in range(1, n + 1):
        dp[i] = (2 * dp[i - 1]) % MOD
        c = S[i - 1]
        if c in last:
            dp[i] = (dp[i] - dp[last[c] - 1]) % MOD
        last[c] = i
    return (dp[n] - 1) % MOD

tests = [
    ("abc", 7),
    ("aba", 6),
    ("aaa", 3)
]

correct = 0
for inp, expected in tests:
    output = countDistinctSubseq(inp)
    result = output == expected
    print(result)
    if result:
        correct += 1
print(f"{correct}/{len(tests)}")