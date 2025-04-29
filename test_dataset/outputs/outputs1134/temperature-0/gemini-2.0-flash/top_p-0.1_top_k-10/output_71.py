def can_reorder_doubled(arr):
    """
    Given an array of integers `arr` of even length, return `true` if and only if it is possible to reorder it such that `arr[2 * i + 1] = 2 * arr[2 * i]` for every `0 <= i < len(arr) / 2`.
    """
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    arr.sort(key=abs)

    for num in arr:
        if counts.get(num, 0) == 0:
            continue

        counts[num] -= 1
        double_num = 2 * num

        if counts.get(double_num, 0) == 0:
            return False

        counts[double_num] -= 1

    return True

def test_can_reorder_doubled():
    test_cases = [
        ([3, 1, 3, 6], False),
        ([2, 1, 2, 6], False),
        ([4, -2, 2, -4], True),
        ([1, 2, 4, 16, 8, 4], False),
        ([0, 0], True),
        ([1, 2, 1, 2], True),
        ([1, 2, 2, 4], True),
        ([1, 2, 4, 8], True),
        ([0, 0, 0, 0], True),
        ([-5, -2], False),
        ([-2, -4], True),
        ([-1, -2], True),
        ([-1, -2, 1, 2], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
        ([-1, -2, 1, 2, -3, -6, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
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