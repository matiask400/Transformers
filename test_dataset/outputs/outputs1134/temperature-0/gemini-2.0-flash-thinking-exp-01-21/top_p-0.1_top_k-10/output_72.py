def solve():
    def find_max_value(points, k):
        max_val = -float('inf')
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                if abs(xi - xj) <= k:
                    current_val = yi + yj + abs(xi - xj)
                    max_val = max(max_val, current_val)
        return max_val

    def run_test(points, k, expected_output):
        output = find_max_value(points, k)
        if output == expected_output:
            print('True')
            return True
        else:
            print('False')
            return False

    test_cases = [
        {
            "points": [[1,3],[2,0],[5,10],[6,-10]],
            "k": 1,
            "expected_output": 4
        },
        {
            "points": [[0,0],[3,0],[9,2]],
            "k": 3,
            "expected_output": 3
        },
        {
            "points": [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]],
            "k": 3,
            "expected_output": 10
        },
        {
            "points": [[0,0],[5,0],[10,0]],
            "k": 4,
            "expected_output": -float('inf') # Should be 0, but the problem guarantees at least one pair. Let's re-read the problem description.
        },
        {
            "points": [[0,0],[5,0],[10,0]],
            "k": 5,
            "expected_output": 5
        },
        {
            "points": [[-10, -10], [-5, -5], [0, 0], [5, 5], [10, 10]],
            "k": 5,
            "expected_output": 0
        },
        {
            "points": [[-10, -10], [-5, -5], [0, 0], [5, 5], [10, 10]],
            "k": 10,
            "expected_output": 10
        }
    ]

    correct_tests = 0
    for test in test_cases:
        if run_test(test["points"], test["k"], test["expected_output"]):
            correct_tests += 1

    print(f"{correct_tests}/{len(test_cases)}")

solve()