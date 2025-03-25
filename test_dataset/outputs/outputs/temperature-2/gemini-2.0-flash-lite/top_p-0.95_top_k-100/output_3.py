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
    n = len(merged_array)
    if n % 2 == 0:
        # Even number of elements, median is the average of the middle two
        mid1 = merged_array[n // 2 - 1]
        mid2 = merged_array[n // 2]
        median = (mid1 + mid2) / 2.0
    else:
        # Odd number of elements, median is the middle element
        median = float(merged_array[n // 2])
    return median

def test_find_median_sorted_arrays():
    """
    Tests the find_median_sorted_arrays function.
    """
    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 2], [7, 8, 9], 7.0)

    ]

    correct_count = 0
    for i, (nums1, nums2, expected_output) in enumerate(tests):
        result = find_median_sorted_arrays(nums1, nums2)
        if abs(result - expected_output) < 1e-5:  # Using a small tolerance for float comparisons
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test {i+1} Failed. Expected: {expected_output}, Got: {result}")

    print(f"{correct_count}/{len(tests)}")


test_find_median_sorted_arrays()