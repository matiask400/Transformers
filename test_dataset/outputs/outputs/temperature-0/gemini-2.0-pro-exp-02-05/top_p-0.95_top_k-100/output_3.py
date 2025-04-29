def findMedianSortedArrays(nums1, nums2):
    merged_array = sorted(nums1 + nums2)
    total_length = len(merged_array)

    if total_length % 2 == 0:
        mid1 = merged_array[total_length // 2 - 1]
        mid2 = merged_array[total_length // 2]
        median = (mid1 + mid2) / 2.0
    else:
        median = float(merged_array[total_length // 2])

    return median

def run_tests(findMedianSortedArrays):
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ]

    passed_tests = 0
    total_tests = len(test_cases)

    for nums1, nums2, expected in test_cases:
        result = findMedianSortedArrays(nums1, nums2)
        if result == expected:
            print("True")
            passed_tests += 1
        else:
            print("False")

    print(f"{passed_tests}/{total_tests}")

run_tests(findMedianSortedArrays)