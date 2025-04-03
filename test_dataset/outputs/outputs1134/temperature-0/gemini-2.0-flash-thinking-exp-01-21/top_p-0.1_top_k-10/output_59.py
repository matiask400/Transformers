def find_missing_number(nums):
    """
    Finds the missing number in an array of n distinct numbers in the range [0, n].

    Args:
        nums: A list of integers.

    Returns:
        The missing number in the range [0, n].
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def run_tests():
    """
    Runs test cases for the find_missing_number function.
    """
    test_cases = [
        {"input": [3, 0, 1], "expected": 2},
        {"input": [0, 1], "expected": 2},
        {"input": [9, 6, 4, 2, 3, 5, 7, 0, 1], "expected": 8},
        {"input": [0], "expected": 1},
        {"input": [1], "expected": 0},
        {"input": [0, 2, 3], "expected": 1},
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        nums = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = find_missing_number(nums)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()