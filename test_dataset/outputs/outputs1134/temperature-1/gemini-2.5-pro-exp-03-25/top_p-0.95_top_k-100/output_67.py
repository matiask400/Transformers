import math

def is_palindrome(x: int) -> bool:
    """
    Checks if an integer x is a palindrome without converting it to a string.

    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x: The integer to check.

    Returns:
        True if x is a palindrome, False otherwise.
    """
    # Rule 1: Negative numbers are not palindromes because of the '-' sign.
    if x < 0:
        return False

    # Rule 2: If the number ends in 0, to be a palindrome,
    # the first digit must also be 0. The only number satisfying this is 0 itself.
    if x % 10 == 0 and x != 0:
        return False

    # Rule 3: Single-digit numbers are always palindromes.
    # This is implicitly handled by the loop below, but good to note.
    # if 0 <= x < 10:
    #     return True

    reversed_half = 0
    original_x = x # We need to modify x, so keep a copy if full reversal was needed (not needed here)

    # Reverse the second half of the number
    # Loop until we've processed half the digits.
    # We know we've reached the middle when the remaining original number (x)
    # is less than or equal to the reversed half we've built.
    while x > reversed_half:
        digit = x % 10
        reversed_half = reversed_half * 10 + digit
        x //= 10 # Integer division to remove the last digit

    # After the loop, we have two cases:
    # 1. The original number had an even number of digits.
    #    The loop stops when x == reversed_half.
    #    Example: x = 1221
    #    - i1: digit=1, rev=1, x=122
    #    - i2: digit=2, rev=12, x=12
    #    Loop terminates because x (12) is not > reversed_half (12).
    #    Check: x == reversed_half (12 == 12) -> True
    #
    # 2. The original number had an odd number of digits.
    #    The loop stops when x < reversed_half. The middle digit
    #    is the last digit added to reversed_half and is irrelevant
    #    for the palindrome check. We can remove it by integer division.
    #    Example: x = 121
    #    - i1: digit=1, rev=1, x=12
    #    - i2: digit=2, rev=12, x=1
    #    Loop terminates because x (1) is not > reversed_half (12).
    #    Check: x == reversed_half // 10 (1 == 12 // 10) -> (1 == 1) -> True

    # Combine both checks:
    return x == reversed_half or x == reversed_half // 10


# --- Testing Framework ---
def run_tests():
    """
    Runs predefined test cases against the is_palindrome function and prints the results.
    """
    test_cases = [
        # Input, Expected Output
        (121, True),
        (-121, False),
        (10, False),
        (-101, False),
        (0, True),
        (1, True),
        (11, True),
        (123, False),
        (1221, True),
        (12321, True),
        (2147483647, False), # Max 32-bit int, not a palindrome
        (1001, True),
        (1000, False), # Ends in 0, not 0 itself
        (22, True),
        (23, False),
        (2332, True),
        (23432, True),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    print("Running tests...")
    for i, (input_val, expected_output) in enumerate(test_cases):
        result = is_palindrome(input_val)
        test_passed = (result == expected_output)
        print(f"Test #{i+1}: Input={input_val}, Expected={expected_output}, Got={result} -> {test_passed}")
        if test_passed:
            correct_count += 1

    print(f"\n{correct_count}/{total_tests} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()