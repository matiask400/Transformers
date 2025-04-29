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

def run_tests(tests):
    correct_count = 0
    total_tests = len(tests)

    for i, (nums1, nums2, expected_output) in enumerate(tests):
        result = findMedianSortedArrays(nums1, nums2)
        if result == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_count}/{total_tests} tests correct")

if __name__ == "__main__":
    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ]
    run_tests(tests)