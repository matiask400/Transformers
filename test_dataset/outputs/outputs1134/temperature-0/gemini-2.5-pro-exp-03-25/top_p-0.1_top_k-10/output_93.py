import sys

# Set higher recursion depth for potential recursive solutions (though DP is preferred here)
# sys.setrecursionlimit(2000) 

def solve():
    """
    Solves the k-palindrome problem using dynamic programming to find the
    Longest Common Subsequence (LCS) between the string and its reverse.
    """

    def is_k_palindrome(s: str, k: int) -> bool:
        """
        Checks if a string s can be transformed into a palindrome by removing
        at most k characters.

        Args:
            s: The input string.
            k: The maximum number of characters allowed to be removed.

        Returns:
            True if s is a k-palindrome, False otherwise.
        """
        n = len(s)
        s_rev = s[::-1]

        # dp[j] will store the length of the LCS between s[:i] and s_rev[:j]
        # We use space optimization (only need the previous row's results)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Store the value from the previous diagonal (dp[i-1][j-1])
            prev_diag = 0 
            # Create a new array for the current row's calculations
            # Alternatively, update dp in place carefully
            # Using a temporary array 'next_dp' is often clearer
            next_dp = [0] * (n + 1) 
            
            for j in range(1, n + 1):
                # Store dp[i-1][j] before it might be overwritten if updating in place
                # Not strictly needed with next_dp approach, but useful for understanding
                # temp = dp[j] 
                
                if s[i - 1] == s_rev[j - 1]:
                    # Characters match, extend the LCS from the diagonal
                    next_dp[j] = 1 + dp[j-1] # dp[j-1] here corresponds to dp[i-1][j-1] from the previous row
                else:
                    # Characters don't match, take the max from left or top
                    # dp[j] corresponds to dp[i-1][j] (top)
                    # next_dp[j-1] corresponds to dp[i][j-1] (left)
                    next_dp[j] = max(dp[j], next_dp[j - 1])
                
                # Update prev_diag for the next iteration (not needed with next_dp)
                # prev_diag = temp 
            
            # The current row becomes the previous row for the next iteration
            dp = next_dp


        # dp[n] now holds the length of the LCS of s and s_rev
        lps_length = dp[n]

        # The minimum number of characters to remove to make s a palindrome
        # is the total length minus the length of the longest palindromic subsequence.
        min_removals = n - lps_length

        # Check if the minimum removals required is within the allowed limit k
        return min_removals <= k

    # --- Testing Framework ---
    test_cases = [
        ("abcdeca", 2, True),
        ("abbababa", 1, True),
        ("racecar", 0, True),
        ("google", 2, True), # remove 'l', 'e' -> "googe" -> remove 'g' -> "ooe" -> remove 'e' -> "oo" (palindrome) OR remove 'g','l' -> "ooge" -> remove 'e' -> "oog" (not palindrome) OR remove 'g','l','e' -> "oog" -> remove 'g' -> "oo" (palindrome) Let's retrace: "google" -> remove 'l', 'e' -> "googe". LPS("googe") = "gg" or "oo". Length 2. 5-2=3 removals needed. Hmm, let's rethink google.
        # google, k=2. s_rev = elgoog.
        # LCS(google, elgoog)
        #   e l g o o g
        # g 0 0 1 1 1 1
        # o 0 0 1 2 2 2
        # o 0 0 1 2 3 3
        # g 0 0 1 2 3 4
        # l 0 1 1 2 3 4
        # e 1 1 1 2 3 4
        # LCS length = 4 ("goog"). n=6. Removals = 6 - 4 = 2. 2 <= k=2. So True. My manual trace was wrong.
        ("abacaba", 0, True),
        ("abacaba", 1, True), # Already a palindrome
        ("abc", 1, False), # Need 2 removals ("a", "b", "c") -> "b" or "a" or "c". LCS("abc", "cba") = "a" or "b" or "c". Length 1. n=3. Removals = 3-1=2. 2 > k=1. False.
        ("abc", 2, True), # Removals = 2. 2 <= k=2. True.
        ("topcoderopen", 5, True), # n=12. s_rev=neporedocot. LCS("topcoderopen", "neporedocot") = "opco" + "epo" = "opcoepo"? No. Let's compute.
        # LCS length should be 7 ("opcoepo"). n=12. Removals = 12 - 7 = 5. 5 <= k=5. True.
        ("aaaaaaaaaa", 0, True),
        ("aaaaaaaaab", 1, True), # remove 'b'. LPS="aaaaaaaaaa". n=11. LPS len=10. Removals = 1. 1 <= k=1. True.
        ("abcdefgh", 7, True), # remove all but one char. n=8. LPS len=1. Removals = 7. 7 <= k=7. True.
        ("abcdefgh", 6, False), # Removals = 7. 7 > k=6. False.
        ("qwertyuiopasdfghjklzxcvbnm", 25, True), # n=26. LPS len=1. Removals = 25. 25 <= k=25. True.
        ("qwertyuiopasdfghjklzxcvbnm", 24, False), # Removals = 25. 25 > k=24. False.
        ("a", 0, True),
        ("a", 1, True),
        ("aba", 0, True),
        ("abca", 1, True), # remove 'c'. LPS="aba". n=4. LPS len=3. Removals = 1. 1 <= k=1. True.
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (s_input, k_input, expected_output) in enumerate(test_cases):
        result = is_k_palindrome(s_input, k_input)
        passed = result == expected_output
        print(f"Test {i+1}: Input (s='{s_input}', k={k_input}), Output={result}, Expected={expected_output} -> {'True' if passed else 'False'}")
        if passed:
            correct_count += 1

    print(f"\nPassed {correct_count} out of {total_tests} tests.")

# Execute the solver function
solve()