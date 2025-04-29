import sys

def solve():
    """
    Solves the Max Increase to Keep City Skyline problem.
    Reads input from stdin, calculates the result, and prints it to stdout.
    """

    # This function is designed to be called if reading input from stdin
    # For the requested format, we will define the main logic in maxIncreaseKeepingSkyline
    # and use the test framework below.
    # If you were reading from stdin, it might look like this:
    # lines = sys.stdin.readlines()
    # grid_str = [line.strip().replace('[','').replace(']','').split(',') for line in lines if line.strip()]
    # grid = [[int(x) for x in row if x] for row in grid_str if row]
    # print(maxIncreaseKeepingSkyline(grid))
    pass # We will use the test framework instead

def maxIncreaseKeepingSkyline(grid):
    """
    Calculates the maximum total sum that the height of the buildings 
    can be increased without changing the city's skyline from any direction.

    Args:
        grid: A list of lists of integers representing the building heights.

    Returns:
        An integer representing the maximum total increase possible.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Calculate the skyline from top/bottom (max height in each column)
    max_col_heights = [0] * cols
    for j in range(cols):
        max_h = 0
        for i in range(rows):
            if grid[i][j] > max_h:
                max_h = grid[i][j]
        max_col_heights[j] = max_h
    
    # Alternatively using list comprehension and zip for columns:
    # max_col_heights = [max(col) for col in zip(*grid)]

    # Calculate the skyline from left/right (max height in each row)
    max_row_heights = [0] * rows
    for i in range(rows):
        max_row_heights[i] = max(grid[i]) if grid[i] else 0

    total_increase = 0
    # Iterate through each building
    for i in range(rows):
        for j in range(cols):
            # The maximum height this building can be without affecting skylines
            # is the minimum of the max height of its row and the max height of its column
            target_height = min(max_row_heights[i], max_col_heights[j])
            
            # The increase for this building is the difference between the target height
            # and its current height
            increase = target_height - grid[i][j]
            total_increase += increase
            
    return total_increase

def run_tests():
    """
    Runs predefined test cases against the maxIncreaseKeepingSkyline function.
    """
    test_cases = [
        ([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]], 35),
        ([[0,0,0],[0,0,0],[0,0,0]], 0),
        ([[1]], 0),
        ([[1,2],[3,4]], 0),
        ([[59,88,44],[3,18,38],[21,26,51]], 139), # Example with non-zero increases
        ([[2,2,2],[2,1,2],[2,2,2]], 1) # Center building can increase by 1
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (grid, expected_output) in enumerate(test_cases):
        result = maxIncreaseKeepingSkyline(grid)
        if result == expected_output:
            print(f"True")
            correct_count += 1
        else:
            print(f"False") # Expected {expected_output}, got {result}") # Optional: print details on failure

    print(f"{correct_count}/{total_tests}")

# Execute the test runner
if __name__ == "__main__":
    run_tests()