def isMatch(s, p):
    from functools import lru_cache

    @lru_cache(None)
    def dp(i, j):
        if j == len(p):
            return i == len(s)
        first_match = i < len(s) and p[j] in {s[i], '.'}
        if (j + 1) < len(p) and p[j+1] == '*':
            return dp(i, j+2) or (first_match and dp(i+1, j))
        else:
            return first_match and dp(i+1, j+1)
    
    return dp(0, 0)

def test():
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
    ]
    correct = 0
    for s, p, expected in tests:
        result = isMatch(s, p)
        if result == expected:
            print("True")
            correct +=1
        else:
            print("False")
    print(f"{correct}/{len(tests)}")

test()