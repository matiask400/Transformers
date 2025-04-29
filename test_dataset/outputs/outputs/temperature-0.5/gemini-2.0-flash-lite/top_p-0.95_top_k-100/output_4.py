def isMatch(s: str, p: str) -> bool:
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the entire input string, False otherwise.
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Case 1: '*' matches zero occurrences of the preceding character
                dp[i][j] = dp[i][j - 2]
                # Case 2: '*' matches one or more occurrences
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                dp[i][j] = False

    return dp[m][n]


def run_tests():
    """Runs the test cases and prints the results."""
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("abc", ".*", True),
        ("abc", "abc", True),
        ("abc", "abd", False),
        ("a", "ab*", True),
        ("a", ".*..", False),
        ("ab", ".*c", False),
        ("a", ".*", True),
        ("a", "a*", True),
        ("ab", ".*c*", False),
        ("aaa", "ab*a", False),
        ("aaa", "ab*a*c*a", True),
        ("aaaa", "a*a*", True),
        ("ab", ".*..c*", False)
    ]
    correct_count = 0
    total_tests = len(test_cases)

    for i, (s, p, expected_result) in enumerate(test_cases):
        result = isMatch(s, p)
        if result == expected_result:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"Correct tests: {correct_count}/{total_tests}")

run_tests()