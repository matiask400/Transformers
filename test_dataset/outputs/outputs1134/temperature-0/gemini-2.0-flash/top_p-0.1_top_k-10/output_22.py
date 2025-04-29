def unique_occurrences(arr):
    """
    Given an array of integers arr, returns true if and only if the number of occurrences of each value in the array is unique.

    Args:
        arr: A list of integers.

    Returns:
        True if the number of occurrences of each value in the array is unique, False otherwise.
    """
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    occurrences = set()
    for count in counts.values():
        if count in occurrences:
            return False
        occurrences.add(count)

    return True

def test_unique_occurrences():
    """
    Tests the unique_occurrences function with several test cases.
    """
    test_cases = [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
        ([1], True),
        ([1,1,1,1,1], True),
        ([1,2,3,4,5], True),
        ([1,1,2,2,3,3,4,4,5], False)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for arr, expected in test_cases:
        result = unique_occurrences(arr)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_unique_occurrences()