def max_value_of_equation(points, k):
    """
    Finds the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k.

    Args:
        points: A list of points, where each point is a list [x, y].
        k: An integer.

    Returns:
        The maximum value of the equation.
    """
    max_value = float('-inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            xi, yi = points[i]
            xj, yj = points[j]
            if abs(xi - xj) <= k:
                max_value = max(max_value, yi + yj + abs(xi - xj))
    return max_value

def test_max_value_of_equation():
    """
    Tests the max_value_of_equation function.
    """
    test_cases = [
        ([[1, 3], [2, 0], [5, 10], [6, -10]], 1, 4),
        ([[0, 0], [3, 0], [9, 2]], 3, 3),
        ([[1, 0], [2, 0], [3, 0]], 1, 1),
        ([[1, 1], [2, 2], [3, 3]], 2, 6),
        ([[1, 1], [2, 2], [3, 3]], 1, 4)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for points, k, expected_output in test_cases:
        actual_output = max_value_of_equation(points, k)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_max_value_of_equation()