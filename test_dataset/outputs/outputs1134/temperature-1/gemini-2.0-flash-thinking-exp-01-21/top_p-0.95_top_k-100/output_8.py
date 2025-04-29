def move_zeros(nums):
    """
    Moves all 0's to the end of the array while maintaining the relative order of non-zero elements.

    Args:
        nums: An integer array.

    Returns:
        None. Modifies nums in-place.
    """
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(nums)):
        nums[i] = 0

def test_move_zeros():
    """
    Tests the move_zeros function with several test cases.
    Prints 'True' for each test passed and 'False' for each test failed.
    Finally prints the number of correct tests over the total.
    """
    test_cases = [
        {"input": [0, 1, 0, 3, 12], "expected": [1, 3, 12, 0, 0]},
        {"input": [0], "expected": [0]},
        {"input": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5]},
        {"input": [0, 0, 0, 0, 0], "expected": [0, 0, 0, 0, 0]},
        {"input": [1, 0, 2, 0, 3], "expected": [1, 2, 3, 0, 0]},
        {"input": [], "expected": []},
        {"input": [0, 0, 1], "expected": [1, 0, 0]},
        {"input": [1, 0, 0], "expected": [1, 0, 0]},
        {"input": [4, 2, 4, 0, 0, 3, 0, 5, 1, 0], "expected": [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]},
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        nums = test_case["input"][:]  # Create a copy to avoid modifying original test case
        expected_output = test_case["expected"]
        move_zeros(nums)
        if nums == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_move_zeros()