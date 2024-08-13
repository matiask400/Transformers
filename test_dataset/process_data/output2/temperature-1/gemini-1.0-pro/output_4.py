if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2], 2.00000),
        ([1, 2], [3, 4], 2.50000),
        ([0, 0], [0, 0], 0.00000),
        ([], [1], 1.00000),
        ([2], [], 2.00000)
    ]

    for nums1, nums2, expected in test_cases:
        result = find_median_sorted_arrays(nums1, nums2)
        passed = result == expected