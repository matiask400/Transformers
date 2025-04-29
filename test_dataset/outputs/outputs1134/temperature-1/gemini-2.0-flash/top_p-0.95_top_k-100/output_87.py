def count_distinct_subsequences(s):
    """
    Counts the number of distinct, non-empty subsequences of a string.

    Args:
        s: The input string.

    Returns:
        The number of distinct subsequences modulo 10^9 + 7.
    """

    MOD = 10**9 + 7
    last = {}
    dp = [0] * (len(s) + 1)
    dp[0] = 1

    for i in range(1, len(s) + 1):
        dp[i] = (2 * dp[i - 1]) % MOD
        if s[i - 1] in last:
            dp[i] = (dp[i] - dp[last[s[i - 1]] - 1] + MOD) % MOD
        last[s[i - 1]] = i

    return (dp[len(s)] - 1 + MOD) % MOD

def test_count_distinct_subsequences():
    """
    Tests the count_distinct_subsequences function with various test cases.
    """

    test_cases = [
        ("abc", 7),
        ("aba", 6),
        ("aaa", 3),
        ("abcd", 15),
        ("aaaaa", 5),
        ("abcabc", 27)
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = count_distinct_subsequences(input_str)
        if actual_output == expected_output:
            print(f"Test case {i+1}: True")
            num_correct += 1
        else:
            print(f"Test case {i+1}: False (Input: {input_str}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"\n{num_correct}/{total_tests} correct")

if __name__ == '__main__':
    test_count_distinct_subsequences()