import math

def is_palindrome(x: int) -> bool:
    """
    Checks if an integer is a palindrome without converting it to a string.

    Args:
        x: An integer.

    Returns:
        True if x is a palindrome, False otherwise.
    """
    # Rule 1: Negative numbers are not palindromes because of the '-' sign.
    if x < 0:
        return False

    # Rule 2: Numbers ending in 0 (except 0 itself) cannot be palindromes.
    # If a number ends in 0, its reverse must start with 0 (unless it's just 0).
    if x != 0 and x % 10 == 0:
        return False

    # Rule 3: Single digit numbers are always palindromes.
    # This is implicitly handled by the loop below, but could be an explicit check.
    # if 0 <= x <= 9:
    #     return True

    reversed_half = 0
    original_x = x # Keep a copy if needed for full reversal, but not for half-reversal

    # Reverse the second half of the number
    # Stop when the remaining number (x) is less than or equal to the reversed half
    while x > reversed_half:
        digit = x % 10
        reversed_half = reversed_half * 10 + digit
        x //= 10 # Use integer division

    # After the loop, x contains the first half and reversed_half contains the reversed second half.
    # Example 1: x = 1221
    # Iter 1: digit=1, reversed_half=1, x=122 (x > reversed_half)
    # Iter 2: digit=2, reversed_half=12, x=12 (x == reversed_half) -> loop stops
    # Check: x == reversed_half (12 == 12) -> True

    # Example 2: x = 121
    # Iter 1: digit=1, reversed_half=1, x=12 (x > reversed_half)
    # Iter 2: digit=2, reversed_half=12, x=1 (x < reversed_half) -> loop stops
    # Check: x == reversed_half (1 == 12) -> False
    # Check: x == reversed_half // 10 (1 == 12 // 10 == 1) -> True

    # If the number has an even number of digits, x and reversed_half should be equal.
    # If the number has an odd number of digits, the middle digit will be the last digit left in x
    # when the loop ends. We can discard the middle digit from reversed_half by integer division.
    return x == reversed_half or x == reversed_half // 10


# --- Test Framework ---
def run_tests():
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (-101, False),
        (0, True),
        (9, True),
        (12345, False),
        (12321, True),
        (11, True),
        (1, True),
        (1221, True),
        (123321, True),
        (2**31 - 1, False), # Max positive int (not a palindrome)
        (1000021, False), # Example from LeetCode discussions
        (120021, False), # Another example
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_val, expected_output) in enumerate(test_cases):
        result = is_palindrome(input_val)
        is_correct = result == expected_output
        print(f"Test {i+1}: Input={input_val}, Output={result}, Expected={expected_output} -> {is_correct}")
        if is_correct:
            correct_count += 1

    print(f"\n{correct_count}/{total_tests} tests passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()