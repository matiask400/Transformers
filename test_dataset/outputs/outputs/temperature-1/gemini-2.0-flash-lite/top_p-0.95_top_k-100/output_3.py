def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Finds the median of two sorted arrays.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        The median of the two sorted arrays.
    """
    merged_array = sorted(nums1 + nums2)
    merged_length = len(merged_array)

    if merged_length == 0:
        return 0.0

    if merged_length % 2 == 0:  # Even length
        mid1 = merged_array[merged_length // 2 - 1]
        mid2 = merged_array[merged_length // 2]
        median = (mid1 + mid2) / 2.0
    else:  # Odd length
        median = float(merged_array[merged_length // 2])

    return median

def test_find_median_sorted_arrays():
    """Tests the find_median_sorted_arrays function."""
    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 2, 3], [4, 5], 3.0),
        ([4, 5], [1, 2, 3], 3.0),
        ([1, 2, 3], [4], 2.5),
        ([1], [2,3,4], 2.5),
        ([-1, -2], [-3, -4, -5], -3.0),
        ([1, 3], [2, 7], 3.0)

    ]
    correct_tests = 0
    for i, (nums1, nums2, expected) in enumerate(tests):
        result = find_median_sorted_arrays(nums1, nums2)
        if abs(result - expected) < 1e-5:  # Using a tolerance for floating-point comparisons
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Actual: {result})")
    print(f"Correct tests: {correct_tests}/{len(tests)}")


if __name__ == '__main__':
    test_find_median_sorted_arrays()