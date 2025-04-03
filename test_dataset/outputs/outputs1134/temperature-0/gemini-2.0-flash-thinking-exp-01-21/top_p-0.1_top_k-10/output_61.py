def solve_problem(points):
    """
    Calculates the minimum number of arrows to burst all balloons.

    Args:
        points: A list of lists, where each inner list represents a balloon
                and contains the start and end x-coordinates of its diameter.

    Returns:
        The minimum number of arrows required.
    """
    if not points:
        return 0

    points.sort(key=lambda x: x[0])  # Sort by start coordinates
    arrows = 0
    i = 0
    n = len(points)

    while i < n:
        arrows += 1
        arrow_pos = points[i][1]  # Shoot arrow at the end of the current balloon
        i += 1
        while i < n and points[i][0] <= arrow_pos:
            i += 1
    return arrows

def run_tests():
    """
    Runs test cases for the solve_problem function and prints the results.
    """
    test_cases = [
        ([[10,16],[2,8],[1,6],[7,12]], 2),
        ([[1,2],[3,4],[5,6],[7,8]], 4),
        ([[1,2],[2,3],[3,4],[4,5]], 2),
        ([], 0),
        ([[1, 5]], 1),
        ([[1, 2], [1, 3], [1, 4]], 1),
        ([[1, 4], [2, 3], [3, 4]], 1),
        ([[1, 4], [2, 5], [3, 6]], 1),
        ([[1, 4], [2, 3], [6, 7]], 2),
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (points, expected_output) in enumerate(test_cases):
        actual_output = solve_problem(points)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Input: {points}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"\n{num_correct}/{total_tests}")

if __name__ == '__main__':
    run_tests()