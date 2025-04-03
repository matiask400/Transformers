def distinct_subsequences(s):
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    last_occurrence = {}
    for i in range(1, n + 1):
        char = s[i-1]
        dp[i] = (2 * dp[i-1]) % MOD
        if char in last_occurrence:
            j = last_occurrence[char]
            dp[i] = (dp[i] - dp[j] + MOD) % MOD
        last_occurrence[char] = i-1
    return (dp[n] - 1 + MOD) % MOD

def test_distinct_subsequences():
    test_cases = [
        ("abc", 7),
        ("aba", 6),
        ("aaa", 3),
        ("", 0),
        ("abcd", 15),
        ("aabbcc", 27),
        ("abcdefg", 127),
        ("aaaaaaaaaa", 10),
        ("ababababab", 342),
        ("ccccccccccc", 10),
    ]
    num_tests = len(test_cases)
    correct_tests = 0
    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = distinct_subsequences(input_str)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False (Input: '{input_str}', Expected: {expected_output}, Actual: {actual_output})")
    print(f"\n{correct_tests}/{num_tests}")

if __name__ == '__main__':
    test_distinct_subsequences()