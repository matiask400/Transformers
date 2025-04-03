def fixed_point(arr):
    """
    Finds the smallest index i in a sorted array arr such that arr[i] == i.

    Args:
        arr: A sorted array of distinct integers.

    Returns:
        The smallest index i such that arr[i] == i, or -1 if no such index exists.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def test_fixed_point():
    """
    Tests the fixed_point function with several test cases.
    """
    test_cases = [
        ([-10, -5, 0, 3, 7], 3),
        ([0, 2, 5, 8, 17], 0),
        ([-10, -5, 3, 4, 7, 9], -1),
        ([-1,0,1,2,4], 4),
        ([0], 0),
        ([1], -1),
        ([-1], -1),
        ([-1, 1], 1),
        ([0, 1], 0),
        ([-2, -1, 0, 1, 2], 2)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for arr, expected in test_cases:
        result = fixed_point(arr)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {arr}, Expected: {expected}, Got: {result}")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_fixed_point()