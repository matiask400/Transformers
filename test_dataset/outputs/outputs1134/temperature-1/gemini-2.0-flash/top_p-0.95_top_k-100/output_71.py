def can_reorder_doubled(arr):
    """
    Checks if it is possible to reorder the array such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.

    Args:
        arr: An array of integers of even length.

    Returns:
        True if it is possible to reorder the array, False otherwise.
    """
    count = {}
    for x in arr:
        count[x] = count.get(x, 0) + 1

    for x in sorted(count.keys(), key=abs):
        if count[x] == 0:
            continue
        if 2 * x not in count or count[2 * x] < count[x]:
            return False
        count[2 * x] -= count[x]
    return True

def test_can_reorder_doubled():
    """
    Tests the can_reorder_doubled function with several test cases.
    """
    test_cases = [
        ([3, 1, 3, 6], False),
        ([2, 1, 2, 6], False),
        ([4, -2, 2, -4], True),
        ([1, 2, 4, 16, 8, 4], False),
        ([0, 0, 0, 0], True),
        ([], True),
        ([1, 2], True),
        ([-1, -2], True),
        ([-2, -1], True),
        ([-4, -2, 2, 4], True),
        ([1, 2, 3, 4], False),
        ([0, 0], True),
        ([-4, 8], False)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for arr, expected in test_cases:
        result = can_reorder_doubled(arr)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_can_reorder_doubled()