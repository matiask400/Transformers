def is_match(s, p):
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the entire string, False otherwise.
    """
    memo = {}  # Use memoization to avoid redundant calculations

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j == 0:
            return i == 0

        if p[j - 1] != '*':
            if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                memo[(i, j)] = dp(i - 1, j - 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = False
                return False
        else:
            # Case 1: Zero occurrences of the preceding element
            if dp(i, j - 2):
                memo[(i, j)] = True
                return True

            # Case 2: One or more occurrences of the preceding element
            if i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                memo[(i, j)] = dp(i - 1, j)
                return memo[(i, j)]
            else:
                memo[(i, j)] = False
                return False

    return dp(len(s), len(p))

def test_is_match():
    """
    Tests the is_match function with various test cases.
    """
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("a", "ab*", True),
        ("bbbaccbbba", "b*a*a*.c*b*b*a*", True),
    ]

    correct_count = 0
    total_count = len(tests)

    for s, p, expected_output in tests:
        result = is_match(s, p)
        if result == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_is_match()