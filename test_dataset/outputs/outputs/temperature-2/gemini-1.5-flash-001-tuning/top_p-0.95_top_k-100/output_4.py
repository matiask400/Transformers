def isMatch(s, p):
    """
    Implements regular expression matching with support for '.' and '*'.
    """
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Empty pattern matches empty string
    dp[0][0] = True

    # Handle '*' at the beginning of pattern
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # Match zero times
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # Match one or more times

    return dp[n][m]


def test_isMatch():
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("a", "ab*", True),
        ("a", ".*", True),
        ("ab", ".*c", False),
        ("aaa", "ab*a", True),
        ("aaa", "ab*a*c", False),
        ("aab", "c*a*b", True),
    ]

    passed_tests = 0

    for case in test_cases:
        result = isMatch(case[0], case[1])
        print(f"True: {result == case[2]}")
        if result == case[2]:
            passed_tests += 1

    print(f"Passed {passed_tests}/{len(test_cases)} tests")

test_isMatch()