def maxIncreaseKeepingSkyline(grid):
    """
    Calculates the maximum total sum that the height of the buildings can be increased
    without changing the skyline.

    Args:
        grid: A 2D array representing the height of buildings.

    Returns:
        The maximum total sum of height increases.
    """
    n = len(grid)
    row_max = [max(row) for row in grid]
    col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]

    increase_sum = 0
    for i in range(n):
        for j in range(n):
            increase_sum += min(row_max[i], col_max[j]) - grid[i][j]

    return increase_sum

def test_maxIncreaseKeepingSkyline():
    """
    Tests the maxIncreaseKeepingSkyline function.
    """
    test_cases = [
        {
            "grid": [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]],
            "expected": 35
        },
        {
            "grid": [[0,0,0],[0,0,0],[0,0,0]],
            "expected": 0
        },
        {
            "grid": [[1,1],[1,1]],
            "expected": 0
        },
        {
            "grid": [[5,5,5],[5,5,5],[5,5,5]],
            "expected": 0
        },
        {
            "grid": [[1,2,3],[4,5,6],[7,8,9]],
            "expected": 30
        }
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        grid = test_case["grid"]
        expected = test_case["expected"]
        actual = maxIncreaseKeepingSkyline(grid)

        if actual == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Actual: {actual})")

    print(f"\nCorrect: {num_correct}/{total_tests}")

if __name__ == "__main__":
    test_maxIncreaseKeepingSkyline()