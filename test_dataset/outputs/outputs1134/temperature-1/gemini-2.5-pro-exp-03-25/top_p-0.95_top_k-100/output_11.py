import sys
import io

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Determines if the input string s matches the pattern p using dynamic programming.

        Args:
            s: The input string.
            p: The pattern string with support for '.' and '*'.

        Returns:
            True if s matches p entirely, False otherwise.
        """
        n = len(s)
        m = len(p)

        # dp[i][j] will be True if the first i characters of s
        # match the first j characters of p.
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Base cases for p: Handle patterns like a*, a*b*, .* that can match an empty string s.
        # dp[0][j] corresponds to matching empty string s="" with pattern p[:j]
        for j in range(1, m + 1):
            # The j-th character of p is p[j-1]
            if p[j-1] == '*':
                # '*' must match zero occurrences of the preceding element p[j-2].
                # This is only possible if the pattern up to p[j-3] matched the empty string.
                # Requires j >= 2 because '*' must have a preceding character.
                if j >= 2:
                    dp[0][j] = dp[0][j-2]
                # If j < 2 (i.e., j=1), p[0] is '*', which is invalid by problem constraints,
                # but if allowed, dp[0][1] would be False. dp[0][j-2] handles this correctly
                # as dp[0][-1] isn't accessed.

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Current characters: s_char = s[i-1], p_char = p[j-1]

                # Case 1: The current pattern character p[j-1] is NOT '*'
                if p[j-1] != '*':
                    # Match occurs if the previous substrings matched (dp[i-1][j-1])
                    # AND the current characters match.
                    match_current = (p[j-1] == s[i-1] or p[j-1] == '.')
                    if match_current and dp[i-1][j-1]:
                        dp[i][j] = True

                # Case 2: The current pattern character p[j-1] IS '*'
                else:
                    # '*' requires a preceding character p[j-2]. (j >= 2 guaranteed by constraints)
                    # preceding_char = p[j-2]

                    # Option A: '*' matches zero occurrences of p[j-2].
                    # The result depends on whether s[:i] matches p[:j-2] (ignoring p[j-2]p[j-1]).
                    option_zero = dp[i][j-2]

                    # Option B: '*' matches one or more occurrences of p[j-2].
                    # This requires the current string character s[i-1] to match p[j-2].
                    match_preceding = (p[j-2] == s[i-1] or p[j-2] == '.')
                    option_one_or_more = False
                    if match_preceding and dp[i-1][j]:
                         # If s[i-1] matches p[j-2], then we need to check if
                         # s[:i-1] matched the pattern p[:j]. The '*' allows
                         # the pattern p[:j] (which includes p[j-2]*) to potentially
                         # match one more character s[i-1].
                        option_one_or_more = True

                    # dp[i][j] is True if either option A or option B is possible.
                    dp[i][j] = option_zero or option_one_or_more

        # The final result is whether the entire string s matches the entire pattern p
        return dp[n][m]

def run_tests():
    """
    Runs test cases against the Solution.isMatch method.
    """
    sol = Solution()
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "", True),
        ("a", "", False),
        ("", "a", False),
        ("", "a*", True),
        ("", ".*", True),
        ("a", "ab*", True), # b* matches zero 'b's
        ("a", ".*c", False), # .* matches 'a', but 'c' doesn't match end of string
        ("aaa", "a*a", True), # a* matches "aa", last "a" matches third "a"
        ("aaa", "ab*a*c*a", True), # b* matches zero, a* matches "aa", c* matches zero, a matches "a"
        ("bbbba", ".*a*a", True), # .* matches bbbb, a* matches zero a's, last a matches the 'a'
        ("ab", ".*c", False),
        ("abcd", "d*", False), # '*' needs preceding char, but "d*" doesn't match "abcd"
        ("abcd", ".*d", True), # .* matches abc, d matches d
        ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False), # Mismatch at the end
        ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*b", True), # Matches
        ("abc", ".*", True),
        ("abc", ".", False), # '.' matches only one char
        ("abc", "..", False), # '..' matches only two chars
        ("abc", "...", True),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture prints
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, (s, p, expected) in enumerate(test_cases):
        result = sol.isMatch(s, p)
        passed = result == expected
        print(passed)
        if passed:
            correct_count += 1
        # Optional: Print details for failed tests
        # else:
        #     print(f"Test {i+1} Failed: s='{s}', p='{p}'. Expected {expected}, Got {result}", file=sys.stderr)

    # Restore stdout
    sys.stdout = old_stdout
    # Print captured output
    print(captured_output.getvalue(), end="")


    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    run_tests()