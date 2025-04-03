def find_median_sorted_arrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        The median of the merged sorted arrays.
    """
    merged_array = sorted(nums1 + nums2)
    n = len(merged_array)
    if n % 2 == 1:
        median = float(merged_array[n // 2])
    else:
        mid1 = merged_array[n // 2 - 1]
        mid2 = merged_array[n // 2]
        median = (mid1 + mid2) / 2.0
    return median

def run_tests():
    """
    Runs test cases for the find_median_sorted_arrays function.
    """
    test_cases = [
        (([1, 3], [2]), 2.0),
        (([1, 2], [3, 4]), 2.5),
        (([0, 0], [0, 0]), 0.0),
        (([], [1]), 1.0),
        (([2], []), 2.0),
        (([1, 2, 5], [3, 4]), 3.0),
        (([1, 2], [1, 2, 3]), 2.0)
    ]
    correct_tests = 0
    total_tests = len(test_cases)

    for i, (inputs, expected_output) in enumerate(test_cases):
        nums1, nums2 = inputs
        actual_output = find_median_sorted_arrays(nums1, nums2)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: nums1={nums1}, nums2={nums2}")
            print(f"  Expected Output: {expected_output}")
            print(f"  Actual Output:   {actual_output}")

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()