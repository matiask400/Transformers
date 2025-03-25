def isMatch(s: str, p: str) -> bool:
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the entire input string, False otherwise.
    """
    dp = {}  # Memoization to store results of subproblems

    def solve(s_idx, p_idx):
        """
        Recursive helper function to solve the matching problem.

        Args:
            s_idx: Index of the current character in the string.
            p_idx: Index of the current character in the pattern.

        Returns:
            True if the pattern matches the substring starting from s_idx,
            False otherwise.
        """
        if (s_idx, p_idx) in dp:
            return dp[(s_idx, p_idx)]

        # Base case: If the pattern is exhausted
        if p_idx == len(p):
            return s_idx == len(s)

        # Check if the current characters match or if the pattern has a '.'
        first_match = s_idx < len(s) and (p[p_idx] == s[s_idx] or p[p_idx] == '.')

        # Case 1: '*' encountered
        if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
            # Option 1: '*' matches zero occurrences of the preceding character
            # Skip the '*' and the preceding character
            match = solve(s_idx, p_idx + 2)
            # Option 2: '*' matches one or more occurrences of the preceding character
            if not match and first_match:
                match = solve(s_idx + 1, p_idx)
            dp[(s_idx, p_idx)] = match
            return match

        # Case 2: No '*' or end of pattern
        if first_match:
            match = solve(s_idx + 1, p_idx + 1)
            dp[(s_idx, p_idx)] = match
            return match

        # No match
        dp[(s_idx, p_idx)] = False
        return False

    return solve(0, 0)

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
        ("a", ".*..a*", False),
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