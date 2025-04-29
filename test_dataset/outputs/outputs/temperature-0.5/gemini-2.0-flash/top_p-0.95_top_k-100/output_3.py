def find_median_sorted_arrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        The median of the two sorted arrays.
    """
    merged_array = sorted(nums1 + nums2)
    length = len(merged_array)

    if length % 2 == 0:
        median = (merged_array[length // 2 - 1] + merged_array[length // 2]) / 2.0
    else:
        median = float(merged_array[length // 2])

    return median


def test_find_median_sorted_arrays():
    """
    Tests the find_median_sorted_arrays function.
    """
    test_cases = [
        ([1, 3], [2], 2.00000),
        ([1, 2], [3, 4], 2.50000),
        ([0, 0], [0, 0], 0.00000),
        ([], [1], 1.00000),
        ([2], [], 2.00000),
        ([1, 3], [2, 4], 2.5)
    ]

    num_passed = 0
    total_tests = len(test_cases)

    for nums1, nums2, expected in test_cases:
        result = find_median_sorted_arrays(nums1, nums2)
        if abs(result - expected) < 1e-5:  # Compare floating-point numbers with tolerance
            print("True")
            num_passed += 1
        else:
            print("False")

    print(f"{num_passed}/{total_tests}")


if __name__ == '__main__':
    test_find_median_sorted_arrays()