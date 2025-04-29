def isMatch(s: str, p: str) -> bool:
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the entire input string, False otherwise.
    """
    s_len = len(s)
    p_len = len(p)

    # dp[i][j] represents whether s[:i] matches p[:j]
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(1, p_len + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]  # '*' matches zero occurrences of the preceding character

    # Fill the dp table
    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # Current characters match
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' case
                dp[i][j] = dp[i][j - 2]  # '*' matches zero occurrences of the preceding character
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # '*' matches one or more occurrences
            else:
                # Characters don't match
                dp[i][j] = False

    return dp[s_len][p_len]

def test_isMatch():
    """Tests the isMatch function."""
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("a", "ab*", True),
        ("abc", ".*", True),
        ("abc", "a.c", True),
        ("abc", "a.d", False),
        ("aaa", "a*a", True),
        ("aaa", "ab*a*c*a", True),
        ("a", ".*..", False),
        ("ab", ".*c", False),
        ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False)
    ]
    correct_tests = 0
    for s, p, expected in tests:
        result = isMatch(s, p)
        if result == expected:
            print(True)
            correct_tests += 1
        else:
            print(False)
    print(f"{correct_tests}/{len(tests)}")

if __name__ == '__main__':
    test_isMatch()