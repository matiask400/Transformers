def findMedianSortedArrays(nums1, nums2):
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
        median = (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2.0
    else:
        median = float(merged_array[n // 2])
    return median

def run_tests():
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1,2,3], [4,5,6], 3.5)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for nums1, nums2, expected_median in test_cases:
        result = findMedianSortedArrays(nums1, nums2)
        if result == expected_median:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_tests}")


if __name__ == "__main__":
    run_tests()