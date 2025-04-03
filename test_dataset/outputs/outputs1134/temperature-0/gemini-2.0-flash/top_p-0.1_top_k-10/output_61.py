def min_arrows_burst_balloons(points):
    """
    Calculates the minimum number of arrows required to burst all balloons.

    Args:
        points: A list of lists, where each inner list represents a balloon
                with [xstart, xend] coordinates.

    Returns:
        The minimum number of arrows required.
    """
    if not points:
        return 0

    points.sort(key=lambda x: x[1])  # Sort by end coordinates
    arrows = 1
    end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > end:
            arrows += 1
            end = points[i][1]

    return arrows

def test_min_arrows_burst_balloons():
    """
    Tests the min_arrows_burst_balloons function with several test cases.
    """
    test_cases = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        ([[1, 2]], 1),
        ([], 0),
        ([[1, 2], [1, 3], [1, 4], [1, 5]], 1),
        ([[1, 5], [2, 3], [4, 5]], 2),
        ([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]], 2)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (points, expected) in enumerate(test_cases):
        result = min_arrows_burst_balloons(points)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {points}, Expected: {expected}, Got: {result})")

    print(f"\nCorrect: {correct_count}/{total_tests}")

if __name__ == "__main__":
    test_min_arrows_burst_balloons()