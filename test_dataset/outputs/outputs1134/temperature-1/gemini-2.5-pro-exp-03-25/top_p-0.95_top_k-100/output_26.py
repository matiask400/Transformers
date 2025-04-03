import sys
import io

def balancedStringSplit(s: str) -> int:
    """
    Splits a balanced string into the maximum number of balanced substrings.

    A balanced string has an equal number of 'L' and 'R' characters.

    Args:
        s: The input balanced string.

    Returns:
        The maximum number of balanced substrings s can be split into.
    """
    balance = 0  # Tracks the balance of 'L' vs 'R'
    count = 0    # Counts the number of balanced substrings found

    for char in s:
        if char == 'L':
            balance += 1
        elif char == 'R':
            balance -= 1

        # If balance is 0, we've found a balanced substring
        if balance == 0:
            count += 1
            
    return count

def run_tests():
    """
    Runs predefined test cases against the balancedStringSplit function
    and prints the results.
    """
    test_cases = [
        ("RLRRLLRLRL", 4),
        ("RLLLLRRRLR", 3),
        ("LLLLRRRR", 1),
        ("RLRRRLLRLL", 2),
        ("RL", 1),
        ("RRLRLL", 2), 
        ("LLRR", 1),   
        ("LRLR", 2)    
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, (s_input, expected_output) in enumerate(test_cases):
        actual_output = balancedStringSplit(s_input)
        passed = actual_output == expected_output
        print(f"{passed}") # Print True or False for each test
        if passed:
            correct_tests += 1

    # Restore stdout
    sys.stdout = old_stdout
    
    # Print the captured output (True/False for each test)
    print(captured_output.getvalue(), end="")
    
    # Print the final summary
    print(f"{correct_tests} / {total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()