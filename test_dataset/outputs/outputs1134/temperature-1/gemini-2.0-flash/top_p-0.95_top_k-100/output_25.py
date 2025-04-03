def find_median_sorted_arrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.

    Args:
        nums1 (list): The first sorted array.
        nums2 (list): The second sorted array.

    Returns:
        float: The median of the two sorted arrays.
    """
    merged_array = sorted(nums1 + nums2)
    total_length = len(merged_array)

    if total_length % 2 == 0:
        mid1 = merged_array[total_length // 2 - 1]
        mid2 = merged_array[total_length // 2]
        return (mid1 + mid2) / 2.0
    else:
        return float(merged_array[total_length // 2])


def test_find_median_sorted_arrays():
    """
    Tests the find_median_sorted_arrays function.
    """
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 5], [2, 3, 4], 3.0),
        ([1, 3], [2, 7], 2.5)

    ]

    correct_count = 0
    total_count = len(test_cases)

    for nums1, nums2, expected in test_cases:
        result = find_median_sorted_arrays(nums1, nums2)
        if abs(result - expected) < 1e-5:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")


if __name__ == '__main__':
    test_find_median_sorted_arrays()