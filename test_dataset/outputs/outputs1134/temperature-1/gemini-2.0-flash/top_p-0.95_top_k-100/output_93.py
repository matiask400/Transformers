def is_k_palindrome(s: str, k: int) -> bool:
    """
    Given a string `s` and an integer `k`, return `true` if `s` is a `k`-palindrome.

    A string is `k`-palindrome if it can be transformed into a palindrome by removing at most `k` characters from it.


    Example 1:
    Input: s = "abcdeca", k = 2
    Output: true
    Explanation: Remove 'b' and 'e' characters.


    Example 2:
    Input: s = "abbababa", k = 1
    Output: true

    Constraints:
    `1 <= s.length <= 1000`
    `s` consists of only lowercase English letters.

    `1 <= k <= s.length`
    """
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[n - j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    longest_palindrome_subsequence_length = dp[n][n]
    return n - longest_palindrome_subsequence_length <= k

def test_is_k_palindrome():
    test_cases = [
        ("abcdeca", 2, True),
        ("abbababa", 1, True),
        ("abc", 1, False),
        ("racecar", 0, True),
        ("abca", 1, True),
        ("abcca", 0, False),
        ("abcca", 1, True),
        ("abcca", 2, True),
        ("abcca", 3, True),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for s, k, expected in test_cases:
        result = is_k_palindrome(s, k)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

test_is_k_palindrome()