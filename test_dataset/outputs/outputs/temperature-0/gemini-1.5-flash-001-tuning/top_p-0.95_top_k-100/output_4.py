def isMatch(s, p):
    """
    Implements regular expression matching with support for '.' and '*'.

    Args:
        s: The input string.
        p: The pattern.

    Returns:
        True if the pattern matches the entire input string, False otherwise.
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
    return dp[m][n]

def test_isMatch():
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("a", "ab*", True),
        ("a", ".*", True),
        ("ab", ".*c", False),
        ("aaa", "a*a", True),
        ("aaa", "ab*a", False),
        ("aaa", "ab*a*", True),
        ("aaa", "a*a*", True),
        ("aaa", "a*b*", True),
        ("aaa", "a*b*c*", True),
        ("aaa", "a*b*c*d*", True),
        ("aaa", "a*b*c*d*e*", True),
        ("aaa", "a*b*c*d*e*f*", True),
        ("aaa", "a*b*c*d*e*f*g*", True),
        ("aaa", "a*b*c*d*e*f*g*h*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*", True),
        ("aaa", "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*", True),
    ]
    passed = 0
    for s, p, expected in test_cases:
        result = isMatch(s, p)
        print(result == expected, end=" ")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")

test_isMatch()