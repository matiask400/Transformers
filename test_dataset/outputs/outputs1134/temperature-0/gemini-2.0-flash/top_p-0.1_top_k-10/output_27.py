def erase_overlap_intervals(intervals):
    """
    Finds the minimum number of intervals to remove to make the rest of the intervals non-overlapping.

    Args:
        intervals: A list of intervals, where each interval is a list of two integers [start, end].

    Returns:
        The minimum number of intervals to remove.
    """

    if not intervals:
        return 0

    # Sort the intervals by their end points.
    intervals.sort(key=lambda x: x[1])

    # Initialize the count of non-overlapping intervals to 1.
    count = 1

    # Initialize the end point of the first interval.
    end = intervals[0][1]

    # Iterate over the remaining intervals.
    for i in range(1, len(intervals)):
        # If the start point of the current interval is greater than or equal to the end point of the previous interval,
        # then the intervals are non-overlapping.
        if intervals[i][0] >= end:
            # Increment the count of non-overlapping intervals.
            count += 1

            # Update the end point of the previous interval.
            end = intervals[i][1]

    # The minimum number of intervals to remove is the total number of intervals minus the number of non-overlapping intervals.
    return len(intervals) - count


def test_erase_overlap_intervals():
    """
    Tests the erase_overlap_intervals function.
    """

    test_cases = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
        ([], 0),
        ([[1, 2]], 0),
        ([[1, 2], [2, 3], [1, 3], [3, 4]], 1)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (intervals, expected) in enumerate(test_cases):
        result = erase_overlap_intervals(intervals)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {intervals}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    print(f"\nCorrect: {correct_count}/{total_count}")


if __name__ == "__main__":
    test_erase_overlap_intervals()