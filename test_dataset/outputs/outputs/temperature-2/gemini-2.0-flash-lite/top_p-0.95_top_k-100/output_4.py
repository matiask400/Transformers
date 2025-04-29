def is_match(s: str, p: str) -> bool:
    """
    Implements regular expression matching with '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the string, False otherwise.
    """

    # Initialize a 2D DP table to store the matching results
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c* where string is empty
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Iterate over the string and pattern
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # If the characters match or pattern has '.', then it matches
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Handle the '*' character
                dp[i][j] = dp[i][j - 2]  # Match zero occurrences of the preceding character
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    # Match one or more occurrences of the preceding character
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                # Characters do not match
                dp[i][j] = False

    # Return the final result from the bottom-right cell of the DP table
    return dp[len(s)][len(p)]


def test_is_match():
    """
    Tests the is_match function.
    """
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("abc", "abc", True),
        ("abc", "abc.*", True),
        ("abc", "a.*", False),
        ("ab", ".*c", False),
        ("a", "ab*", True),
        ("aaa", "a*a", True),
        ("aaa", "ab*a", False),
        ("aaaaaaaaaaaaab", "a*b", True),
        ("", ".*", True),
        ("a", "", False),
        ("abcd", "d*", False)


    ]

    correct_count = 0
    for i, (s, p, expected_output) in enumerate(tests):
        result = is_match(s, p)
        if result == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test {i+1} Failed. Expected: {expected_output}, Got: {result}")

    print(f"{correct_count}/{len(tests)}")

test_is_match()