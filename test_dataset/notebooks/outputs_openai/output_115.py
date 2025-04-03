def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    if n == 0:
        return 1
    if m < n:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        # Iterate backwards to ensure dp[j-1] refers to the previous state
        for j in range(n, 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]
    return dp[n]

# Define test cases
test_cases = [
    {
        "s": "rabbbit",
        "t": "rabbit",
        "expected": 3
    },
    {
        "s": "babgbag",
        "t": "bag",
        "expected": 5
    },
    # Additional test cases
    {
        "s": "abcdef",
        "t": "ace",
        "expected": 1
    },
    {
        "s": "aaaaa",
        "t": "aaa",
        "expected": 10
    },
    {
        "s": "abc",
        "t": "",
        "expected": 1
    },
    {
        "s": "",
        "t": "a",
        "expected": 0
    },
    {
        "s": "aabbcc",
        "t": "abc",
        "expected": 8
    },
    {
        "s": "leetcode",
        "t": "let",
        "expected": 3
    }
]

correct = 0
total = len(test_cases)

for case in test_cases:
    result = numDistinct(case["s"], case["t"])
    is_correct = result == case["expected"]
    print(is_correct)
    if is_correct:
        correct += 1

print(f"{correct}/{total}")