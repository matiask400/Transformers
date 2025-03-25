def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Finds the median of two sorted arrays.

    Args:
        nums1: The first sorted array.
        nums2: The second sorted array.

    Returns:
        The median of the two sorted arrays.
    """
    merged = sorted(nums1 + nums2)
    merged_len = len(merged)

    if merged_len == 0:
        return 0.0

    if merged_len % 2 == 0:
        # Even length, median is the average of the middle two elements
        mid1 = merged_len // 2 - 1
        mid2 = merged_len // 2
        return (merged[mid1] + merged[mid2]) / 2.0
    else:
        # Odd length, median is the middle element
        mid = merged_len // 2
        return float(merged[mid])


def run_tests():
    """Runs the test cases and prints the results."""
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 2, 3], [4, 5, 6], 3.5),
        ([4,5,6], [1,2,3], 3.5),
        ([1,3], [2,7], 3),
        ([1,2,3,4], [5,6,7,8], 4.5)
    ]
    correct_count = 0
    total_tests = len(test_cases)

    for i, (nums1, nums2, expected_median) in enumerate(test_cases):
        result = findMedianSortedArrays(nums1, nums2)
        if abs(result - expected_median) < 1e-5:  # Handle floating-point comparisons
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"Correct tests: {correct_count}/{total_tests}")

run_tests()