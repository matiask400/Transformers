def isMatch(s: str, p: str) -> bool:
    memo = {}

    def solve(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(p):
            return i == len(s)
        if j + 1 < len(p) and p[j + 1] == '*':
            # Case 1: '*' matches zero preceding elements
            if solve(i, j + 2):
                memo[(i, j)] = True
                return True
            # Case 2: '*' matches one or more preceding elements
            while i < len(s) and (p[j] == '.' or p[j] == s[i]):
                if solve(i + 1, j):
                    memo[(i, j)] = True
                    return True
                i += 1
            memo[(i, j)] = False
            return False
        else:
            if i < len(s) and (p[j] == '.' or p[j] == s[i]):
                res = solve(i + 1, j + 1)
                memo[(i, j)] = res
                return res
            else:
                memo[(i, j)] = False
                return False

    return solve(0, 0)

def test_isMatch():
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("ab", ".*c", False),
        ("aaa", "a*a", True),
        ("aaa", "ab*a", False),
        ("a", "ab*", True),
        ("bbbba", ".*a*a", True),
        ("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*", True)
    ]
    correct_count = 0
    for s, p, expected in tests:
        actual = isMatch(s, p)
        if actual == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
    print(f"{correct_count}/{len(tests)}")

test_isMatch()