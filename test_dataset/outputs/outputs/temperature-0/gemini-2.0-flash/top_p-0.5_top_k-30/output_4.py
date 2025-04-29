def is_match(s, p):
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the entire string, False otherwise.
    """
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                dp[i][j] = False

    return dp[len(s)][len(p)]

def test_is_match():
    """
    Tests the is_match function.
    """
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("a", "ab*", True),
        ("a", ".*..a*", False),
        ("aaa", "a*a", True),
        ("abc", ".*c", True),
        ("abcd", ".*d", True)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for s, p, expected_output in test_cases:
        result = is_match(s, p)
        if result == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_is_match()