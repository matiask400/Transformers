def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
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

    if merged_length % 2 == 0:
        # Even length, median is the average of the middle two elements
        mid1 = merged_array[merged_length // 2 - 1]
        mid2 = merged_array[merged_length // 2]
        return (mid1 + mid2) / 2.0
    else:
        # Odd length, median is the middle element
        return float(merged_array[merged_length // 2])

def test_find_median_sorted_arrays():
    """Tests the findMedianSortedArrays function."""
    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 2, 3], [4, 5, 6], 3.5),
        ([4, 5, 6], [1, 2, 3], 3.5),
        ([1, 3], [2, 7], 3.0),
        ([1, 2, 3], [1, 2, 3], 2.0)
    ]
    correct_tests = 0
    for nums1, nums2, expected_median in tests:
        result = findMedianSortedArrays(nums1, nums2)
        if abs(result - expected_median) < 1e-5:  # Use a small tolerance for floating-point comparisons
            print(True)
            correct_tests += 1
        else:
            print(False)
    print(f"{correct_tests}/{len(tests)}")

if __name__ == '__main__':
    test_find_median_sorted_arrays()