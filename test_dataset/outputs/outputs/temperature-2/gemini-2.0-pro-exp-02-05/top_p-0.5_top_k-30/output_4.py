def is_match(s: str, p: str) -> bool:
    """
    Given an input string (s) and a pattern (p), implement regular expression matching
    with support for '.' and '*' where:
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).
    """
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

    return dp[m][n]


def test_is_match():
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

    for s, p, expected_output in test_cases:
        actual_output = is_match(s, p)
        if actual_output == expected_output:
            print("True")
            passed_tests += 1
        else:
            print("False")

    print(f"{passed_tests}/{total_tests}")


if __name__ == "__main__":
    test_is_match()