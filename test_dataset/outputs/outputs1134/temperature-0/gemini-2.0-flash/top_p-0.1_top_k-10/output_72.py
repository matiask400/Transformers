def max_value_of_equation(points, k):
    """
    Finds the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k.

    Args:
        points: A list of lists, where each inner list represents a point [xi, yi].
        k: An integer.

    Returns:
        The maximum value of the equation.
    """
    max_val = float('-inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x_diff = abs(points[i][0] - points[j][0])
            if x_diff <= k:
                val = points[i][1] + points[j][1] + x_diff
                max_val = max(max_val, val)
    return max_val

def test_max_value_of_equation():
    """
    Tests the max_value_of_equation function with several test cases.
    """
    test_cases = [
        ([[1, 3], [2, 0], [5, 10], [6, -10]], 1, 4),
        ([[0, 0], [3, 0], [9, 2]], 3, 3),
        ([[1, 0], [3, 1], [5, 2], [7, 3]], 2, 4),
        ([[1, 0], [3, 1], [5, 2], [7, 3]], 1, float('-inf')),
        ([[1, 1], [2, 2], [3, 3]], 1, 4),
        ([[1, 1], [2, 2], [3, 3]], 2, 6),
        ([[1, 1], [2, 2], [3, 3]], 0, float('-inf')),
        ([[1, 1], [4, 4], [7, 7]], 3, 6),
        ([[1, 1], [4, 4], [7, 7]], 2, float('-inf')),
        ([[1, 1], [4, 4], [7, 7]], 6, 12)
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (points, k, expected) in enumerate(test_cases):
        result = max_value_of_equation(points, k)
        if result == expected or (expected == float('-inf') and result == float('-inf')):
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"\nCorrect tests: {num_correct}/{total_tests}")

if __name__ == "__main__":
    test_max_value_of_equation()