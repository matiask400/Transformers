def is_boomerang(points):
    # Check if all points are distinct
    if len(set(map(tuple, points))) != 3:
        return False
    # Calculate area of triangle formed by the points
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    area = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
    return area != 0

def run_tests():
    test_cases = [
        ([[1,1],[2,3],[3,2]], True),
        ([[1,1],[2,2],[3,3]], False),
        ([[0,0],[1,1],[0,1]], True),
        ([[0,0],[0,0],[0,0]], False),
        ([[1,2],[3,4],[5,6]], False),
        ([[1,0],[2,1],[3,0]], True),
    ]
    
    correct = 0
    total = len(test_cases)
    for points, expected in test_cases:
        result = is_boomerang(points)
        is_correct = result == expected
        print(is_correct)
        if is_correct:
            correct += 1
    print(f"{correct}/{total}")

run_tests()