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
            s_idx: The current index in the string s.
            p_idx: The current index in the pattern p.

        Returns:
            True if the pattern matches the substring of s starting at s_idx,
            False otherwise.
        """
        if (s_idx, p_idx) in dp:
            return dp[(s_idx, p_idx)]

        # Base case: If the pattern is exhausted
        if p_idx == len(p):
            return s_idx == len(s)

        # Check if the current characters match or if the pattern has a '.'
        first_match = (s_idx < len(s) and
                       (p[p_idx] == s[s_idx] or p[p_idx] == '.'))

        # Case 1: '*' encountered
        if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
            # Option 1: '*' matches zero occurrences of the preceding character
            match = solve(s_idx, p_idx + 2)  # Skip the '*' and the preceding character
            # Option 2: '*' matches one or more occurrences of the preceding character
            if not match and first_match:
                match = solve(s_idx + 1, p_idx)  # Consume one character from s
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
        ("abc", "abc", True),
        ("abc", "abd", False),
        ("abc", "a.c", True),
        ("abc", "a.*", True),
        ("abc", "a*b*c", True),
        ("abc", "a*b*c*", True),
        ("abc", "a*b*c*d", False),
        ("a", "ab*", True),
        ("a", ".*..", False),
        ("ab", ".*c", False),
        ("aaaaaaaaaaaaab", "a*b", True)
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