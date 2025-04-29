def isMatch(s, p):
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern string.

    Returns:
        True if the pattern matches the entire input string, False otherwise.
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # Match zero times
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # Match one or more times

    return dp[m][n]

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
        ("aaa", "a*a", True),
        ("aaa", "ab*a", False),
        ("aaa", "ab*a*", True),
        ("a", ".*..a*", True),
        ("ab", ".*..a*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.a", False),
    ]
    passed = 0
    for s, p, expected in test_cases:
        result = isMatch(s, p)
        print(f"Test case: s = {s}, p = {p}, expected = {expected}, actual = {result} - {result == expected}")
        if result == expected:
            passed += 1
    print(f"Passed {passed} out of {len(test_cases)} tests")

test_isMatch()