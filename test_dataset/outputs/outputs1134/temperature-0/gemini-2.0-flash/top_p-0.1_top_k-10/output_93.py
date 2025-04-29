def is_k_palindrome(s: str, k: int) -> bool:
    """
    Given a string `s` and an integer `k`, return `true` if `s` is a `k`-palindrome.

    A string is `k`-palindrome if it can be transformed into a palindrome by removing at most `k` characters from it.
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

    return dp[0][n - 1] <= k


def test_is_k_palindrome():
    test_cases = [
        ("abcdeca", 2, True),
        ("abbababa", 1, True),
        ("abc", 1, False),
        ("ab", 0, False),
        ("a", 0, True),
        ("racecar", 0, True),
        ("leetcode", 3, True),
        ("leetcodel", 3, False),
        ("leetcodel", 4, True),
        ("leetcodel", 5, True),
        ("leetcodel", 6, True),
        ("leetcodel", 7, True),
        ("leetcodel", 8, True),
        ("leetcodel", 9, True),
        ("leetcodel", 10, True),
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


if __name__ == "__main__":
    test_is_k_palindrome()