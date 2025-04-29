def isMatch(s: str, p: str) -> bool:
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern to match.

    Returns:
        True if the pattern matches the entire input string, False otherwise.
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
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
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*. ", False),
    ]
    passed = 0
    for s, p, expected in test_cases:
        result = isMatch(s, p)
        print(f"Test: {s} + {p} -> {expected} == {result} -> {result == expected}")
        if result == expected:
            passed += 1
    print(f"Passed {passed} out of {len(test_cases)} tests.")

test_isMatch()