import sys

# Set higher recursion depth for potential deep DP, although iterative is preferred
# sys.setrecursionlimit(2000) 

def solve():
    """
    Solves the K-Palindrome problem using dynamic programming to find the 
    Longest Common Subsequence (LCS) between the string and its reverse, 
    which is equivalent to the Longest Palindromic Subsequence (LPS).
    """
    def is_k_palindrome(s: str, k: int) -> bool:
        """
        Checks if a string s can be made a palindrome by removing at most k characters.

        Args:
            s: The input string.
            k: The maximum number of characters allowed to be removed.

        Returns:
            True if s is a k-palindrome, False otherwise.
        """
        n = len(s)
        s_rev = s[::-1]

        # dp[i][j] will store the length of the LCS between the first i 
        # characters of s and the first j characters of s_rev.
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Build the dp table
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s_rev[j - 1]:
                    # If characters match, extend the LCS from the previous diagonal
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # If characters don't match, take the maximum LCS length 
                    # by excluding either the last char of s or the last char of s_rev
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The length of the Longest Palindromic Subsequence (LPS) is dp[n][n]
        lps_length = dp[n][n]

        # The number of characters to remove is the difference between the
        # original string length and the length of its LPS.
        removals_needed = n - lps_length

        # Check if the number of removals needed is within the allowed limit k
        return removals_needed <= k

    # --- Test Runner ---
    test_cases = [
        ("abcdeca", 2, True),
        ("abbababa", 1, True),
        ("racecar", 0, True),
        ("google", 2, False),
        ("abacaba", 0, True),
        ("abacaba", 1, True),
        ("topcoderopen", 5, True),
        ("topcoderopen", 4, False),
        ("aaaaaaaaaa", 0, True),
        ("abcdefgh", 7, True),
        ("abcdefgh", 6, False),
        ("qwertyuiopasdfghjklzxcvbnm", 25, True),
        ("qwertyuiopasdfghjklzxcvbnm", 24, True), # LPS is 1 ('q'), remove 25. Ok.
        ("qwertyuiopasdfghjklzxcvbnmq", 25, True), # LPS is 2 ('q','q'), remove 25. Ok.
        ("a", 0, True),
        ("a", 1, True),
        ("ab", 1, True),
        ("ab", 0, False),
        ("aba", 0, True),
        ("abca", 1, True), # remove 'c' -> aba
        ("abcda", 1, False),
        ("abcda", 2, True) # remove 'b','d' -> aca
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (s_input, k_input, expected_output) in enumerate(test_cases):
        result = is_k_palindrome(s_input, k_input)
        passed = result == expected_output
        print(f"Test {i+1}: Input=(s='{s_input}', k={k_input}), Output={result}, Expected={expected_output} -> {passed}")
        if passed:
            correct_count += 1

    print(f"\n{correct_count}/{total_tests} tests passed.")

# Execute the solution and tests
solve()