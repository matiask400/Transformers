def num_distinct_subsequences(s, t):
    """
    Given two strings s and t, return the number of distinct subsequences of s which equals t.

    A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

    It is guaranteed the answer fits on a 32-bit signed integer.

    Args:
        s: The source string.
        t: The target string.

    Returns:
        The number of distinct subsequences of s which equals t.
    """

    n = len(s)
    m = len(t)

    # dp[i][j] represents the number of distinct subsequences of s[:i] which equals t[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the first column to 1, because an empty string is always a subsequence of any string
    for i in range(n + 1):
        dp[i][0] = 1

    # Iterate over the strings and fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


def test_num_distinct_subsequences():
    test_cases = [
        (("rabbbit", "rabbit"), 3),
        (("babgbag", "bag"), 5),
        (("abcde", "ace"), 1),
        (("abcde", "abcde"), 1),
        (("abcde", "abcdf"), 0),
        (("ddd", "dd"), 3),
        (("daacbcaabddacdbaaadcbbbcbbcdcaab", "cebddaccdacb"), 0)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for (s, t), expected in test_cases:
        result = num_distinct_subsequences(s, t)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: s = {s}, t = {t}")
            print(f"Expected: {expected}, Got: {result}")

    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_num_distinct_subsequences()