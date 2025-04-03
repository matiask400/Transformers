import sys
import io

def solve():
    """
    Implements the regular expression matching logic using dynamic programming
    and runs test cases.
    """

    def isMatch(s: str, p: str) -> bool:
        """
        Checks if the input string s matches the pattern p.

        Args:
            s: The input string.
            p: The pattern string with support for '.' and '*'.

        Returns:
            True if s matches p entirely, False otherwise.
        """
        m, n = len(s), len(p)

        # dp[i][j] will be True if the first i characters of s
        # match the first j characters of p
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, .* that can match an empty string
        # dp[0][j] represents matching empty string s="" with pattern p[:j]
        for j in range(1, n + 1):
            # The j-th character in p is p[j-1]
            if p[j - 1] == '*':
                # '*' must follow a character, so j must be at least 2
                # Check if the pattern p[:j] without the 'x*' part (i.e., p[:j-2])
                # matches the empty string.
                if j >= 2:
                    dp[0][j] = dp[0][j - 2]
            # If p[j-1] is not '*', it cannot match an empty string if j > 0
            # and dp[0][j] remains False (default initialization)

        # Fill the rest of the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current characters to consider: s[i-1] and p[j-1]

                # Case 1: The current pattern character p[j-1] is NOT '*'
                if p[j - 1] != '*':
                    # Check if current characters match (s[i-1] == p[j-1] or p[j-1] == '.')
                    match = (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                    # If they match, the result depends on the previous state dp[i-1][j-1]
                    if match:
                        dp[i][j] = dp[i - 1][j - 1]
                    # If they don't match, dp[i][j] remains False

                # Case 2: The current pattern character p[j-1] IS '*'
                else:
                    # '*' must follow a character, so j must be at least 2
                    # The character preceding '*' is p[j-2]

                    # Option 1: '*' matches zero occurrences of the preceding element p[j-2].
                    # In this case, the result depends on whether s[:i] matches p[:j-2].
                    option1 = dp[i][j - 2] # Requires j >= 2, handled by loop start and check below

                    # Option 2: '*' matches one or more occurrences of the preceding element p[j-2].
                    # This is possible only if the current character s[i-1] matches p[j-2].
                    match_prev = (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                    option2 = False
                    if match_prev:
                         # If s[i-1] matches p[j-2], then we check if s[:i-1] matches p[:j]
                         # (because '*' allows matching multiple s characters with the same p[j-2]* part)
                        option2 = dp[i - 1][j]

                    # The result is True if either option is True
                    if j >= 2: # Ensure p[j-2] is valid
                       dp[i][j] = option1 or option2
                    # If j < 2 and p[j-1] is '*', the pattern is invalid based on constraints,
                    # but robust code might handle it. Here, we rely on j starting from 1
                    # and the check j>=2. If j=1, p[0] cannot be '*'.

        # The final result is whether the entire string s matches the entire pattern p
        return dp[m][n]

    # Test cases
    test_cases = [
        {"input": ("aa", "a"), "expected": False},
        {"input": ("aa", "a*"), "expected": True},
        {"input": ("ab", ".*"), "expected": True},
        {"input": ("aab", "c*a*b"), "expected": True},
        {"input": ("mississippi", "mis*is*p*."), "expected": False},
        {"input": ("", ""), "expected": True},
        {"input": ("a", ""), "expected": False},
        {"input": ("", "a"), "expected": False},
        {"input": ("", "a*"), "expected": True},
        {"input": ("", ".*"), "expected": True},
        {"input": ("", "c*a*"), "expected": True},
        {"input": ("a", "ab*"), "expected": True},
        {"input": ("a", ".*..a*"), "expected": False}, # Tricky: .* matches 'a', then .. needs two more chars
        {"input": ("bbbba", ".*a*a"), "expected": True},
        {"input": ("ab", ".*c"), "expected": False},
        {"input": ("aaa", "a*a"), "expected": True},
        {"input": ("aaa", "ab*a*c*a"), "expected": True},
        {"input": ("abcd", "d*"), "expected": False}, # '*' matches preceding 'd', not 'abcd'
        {"input": ("aasdfasdfasdfasdf", "aasdf.*asdf.*asdf.*asdf"), "expected": True},
        {"input": ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"), "expected": False}, # Mismatch at the end
        {"input": ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*b"), "expected": True},
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture prints
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, test in enumerate(test_cases):
        s_input, p_input = test["input"]
        expected_output = test["expected"]
        actual_output = isMatch(s_input, p_input)
        result = actual_output == expected_output
        print(result)
        if result:
            correct_count += 1

    # Restore stdout
    sys.stdout = old_stdout
    # Get captured output
    output_str = captured_output.getvalue()

    # Print captured output
    print(output_str, end="")
    # Print summary
    print(f"{correct_count}/{total_tests}")

# Execute the solve function
solve()