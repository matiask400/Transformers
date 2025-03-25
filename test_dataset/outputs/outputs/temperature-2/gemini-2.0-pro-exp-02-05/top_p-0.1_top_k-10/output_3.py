def findMedianSortedArrays(nums1, nums2):
    merged_array = sorted(nums1 + nums2)
    total_length = len(merged_array)

    if total_length % 2 == 0:
        median = (merged_array[total_length // 2 - 1] + merged_array[total_length // 2]) / 2.0
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
        ([1,2,3], [4,5,6], 3.5),
        ([1,2], [-1,3], 1.5)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for nums1, nums2, expected in test_cases:
        result = findMedianSortedArrays(nums1, nums2)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_tests}")

run_tests(findMedianSortedArrays)