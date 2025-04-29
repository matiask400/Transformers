def isMatch(s, p):
    """
    Checks if a given string s matches a given pattern p using regular expression matching.

    Args:
        s: The input string.
        p: The pattern to match against.

    Returns:
        True if the string matches the pattern, False otherwise.
    """
    m = len(s)
    n = len(p)

    # Create a DP table to store matching results
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty string and empty pattern match
    dp[0][0] = True

    # Handle cases where pattern starts with '*'
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill in the DP table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Either match 0 or more preceding elements
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

    return dp[m][n]

def test_isMatch():
    """
    Tests the isMatch function with various inputs.
    """
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
    ]
    passed = 0
    for s, p, expected_output in test_cases:
        output = isMatch(s, p)
        print(f'Test: "{s}" + "{p}" - {output} == {expected_output} - {output == expected_output}')
        if output == expected_output:
            passed += 1
    print(f'Passed {passed} out of {len(test_cases)} tests.')


test_isMatch()