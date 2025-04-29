def isMatch(s: str, p: str) -> bool:
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j == len(p):
            return i == len(s)

        if j + 1 < len(p) and p[j + 1] == '*':
            if i < len(s) and (p[j] == s[i] or p[j] == '.'):
                res = dp(i + 1, j) or dp(i, j + 2)
            else:
                res = dp(i, j + 2)
        else:
            if i < len(s) and (p[j] == s[i] or p[j] == '.'):
                res = dp(i + 1, j + 1)
            else:
                res = False

        memo[(i, j)] = res
        return res

    return dp(0, 0)

def test_isMatch():
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "a*", True),
        ("a", "", False),
        ("", "", True),
        ("ab", ".*c", False),
        ("aaa", "a*a", True),
        ("aaa", "ab*a*c*a", True),
        ("abcd", "d*", False),
        ("a", "ab*", True)
    ]
    num_correct = 0
    total_tests = len(tests)

    for s, p, expected in tests:
        actual = isMatch(s, p)
        if actual == expected:
            print("True")
            num_correct += 1
        else:
            print("False")
    print(f"{num_correct}/{total_tests}")

test_isMatch()