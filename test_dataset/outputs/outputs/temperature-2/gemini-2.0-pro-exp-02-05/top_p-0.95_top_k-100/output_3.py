def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays.
    """
    merged_array = sorted(nums1 + nums2)
    total_length = len(merged_array)

    if total_length % 2 == 0:
        median = (merged_array[total_length // 2 - 1] + merged_array[total_length // 2]) / 2.0
    else:
        median = merged_array[total_length // 2]

    return median


def test_find_median_sorted_arrays():
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ]

    passed_tests = 0
    total_tests = len(test_cases)

    for nums1, nums2, expected_output in test_cases:
        actual_output = find_median_sorted_arrays(nums1, nums2)
        result = actual_output == expected_output
        print(result)
        if result:
            passed_tests += 1

    print(f"{passed_tests}/{total_tests}")


if __name__ == "__main__":
    test_find_median_sorted_arrays()