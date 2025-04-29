def is_k_palindrome(s: str, k: int) -> bool:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    lps_length = dp[0][n - 1]
    removals_needed = n - lps_length
    return removals_needed <= k

def run_tests():
    tests = [
        {"input": {"s": "abcdeca", "k": 2}, "expected": True},
        {"input": {"s": "abbababa", "k": 1}, "expected": True},
        {"input": {"s": "ababa", "k": 0}, "expected": True},
        {"input": {"s": "aaba", "k": 0}, "expected": False},
        {"input": {"s": "aaba", "k": 1}, "expected": True},
        {"input": {"s": "leetcode", "k": 2}, "expected": False},
        {"input": {"s": "leetcode", "k": 3}, "expected": False},
        {"input": {"s": "leetcode", "k": 4}, "expected": True},
        {"input": {"s": "mbadm", "k": 2}, "expected": True},
        {"input": {"s": "mbdadm", "k": 2}, "expected": True},
        {"input": {"s": "mbdadbm", "k": 2}, "expected": True},
        {"input": {"s": "mbdadbmm", "k": 2}, "expected": False},
        {"input": {"s": "mbdadbmm", "k": 3}, "expected": True},
    ]
    correct_count = 0
    for i, test in enumerate(tests):
        actual_output = is_k_palindrome(**test["input"])
        expected_output = test["expected"]
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)
    print(f"{correct_count}/{len(tests)}")

if __name__ == '__main__':
    run_tests()