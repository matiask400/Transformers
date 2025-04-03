import sys
import io

# Define the solution function
def removePalindromeSub(s: str) -> int:
  """
  Calculates the minimum number of steps to make the given string empty
  by removing palindromic subsequences.

  Args:
    s: The input string consisting only of 'a' and 'b'.

  Returns:
    The minimum number of steps (1 or 2 for non-empty strings).
  """
  # Constraint: 1 <= s.length <= 1000, so s is never empty.

  # Check if the string is a palindrome
  # A string is a palindrome if it reads the same forwards and backwards.
  if s == s[::-1]:
    # If s is already a palindrome, we can remove the entire string
    # as one palindromic subsequence in a single step.
    return 1
  else:
    # If s is not a palindrome, and consists only of 'a's and 'b's:
    # We can consider two specific palindromic subsequences:
    # 1. The subsequence consisting of all 'a's (e.g., "aaa..."). This is always a palindrome.
    # 2. The subsequence consisting of all 'b's (e.g., "bbb..."). This is also always a palindrome.
    #
    # We can remove all 'a's in one step. The remaining string will consist only of 'b's.
    # Then, we can remove all remaining 'b's in a second step (since "bbb..." is a palindrome).
    # Therefore, any non-palindromic string consisting only of 'a's and 'b's
    # can be emptied in exactly 2 steps.
    # It requires more than 1 step because it's not a palindrome itself.
    return 2

# --- Testing Framework ---
def run_tests():
    """
    Runs predefined test cases against the removePalindromeSub function
    and prints the results in the specified format.
    """
    test_cases = [
        ("ababa", 1),
        ("abb", 2),
        ("baabb", 2),
        ("bbaaba", 2),
        ("aaaaa", 1),
        ("bbbbb", 1),
        ("a", 1),
        ("b", 1),
        ("ab", 2),
        ("ba", 2),
        ("aabb", 2),
        ("bbaa", 2),
        ("bab", 1),
        ("aba", 1),
        ("aaabaaa", 1),
        ("aaabbaa", 2),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture prints for final output formatting
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, (input_s, expected_output) in enumerate(test_cases):
        # Execute the function with the test case input
        result = removePalindromeSub(input_s)
        # Check if the result matches the expected output
        passed = result == expected_output
        # Print 'True' or 'False' for each test
        print(passed)
        if passed:
            correct_count += 1
        # Optional: Print details for failed tests to stderr for debugging
        # if not passed:
        #     print(f"Test {i+1} Failed: Input='{input_s}', Expected={expected_output}, Got={result}", file=sys.stderr)

    # Restore stdout
    sys.stdout = old_stdout
    # Print the captured True/False results
    print(captured_output.getvalue(), end="")

    # Print the final summary line
    print(f"{correct_count}/{total_tests}")

# --- Main Execution ---
if __name__ == '__main__':
    # Run the tests when the script is executed
    run_tests()