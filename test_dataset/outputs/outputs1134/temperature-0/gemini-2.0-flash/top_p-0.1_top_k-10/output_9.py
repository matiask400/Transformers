def maxIncreaseKeepingSkyline(grid):
    """
    Calculates the maximum total sum that the height of the buildings can be increased
    without changing the skyline.

    Args:
        grid: A 2D array representing the height of buildings.

    Returns:
        The maximum total sum that the height of the buildings can be increased.
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
    Tests the maxIncreaseKeepingSkyline function with several test cases.
    """
    test_cases = [
        ([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]], 35),
        ([[0,0,0],[0,0,0],[0,0,0]], 0),
        ([[1,1,1],[1,1,1],[1,1,1]], 0),
        ([[1,2,3],[4,5,6],[7,8,9]], 8),
        ([[5,9,4],[2,1,3],[6,8,7]], 10)
    ]
    
    num_tests = len(test_cases)
    num_correct = 0
    
    for i, (grid, expected) in enumerate(test_cases):
        result = maxIncreaseKeepingSkyline(grid)
        if result == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")
    
    print(f"\nCorrect: {num_correct}/{num_tests}")

if __name__ == "__main__":
    test_maxIncreaseKeepingSkyline()