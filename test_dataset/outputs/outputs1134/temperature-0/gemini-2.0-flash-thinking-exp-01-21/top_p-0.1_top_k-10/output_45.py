def is_boomerang(points):
    """
    Given an array `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane,
    return `true` if these points are a boomerang.

    A boomerang is a set of three points that are all distinct and not in a straight line.
    """
    p1, p2, p3 = points[0], points[1], points[2]

    if p1 == p2 or p1 == p3 or p2 == p3:
        return False

    cross_product = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])
    if cross_product == 0:
        return False

    return True

def run_tests():
    test_cases = [
        {"input": [[1,1],[2,3],[3,2]], "expected": True},
        {"input": [[1,1],[2,2],[3,3]], "expected": False},
        {"input": [[1,1],[2,2],[1,1]], "expected": False},
        {"input": [[1,1],[2,3],[1,1]], "expected": False},
        {"input": [[0,0],[0,2],[2,0]], "expected": True},
        {"input": [[0,0],[0,0],[0,0]], "expected": False},
        {"input": [[100,100],[0,0],[100,100]], "expected": False},
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        input_points = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = is_boomerang(input_points)
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()