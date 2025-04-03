def balancedStringSplit(s):
    """
    Splits a balanced string into the maximum amount of balanced strings.

    Args:
        s: A balanced string consisting of 'L' and 'R' characters.

    Returns:
        The maximum amount of split balanced strings.
    """
    balance = 0
    count = 0
    for char in s:
        if char == 'L':
            balance += 1
        elif char == 'R':
            balance -= 1
        if balance == 0:
            count += 1
    return count

def run_tests():
    test_cases = [
        {"input": "RLRRLLRLRL", "expected_output": 4},
        {"input": "RLLLLRRRLR", "expected_output": 3},
        {"input": "LLLLRRRR", "expected_output": 1},
        {"input": "RLRRRLLRLL", "expected_output": 2},
        {"input": "RL", "expected_output": 1},
        {"input": "RRLL", "expected_output": 1},
        {"input": "LLRR", "expected_output": 1},
        {"input": "RRRLLL", "expected_output": 1},
        {"input": "LLLRRR", "expected_output": 1},
        {"input": "RLRLRLRL", "expected_output": 4},
        {"input": "RRRRLLLL", "expected_output": 1},
        {"input": "LLLLRRRRRLRL", "expected_output": 2},
    ]
    correct_count = 0
    for i, test_case in enumerate(test_cases):
        input_s = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = balancedStringSplit(input_s)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()