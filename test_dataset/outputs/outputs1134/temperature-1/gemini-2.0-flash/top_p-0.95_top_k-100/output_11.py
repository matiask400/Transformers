def isMatch(s, p):
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                dp[i][j] = False

    return dp[m][n]

def test_isMatch():
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("abc", "abc", True),
        ("abcd", ".*d", True),
        ("abcd", ".*c", False),
        ("", "a*", True),
        ("", ".*", True),
        ("a", "ab*", True),
        ("a", ".*a", True),
        ("a", ".*b", False),
        ("a", "a.", False),
        ("ab", "a.", True),
        ("bbbaccbbbaababbaaaabccbbaacac", "b*b*.*..*c***b*ba*.*.*b*b.*.*a.c*", False)
    ]

    correct_count = 0
    total_tests = len(tests)

    for s, p, expected in tests:
        result = isMatch(s, p)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: s = '{s}', p = '{p}'")
            print(f"Expected: {expected}, Got: {result}")

    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    test_isMatch()