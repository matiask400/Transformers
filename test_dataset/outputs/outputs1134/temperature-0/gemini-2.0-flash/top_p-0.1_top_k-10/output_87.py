def count_distinct_subsequences(S):
    """
    Counts the number of distinct, non-empty subsequences of S modulo 10^9 + 7.

    Args:
        S: The input string.

    Returns:
        The number of distinct subsequences modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    n = len(S)
    dp = [0] * (n + 1)
    dp[0] = 1
    last = {}

    for i in range(1, n + 1):
        dp[i] = (2 * dp[i - 1]) % MOD
        if S[i - 1] in last:
            dp[i] = (dp[i] - dp[last[S[i - 1]] - 1] + MOD) % MOD
        last[S[i - 1]] = i

    return (dp[n] - 1 + MOD) % MOD


def test_count_distinct_subsequences():
    """
    Tests the count_distinct_subsequences function with several test cases.
    """
    test_cases = [
        ("abc", 7),
        ("aba", 6),
        ("aaa", 3),
        ("abcd", 15),
        ("aaaa", 4),
        ("a", 1),
        ("abac", 11),
        ("abcabc", 27),
        ("abcdefg", 127),
        ("aaaaaaaaaa", 11)
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = count_distinct_subsequences(input_str)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Input: {input_str}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"\n{num_correct}/{total_tests} correct")


if __name__ == "__main__":
    test_count_distinct_subsequences()