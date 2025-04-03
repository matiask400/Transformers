def isMatch(s, p):
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:
    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).
    """
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j == len(p):
            return i == len(s)

        if i == len(s):
            if (len(p) - j) % 2 == 0:
                for k in range(j, len(p), 2):
                    if k + 1 >= len(p) or p[k+1] != '*':
                        memo[(i, j)] = False
                        return False
                memo[(i, j)] = True
                return True
            else:
                memo[(i, j)] = False
                return False

        first_match = (p[j] == s[i] or p[j] == '.')

        if j + 1 < len(p) and p[j + 1] == '*':
            memo[(i, j)] = (dp(i, j + 2) or (first_match and dp(i + 1, j)))
            return memo[(i, j)]
        else:
            memo[(i, j)] = first_match and dp(i + 1, j + 1)
            return memo[(i, j)]

    return dp(0, 0)

def test_isMatch():
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("a", "ab*", True),
        ("ab", ".*c", False),
        ("aaa", "a*a", True),
        ("abcd", "d*", False),
        ("", "a*", True),
        ("", ".*", True),
        ("abc", ".*", True),
        ("a", ".*", True),
        ("a", "ab*", True),
        ("a", ".*a", False),
        ("bbbba", ".*a*a", True),
        ("aaaaaaaaaaaaab", "a*b", True)
    ]

    correct_count = 0
    for i, (s, p, expected) in enumerate(enumerate(tests)):
        result = isMatch(s, p)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: s='{s}', p='{p}'")
            print(f"  Expected: {expected}, Got: {result}")

    print(f"\nCorrect: {correct_count}/{len(tests)}")

if __name__ == "__main__":
    test_isMatch()