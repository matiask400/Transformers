def isBoomerang(points):
    """
    Determines if three points form a boomerang.

    Args:
        points: A list of three points, where each point is a list of two integers [x, y].

    Returns:
        True if the points form a boomerang, False otherwise.
    """
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    # Check if points are distinct
    if (x1 == x2 and y1 == y2) or \
       (x1 == x3 and y1 == y3) or \
       (x2 == x3 and y2 == y3):
        return False

    # Check if points are in a straight line (collinear)
    # Using the determinant method: area of triangle formed by the points should be non-zero
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area != 0

def test_isBoomerang():
    test_cases = [
        ([[1, 1], [2, 3], [3, 2]], True),
        ([[1, 1], [2, 2], [3, 3]], False),
        ([[0, 0], [1, 0], [2, 0]], False),
        ([[0, 0], [0, 1], [0, 2]], False),
        ([[1, 0], [0, 0], [2, 0]], False),
        ([[1, 1], [2, 2], [1, 1]], False),
        ([[0, 0], [0, 0], [0, 0]], False),
        ([[1, 1], [2, 3], [2, 3]], False),
        ([[0, 0], [1, 1], [0, 2]], True),
        ([[1, 1], [0, 0], [2, 2]], False)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (points, expected) in enumerate(test_cases):
        result = isBoomerang(points)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_isBoomerang()