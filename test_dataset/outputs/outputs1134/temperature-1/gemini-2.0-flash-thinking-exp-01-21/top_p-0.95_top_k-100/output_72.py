def solve():
    def find_max_value(points, k):
        max_val = -float('inf')
        n = len(points)
        found_pair = False
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                if abs(xi - xj) <= k:
                    found_pair = True
                    current_val = yi + yj + abs(xi - xj)
                    max_val = max(max_val, current_val)
        if not found_pair:
            return 0 # Should not happen based on problem description, but to handle potential edge cases.
        return max_val

    test_cases = [
        ([[1,3],[2,0],[5,10],[6,-10]], 1, 4),
        ([[0,0],[3,0],[9,2]], 3, 3),
        ([[0,0],[1,1],[2,2],[3,3]], 2, 5),
        ([[0,0],[5,5],[10,10],[15,15]], 5, 10),
        ([[0,0],[1,1],[5,5],[6,6]], 5, 10),
        ([[0,0],[10,10]], 20, 20),
        ([[0,0],[10,10]], 5, -float('inf')), # Should be invalid, problem guarantees at least one pair
        ([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]], 1, 4),
        ([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]], 5, 15),
        ([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]], 9, 25),
        ([[-1,-1],[0,0],[1,1],[2,2],[3,3]], 2, 5),
    ]

    correct_count = 0
    for i, (points, k, expected_output) in enumerate(test_cases):
        if expected_output == -float('inf'): # Handle invalid case from test setup.
            continue # Skip if test case is meant to be invalid
        actual_output = find_max_value(points, k)
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{len(test_cases)- test_cases.count(([[0,0],[10,10]], 5, -float('inf')))}") # Exclude invalid test from total

solve()