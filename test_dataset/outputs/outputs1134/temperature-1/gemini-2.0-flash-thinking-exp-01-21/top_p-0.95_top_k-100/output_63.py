def find_peak_element(nums):
    """
    Finds a peak element in an array.

    Args:
        nums: An integer array.

    Returns:
        The index of a peak element.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

def test_find_peak_element():
    test_cases = [
        {"input": [1, 2, 3, 1], "expected_output": 2},
        {"input": [1, 2, 1, 3, 5, 6, 4], "expected_output": 5},
        {"input": [1], "expected_output": 0},
        {"input": [1, 2], "expected_output": 1},
        {"input": [2, 1], "expected_output": 0},
        {"input": [1,2,3,4,5], "expected_output": 4},
        {"input": [5,4,3,2,1], "expected_output": 0},
        {"input": [3,2,1,5,6], "expected_output": 4},
        {"input": [1,2,3,2,1], "expected_output": 2},
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        nums = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = find_peak_element(nums)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)
        # Optionally print details of failed tests for debugging
        # if actual_output != expected_output:
        #     print(f"Test {i+1} Failed: Input={nums}, Expected={expected_output}, Actual={actual_output}")

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_find_peak_element()