def isMatch(s, p):
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

    return dp[m][n]

def run_tests(isMatch):
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("mississippi", "mis*is*ip*.", True),
        ("", "c*", True),
        ("", ".*", True),
        ("a", "", False),
        ("ab", ".*c", False)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for s, p, expected in test_cases:
        result = isMatch(s, p)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"  Input: s = \"{s}\", p = \"{p}\"")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    print(f"{correct_count}/{total_tests}")

run_tests(isMatch)