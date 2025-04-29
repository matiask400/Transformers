def shortest_subarray_to_remove(arr):
    """
    Given an integer array `arr`, remove a subarray (can be empty) from `arr` such that the remaining elements in `arr` are non-decreasing.
    A subarray is a contiguous subsequence of the array.
    Return the length of the shortest subarray to remove.
    """
    n = len(arr)
    if n <= 1:
        return 0

    # Find the length of the longest non-decreasing prefix
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    # If the entire array is non-decreasing, return 0
    if left == n - 1:
        return 0

    # Find the length of the longest non-decreasing suffix
    right = n - 1
    while right > 0 and arr[right - 1] <= arr[right]:
        right -= 1

    # Initialize the result with the length of removing the prefix or suffix
    result = min(n - left - 1, right)

    # Iterate through the prefix and suffix to find the shortest subarray to remove
    i = 0
    j = right
    while i <= left and j < n:
        if arr[i] <= arr[j]:
            result = min(result, j - i - 1)
            i += 1
        else:
            j += 1

    return result


def test_shortest_subarray_to_remove():
    test_cases = [
        ([1, 2, 3, 10, 4, 2, 3, 5], 3, "Test Case 1"),
        ([5, 4, 3, 2, 1], 4, "Test Case 2"),
        ([1, 2, 3], 0, "Test Case 3"),
        ([1], 0, "Test Case 4"),
        ([1, 2, 3, 4, 5], 0, "Test Case 5"),
        ([5, 4, 3, 2, 1, 2, 3, 4, 5], 4, "Test Case 6"),
        ([1, 2, 3, 4, 5, 4, 3, 2, 1], 4, "Test Case 7"),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 9, "Test Case 8"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, "Test Case 9"),
        ([4, 3, 2, 1, 5, 6, 7, 8, 9, 10], 4, "Test Case 10"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 1, "Test Case 11"),
        ([1, 3, 2, 4, 5], 1, "Test Case 12"),
        ([2, 2, 2, 1, 2, 2, 2], 1, "Test Case 13"),
        ([1, 2, 3, 4, 0, 1, 2, 3], 1, "Test Case 14"),
        ([1, 2, 3, 4, 5, 0], 1, "Test Case 15"),
        ([0, 1, 2, 3, 4, 5], 0, "Test Case 16"),
        ([5, 4, 3, 2, 1, 0], 5, "Test Case 17"),
        ([1, 2, 3, 4, 5, 4, 3, 2, 1, 0], 5, "Test Case 18"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 10, "Test Case 19"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 0, "Test Case 20"),
        ([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 19, "Test Case 21"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, "Test Case 22"),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10, "Test Case 23"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1, "Test Case 24"),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, "Test Case 25"),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for arr, expected, test_name in test_cases:
        result = shortest_subarray_to_remove(arr)
        if result == expected:
            print(f"True - {test_name}")
            correct_count += 1
        else:
            print(f"False - {test_name}: Expected {expected}, got {result}")

    print(f"\n{correct_count}/{total_count}")


if __name__ == "__main__":
    test_shortest_subarray_to_remove()