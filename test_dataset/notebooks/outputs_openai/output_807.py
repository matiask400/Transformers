def max_increase_keeping_skyline(grid):
    if not grid or not grid[0]:
        return 0
    n = len(grid)
    m = len(grid[0])
    row_max = [max(row) for row in grid]
    col_max = [max(grid[i][j] for i in range(n)) for j in range(m)]
    total = 0
    for i in range(n):
        for j in range(m):
            total += min(row_max[i], col_max[j]) - grid[i][j]
    return total

def run_tests():
    tests = [
        (
            [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]],
            35
        ),
        (
            [[0,0,0],[0,0,0],[0,0,0]],
            0
        ),
        (
            [[1,2,3],[4,5,6],[7,8,9]],
            6
        ),
        (
            [[5]],
            0
        ),
        (
            [[1,1,1],[1,1,1],[1,1,1]],
            0
        ),
        (
            [[1,2],[3,4]],
            1
        ),
    ]
    passed = 0
    for idx, (grid, expected) in enumerate(tests, 1):
        result = max_increase_keeping_skyline(grid)
        test_passed = result == expected
        print(test_passed)
        if test_passed:
            passed += 1
    print(f"{passed}/{len(tests)}")

run_tests()