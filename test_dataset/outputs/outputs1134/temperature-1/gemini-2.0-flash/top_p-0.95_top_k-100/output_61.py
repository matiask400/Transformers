def find_min_arrow_shots(points):
    """
    Finds the minimum number of arrows that must be shot to burst all balloons.

    Args:
        points: A list of lists, where each inner list represents a balloon with [xstart, xend].

    Returns:
        The minimum number of arrows required.
    """

    if not points:
        return 0

    # Sort the balloons by their end coordinates.
    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > end:
            arrows += 1
            end = points[i][1]

    return arrows


def test_find_min_arrow_shots():
    """
    Tests the find_min_arrow_shots function with several test cases.
    """

    test_cases = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        ([], 0),
        ([[1, 2]], 1),
        ([[1, 2], [1, 3]], 1),
        ([[1, 2], [2, 3], [1, 3], [1, 4]], 1),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (points, expected) in enumerate(test_cases):
        result = find_min_arrow_shots(points)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected {expected}, Got {result})")

    print(f"\n{correct_count}/{total_count} correct")


if __name__ == "__main__":
    test_find_min_arrow_shots()