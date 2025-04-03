def find_peak_element(nums):
    """
    Finds a peak element in an integer array and returns its index.

    Args:
        nums: An integer array.

    Returns:
        The index of a peak element.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

def test_find_peak_element():
    """
    Tests the find_peak_element function with several test cases.
    """
    test_cases = [
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([5, 4, 3, 2, 1], 0),
        ([3, 2, 1], 0),
        ([1, 2, 3], 2),
        ([3, 4, 5], 2),
        ([5, 4, 3], 0),
        ([1,5,3,7,2], 1)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (nums, expected) in enumerate(enumerate(test_cases)):
        actual = find_peak_element(nums)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {nums}, Expected: {expected}, Actual: {actual})")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_find_peak_element()