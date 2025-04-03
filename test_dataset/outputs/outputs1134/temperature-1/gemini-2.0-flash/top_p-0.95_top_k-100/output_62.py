def longest_subarray_with_k_flips(A, K):
    """
    Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
    Return the length of the longest (contiguous) subarray that contains only 1s.

    Args:
        A (list[int]): A list of 0s and 1s.
        K (int): The maximum number of 0s we can change to 1s.

    Returns:
        int: The length of the longest subarray that contains only 1s.
    """

    window_start = 0
    max_length = 0
    zero_count = 0

    for window_end in range(len(A)):
        if A[window_end] == 0:
            zero_count += 1

        while zero_count > K:
            if A[window_start] == 0:
                zero_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

def test_longest_subarray_with_k_flips():
    test_cases = [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
        ([0, 0, 0, 0], 2, 2),
        ([1, 1, 1, 1], 2, 4),
        ([0, 0, 0, 1, 1, 1, 0, 0], 0, 3),
        ([0, 0, 0, 1, 1, 1, 0, 0], 1, 4),
        ([0, 0, 0, 1, 1, 1, 0, 0], 2, 5),
        ([0, 0, 0, 1, 1, 1, 0, 0], 3, 6),
        ([0, 0, 0, 1, 1, 1, 0, 0], 4, 7),
        ([0, 0, 0, 1, 1, 1, 0, 0], 5, 7),
        ([1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 1, 5),
        ([1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 2, 6),
        ([1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 3, 8),
        ([0], 0, 0),
        ([1], 0, 1),
        ([0], 1, 1),
        ([1], 1, 1),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for A, K, expected in test_cases:
        result = longest_subarray_with_k_flips(A, K)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
    
    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_longest_subarray_with_k_flips()