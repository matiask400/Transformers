def missingNumber(nums):
    """
    Finds the missing number in the range [0, n] in the given array nums.

    Args:
        nums: An array of n distinct numbers in the range [0, n].

    Returns:
        The only number in the range that is missing from the array.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def test_missingNumber():
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
        ([0,2,3],1)
    ]
    
    num_correct = 0
    total_tests = len(test_cases)
    
    for i, (nums, expected) in enumerate(test_cases):
        actual = missingNumber(nums)
        if actual == expected:
            print(True)
            num_correct += 1
        else:
            print(False)
            print(f"Test Case {i+1}: Input: {nums}, Expected: {expected}, Actual: {actual}")
    
    print(f"{num_correct}/{total_tests}")

test_missingNumber()