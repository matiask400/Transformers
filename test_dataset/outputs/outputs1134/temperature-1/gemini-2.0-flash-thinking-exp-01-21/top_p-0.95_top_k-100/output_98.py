def find_smallest_index(arr):
    """
    Given a sorted array of distinct integers arr, return the smallest index i that satisfies arr[i] == i.
    If there is no such index, return -1.
    """
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            result = mid
            right = mid - 1  # Search for smaller index
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return result

def run_tests():
    test_cases = [
        ([-10, -5, 0, 3, 7], 3),
        ([0, 2, 5, 8, 17], 0),
        ([-10, -5, 3, 4, 7, 9], -1),
        ([-1, 0, 1, 2, 4], 4),
        ([-2, 0, 2, 3, 6, 7, 9], 2),
        ([-3, -1, 1, 5], -1),
        ([0], 0),
        ([-1], -1),
        ([1], -1),
        ([-1, 1], -1),
        ([0, 1], 0),
        ([-2, -1, 0], -1)
    ]
    correct_count = 0
    for i, (arr, expected_output) in enumerate(test_cases):
        output = find_smallest_index(arr)
        if output == expected_output:
            print('True')
            correct_count += 1
        else:
            print('False')
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()