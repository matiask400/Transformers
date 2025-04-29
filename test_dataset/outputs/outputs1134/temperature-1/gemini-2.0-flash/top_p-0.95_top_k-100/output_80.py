def num_distinct_subsequences(s, t):
    """
    Given two strings s and t, return the number of distinct subsequences of s which equals t.

    A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

    It is guaranteed the answer fits on a 32-bit signed integer.

    Example 1:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
    As shown below, there are 3 ways you can generate "rabbit" from S.

    rabbbit
    rabbbit
    rabbbit

    Example 2:
    Input: s = "babgbag", t = "bag"
    Output: 5
    Explanation:
    As shown below, there are 5 ways you can generate "bag" from S.

    babgbag
    babgbag
    babgbag
    babgbag
    babgbag

    Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.
    """

    n = len(s)
    m = len(t)

    # dp[i][j] represents the number of distinct subsequences of s[:i] which equals t[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # If t is an empty string, there is always 1 way to form it (by deleting all characters)
    for i in range(n + 1):
        dp[i][0] = 1

    # If s is an empty string and t is not, there is no way to form t from s
    # So, dp[0][j] = 0 for j > 0 (already initialized as 0)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                # If the current characters match, we can either include it or exclude it
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                # If the current characters don't match, we can only exclude it
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


def test_num_distinct_subsequences():
    test_cases = [
        {"s": "rabbbit", "t": "rabbit", "expected": 3},
        {"s": "babgbag", "t": "bag", "expected": 5},
        {"s": "abcde", "t": "ace", "expected": 1},
        {"s": "abcde", "t": "abcde", "expected": 1},
        {"s": "abcde", "t": "abce", "expected": 1},
        {"s": "abcde", "t": "abcdef", "expected": 0},
        {"s": "aaaaaaaaaa", "t": "aa", "expected": 55},
        {"s": "ddd", "t": "dd", "expected": 3},
        {"s": "daacbccaacdbddabddaacdbcbcaacbdacddcaadcbaacbca", "t": "caadcdaac", "expected": 54397419},
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        s = test_case["s"]
        t = test_case["t"]
        expected = test_case["expected"]
        result = num_distinct_subsequences(s, t)

        if result == expected:
            print(f"Test {i + 1}: True")
            num_correct += 1
        else:
            print(f"Test {i + 1}: False")
            print(f"  Input: s = '{s}', t = '{t}'")
            print(f"  Expected: {expected}")
            print(f"  Actual: {result}")

    print(f"\n{num_correct}/{total_tests} correct")


if __name__ == "__main__":
    test_num_distinct_subsequences()