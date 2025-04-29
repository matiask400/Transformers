def is_boomerang(points):
    """
    Given an array `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane,
    return `true` if these points are a boomerang.

    A boomerang is a set of three points that are all distinct and not in a straight line.
    """
    p1, p2, p3 = points
    if p1 == p2 or p1 == p3 or p2 == p3:
        return False

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Check if the points are in a straight line using cross product
    cross_product = (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)
    if cross_product == 0:
        return False
    else:
        return True

def run_tests():
    test_cases = [
        {"input": [[1,1],[2,3],[3,2]], "expected": True},
        {"input": [[1,1],[2,2],[3,3]], "expected": False},
        {"input": [[1,1],[2,2],[1,1]], "expected": False},
        {"input": [[0,0],[0,0],[0,0]], "expected": False},
        {"input": [[0,0],[1,1],[2,0]], "expected": True},
        {"input": [[0,0],[0,1],[0,2]], "expected": False},
        {"input": [[1,0],[0,0],[2,0]], "expected": False},
        {"input": [[1,0],[0,1],[2,2]], "expected": True},
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        input_points = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = is_boomerang(input_points)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    total_tests = len(test_cases)
    print(f"Correct tests: {correct_count} over {total_tests}")

if __name__ == '__main__':
    run_tests()