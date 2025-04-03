def balancedStringSplit(s):
    """
    Splits a balanced string into the maximum amount of balanced strings.

    Args:
        s: The balanced string.

    Returns:
        The maximum amount of split balanced strings.
    """
    balance = 0
    count = 0
    for char in s:
        if char == 'L':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            count += 1
    return count

def test_balancedStringSplit():
    """
    Tests the balancedStringSplit function with several test cases.
    """
    test_cases = [
        ("RLRRLLRLRL", 4),
        ("RLLLLRRRLR", 3),
        ("LLLLRRRR", 1),
        ("RLRRRLLRLL", 2),
        ("RL", 1),
        ("LR", 1),
        ("RRLL", 1),
        ("LLRR", 1),
        ("RLRLRLRL", 4),
        ("LRLRLRLR", 4)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = balancedStringSplit(input_str)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {input_str}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"\n{correct_count}/{total_tests} correct")

if __name__ == "__main__":
    test_balancedStringSplit()