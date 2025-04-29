def isMatch(s: str, p: str) -> bool:
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the entire input string, False otherwise.
    """
    dp = {}  # Memoization table (s_index, p_index) -> boolean

    def solve(s_index, p_index):
        if (s_index, p_index) in dp:
            return dp[(s_index, p_index)]

        # Base cases
        if p_index == len(p):
            return s_index == len(s)

        first_match = (s_index < len(s) and
                       (p[p_index] == s[s_index] or p[p_index] == '.'))

        if p_index + 1 < len(p) and p[p_index + 1] == '*':
            # Two possibilities:
            # 1. '*' matches zero occurrences of the preceding character
            # 2. '*' matches one or more occurrences of the preceding character
            result = solve(s_index, p_index + 2) or (first_match and solve(s_index + 1, p_index))
        else:
            # No '*' or end of pattern
            result = first_match and solve(s_index + 1, p_index + 1)

        dp[(s_index, p_index)] = result
        return result

    return solve(0, 0)

def run_tests():
    """Runs the tests and prints the results."""
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("a", "ab*", True),
        ("abc", ".*", True),
        ("abc", "a.c", True),
        ("abc", "a.d", False),
        ("aaa", "ab*a", True),
        ("aaa", "ab*c*a", True),
        ("a", ".*..a*", False),
        ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False)
    ]
    correct_tests = 0
    for i, (s, p, expected_output) in enumerate(test_cases):
        result = isMatch(s, p)
        if result == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"Correct tests: {correct_tests}/{len(test_cases)}")

run_tests()