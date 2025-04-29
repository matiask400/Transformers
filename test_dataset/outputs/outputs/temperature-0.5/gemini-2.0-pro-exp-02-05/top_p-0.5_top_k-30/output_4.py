def isMatch(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                dp[i][j] = False

    return dp[m][n]

def run_tests(isMatch):
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "", True),
        ("a", "", False),
        ("", "a*", True),
        ("ab", ".*c", False)

    ]

    passed_tests = 0
    total_tests = len(test_cases)

    for i, (s, p, expected) in enumerate(test_cases):
        result = isMatch(s, p)
        if result == expected:
            print(f"Test {i+1}: True")
            passed_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{passed_tests}/{total_tests} tests passed.")

run_tests(isMatch)