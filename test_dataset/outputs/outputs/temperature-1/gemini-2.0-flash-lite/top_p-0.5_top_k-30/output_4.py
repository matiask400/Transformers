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

    def regex_match(s_idx, p_idx):
        """Recursive helper function with memoization."""
        if (s_idx, p_idx) in dp:
            return dp[(s_idx, p_idx)]

        # Base cases
        if p_idx == len(p):
            return s_idx == len(s)  # Pattern exhausted, string also exhausted

        if s_idx == len(s):
            # String exhausted, check if pattern can match empty string
            if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
                result = regex_match(s_idx, p_idx + 2)  # Skip the char and '*'
                dp[(s_idx, p_idx)] = result
                return result
            else:
                dp[(s_idx, p_idx)] = False
                return False

        # Recursive cases
        char_match = (p[p_idx] == '.' or p[p_idx] == s[s_idx])

        if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
            # '*' case: zero or more occurrences of the preceding character
            # Option 1: Match zero occurrences (skip the char and '*')
            result = regex_match(s_idx, p_idx + 2)
            # Option 2: Match one or more occurrences (if char matches)
            if char_match:
                result = result or regex_match(s_idx + 1, p_idx)
            dp[(s_idx, p_idx)] = result
            return result
        elif char_match:
            # Regular character match or '.' match
            result = regex_match(s_idx + 1, p_idx + 1)
            dp[(s_idx, p_idx)] = result
            return result
        else:
            # No match
            dp[(s_idx, p_idx)] = False
            return False

    return regex_match(0, 0)

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
        ("a", ".*..", False),
        ("ab", ".*c", False),
        ("aaa", "ab*a", False),
        ("aaa", "ab*a*c*a", True),
        ("aaaa", "a*a*", True),
        ("ab", ".*..", False),
        ("a", ".*", True),
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