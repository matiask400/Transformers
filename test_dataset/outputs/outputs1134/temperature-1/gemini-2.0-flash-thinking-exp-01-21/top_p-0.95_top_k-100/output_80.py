def num_distinct_subsequences(s: str, t: str) -> int:
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]

def test_num_distinct_subsequences():
    tests = [
        {"s": "rabbbit", "t": "rabbit", "expected": 3},
        {"s": "babgbag", "t": "bag", "expected": 5},
        {"s": "abcde", "t": "ace", "expected": 1},
        {"s": "abcde", "t": "aec", "expected": 0},
        {"s": "dddce", "t": "dc", "expected": 3},
        {"s": "daacaedaceca", "t": "ace", "expected": 15},
        {"s": "leetcode", "t": "lee", "expected": 4},
        {"s": "aaaaaaaaaa", "t": "aaaaa", "expected": 252},
        {"s": "bccbabcbc", "t": "bccbc", "expected": 10},
    ]
    correct_count = 0
    for test in tests:
        s = test["s"]
        t = test["t"]
        expected = test["expected"]
        actual = num_distinct_subsequences(s, t)
        if actual == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
    print(f"{correct_count}/{len(tests)}")

if __name__ == '__main__':
    test_num_distinct_subsequences()