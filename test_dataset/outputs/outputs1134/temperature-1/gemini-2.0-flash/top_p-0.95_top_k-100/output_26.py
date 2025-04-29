def balancedStringSplit(s):
    """
    Splits a balanced string into the maximum amount of balanced substrings.

    Args:
        s: The balanced string to split.

    Returns:
        The maximum amount of split balanced strings.
    """
    count = 0
    balance = 0
    for char in s:
        if char == 'R':
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
        ("RLRL", 2),
        ("LRLR", 2) # Example where it should return 2.
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = balancedStringSplit(input_str)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Input: {input_str}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"{num_correct}/{total_tests}")

if __name__ == "__main__":
    test_balancedStringSplit()