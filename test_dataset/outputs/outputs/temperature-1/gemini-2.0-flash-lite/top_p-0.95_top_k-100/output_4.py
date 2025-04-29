def is_match(s: str, p: str) -> bool:
    """
    Implements regular expression matching with '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the entire input string, False otherwise.
    """
    dp = {}  # Memoization to store intermediate results

    def backtrack(s_index, p_index):
        """Recursive helper function for matching."""
        if (s_index, p_index) in dp:
            return dp[(s_index, p_index)]

        # Base case: Pattern exhausted
        if p_index == len(p):
            return s_index == len(s)

        # Check if the current characters match or if the pattern has '.'
        first_match = (s_index < len(s) and
                       (p[p_index] == s[s_index] or p[p_index] == '.'))

        # Case 1: '*' encountered
        if p_index + 1 < len(p) and p[p_index + 1] == '*':
            # Option 1: '*' matches zero occurrences of preceding element
            match_zero = backtrack(s_index, p_index + 2)
            # Option 2: '*' matches one or more occurrences
            match_one_or_more = (first_match and
                                 backtrack(s_index + 1, p_index))
            result = match_zero or match_one_or_more
        else:
            # Case 2: No '*' or end of string
            result = first_match and backtrack(s_index + 1, p_index + 1)

        dp[(s_index, p_index)] = result  # Store the result in memo
        return result

    return backtrack(0, 0)


def test_is_match():
    """Tests the is_match function."""
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("ab", ".*c", False),
        ("a", ".*", True),
        ("a", "ab*", True),
        ("abcd", "d*a*c*b*", True),
        ("aaa", "ab*a", True),
        ("aaa", "ab*a*c*a", True),
        ("abc", "abc", True),
        ("abc", "abc.", False)
    ]
    correct_tests = 0
    for i, (s, p, expected) in enumerate(tests):
        result = is_match(s, p)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_tests}/{len(tests)}")


if __name__ == '__main__':
    test_is_match()