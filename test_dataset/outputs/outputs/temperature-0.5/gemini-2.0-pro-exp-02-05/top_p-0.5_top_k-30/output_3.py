def findMedianSortedArrays(nums1, nums2):
    merged_array = sorted(nums1 + nums2)
    total_length = len(merged_array)

    if total_length % 2 == 0:
        mid1 = merged_array[total_length // 2 - 1]
        mid2 = merged_array[total_length // 2]
        median = (mid1 + mid2) / 2.0
    else:
        median = merged_array[total_length // 2]

    return median

def run_tests(findMedianSortedArrays):
    test_cases = [
        ([1, 3], [2], 2.00000),
        ([1, 2], [3, 4], 2.50000),
        ([0, 0], [0, 0], 0.00000),
        ([], [1], 1.00000),
        ([2], [], 2.00000),
    ]

    passed_tests = 0
    total_tests = len(test_cases)

    for i, (nums1, nums2, expected) in enumerate(test_cases):
        result = findMedianSortedArrays(nums1, nums2)
        if result == expected:
            print(f"Test {i + 1}: True")
            passed_tests += 1
        else:
            print(f"Test {i + 1}: False")

    print(f"\n{passed_tests}/{total_tests} tests passed.")

run_tests(findMedianSortedArrays)