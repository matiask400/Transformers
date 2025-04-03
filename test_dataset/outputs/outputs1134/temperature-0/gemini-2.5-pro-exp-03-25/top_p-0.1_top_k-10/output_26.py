import sys
import io

# Define the solution function
def solve(s: str) -> int:
    """
    Splits a balanced string s into the maximum amount of balanced strings.

    A balanced string has an equal quantity of 'L' and 'R' characters.
    The function finds the maximum number of contiguous balanced substrings
    that the input string `s` can be divided into.

    Args:
        s: A balanced string containing only 'L' and 'R'.
           Constraints: 1 <= s.length <= 1000, s[i] is 'L' or 'R', s is balanced.

    Returns:
        The maximum number of split balanced strings.
    """
    # Initialize count of balanced substrings found
    count = 0
    # Initialize balance tracker (e.g., +1 for 'R', -1 for 'L')
    balance = 0

    # Iterate through the string character by character
    for char in s:
        # Update balance based on the character
        if char == 'L':
            balance -= 1
        elif char == 'R':
            balance += 1
        # No need to check for other characters due to problem constraints.

        # If balance is 0, it means the substring processed so far
        # from the start of the current segment is balanced.
        # Since we want the maximum number of splits, we count this
        # balanced substring and continue processing the rest of the string.
        if balance == 0:
            count += 1

    # Since the input string `s` is guaranteed to be balanced, the final
    # balance after iterating through the entire string will be 0.
    # The `count` variable correctly accumulates the number of times
    # a balanced prefix (of the remaining string) was identified.
    return count

# Define the test cases based on the examples and additional scenarios
test_cases = [
    # Example 1
    ("RLRRLLRLRL", 4),
    # Example 2
    ("RLLLLRRRLR", 3),
    # Example 3
    ("LLLLRRRR", 1),
    # Example 4
    ("RLRRRLLRLL", 2),
    # Additional simple cases
    ("RL", 1),
    ("LR", 1), # Although not explicitly given, this is a valid balanced string
    # Cases with multiple splits
    ("RLRL", 2),
    ("LRLR", 2),
    # Cases where the first split is the whole string
    ("RRLL", 1),
    ("LLRR", 1),
    # Longer cases
    ("RLRLRLRLRL", 5), # 10 chars, 5 splits ("RL", "RL", "RL", "RL", "RL")
    ("LLRRLLRR", 2),   # 8 chars, 2 splits ("LLRR", "LLRR")
    ("RRLLRRLL", 2),   # 8 chars, 2 splits ("RRLL", "RRLL")
    # Case with nested balance
    ("RRLRRLRLLL", 2) # Splits into "RRLRRLRL" and "LL" is wrong. Should be "RRLRRLRL" (bal=0), "LL" (bal=-2) -> No.
                       # Let's trace "RRLRRLRLLL":
                       # R: +1
                       # RR: +2
                       # RRL: +1
                       # RRLR: +2
                       # RRLRR: +3
                       # RRLRRL: +2
                       # RRLRRLR: +3
                       # RRLRRLRL: +2
                       # RRLRRLRLL: +1
                       # RRLRRLRLLL: 0.  -> Only 1 split: the entire string.
                       # Re-evaluating the test case: "RRLRRLRLLL" has 6 R and 4 L, so it's not balanced.
                       # Let's use a valid balanced string: "RRLRLL"
                       # R: +1
                       # RR: +2
                       # RRL: +1
                       # RRLR: +2
                       # RRLRL: +1
                       # RRLRLL: 0. -> 1 split.
    ("RRLRLL", 1),
    # Another complex case: "RLRLRRLLRL"
    # R: +1
    # RL: 0 -> Split 1 ("RL")
    # R: +1
    # RL: 0 -> Split 2 ("RL")
    # R: +1
    # RR: +2
    # RRL: +1
    # RRLL: 0 -> Split 3 ("RRLL")
    # R: +1
    # RL: 0 -> Split 4 ("RL")
    ("RLRLRRLLRL", 4),

]

# Function to run tests and print results in the specified format
def run_tests_and_print_results(test_cases):
    """
    Runs the provided test cases against the solve function and prints the
    results according to the specified format.
    - Prints 'True' for each passed test.
    - Prints 'False' for each failed test.
    - Finally, prints the summary 'correct_count/total_tests'.
    """
    correct_count = 0
    total_tests = len(test_cases)

    results_log = [] # To store 'True' or 'False' for each test's outcome

    for i, (s_input, expected_output) in enumerate(test_cases):
        # Execute the solve function
        try:
            result = solve(s_input)
            # Compare the result with the expected output
            is_correct = (result == expected_output)
        except Exception as e:
            # In case the solve function raises an unexpected error
            print(f"Test {i+1} ('{s_input}') failed with error: {e}", file=sys.stderr)
            is_correct = False

        results_log.append(str(is_correct)) # Append 'True' or 'False' as a string
        if is_correct:
            correct_count += 1

    # Print the results for each test ('True' or 'False') on separate lines
    for result_str in results_log:
        print(result_str)

    # Print the final summary: number of correct tests / total tests
    print(f"{correct_count}/{total_tests}")


# Execute the tests when the script is run directly
if __name__ == "__main__":
    run_tests_and_print_results(test_cases)