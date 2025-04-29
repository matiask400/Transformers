import sys
import io

def solve():
    """
    Solves the Magic Squares In Grid problem and runs tests.
    """

    def numMagicSquaresInside(grid):
        """
        Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?
        (Each subgrid is contiguous).

        Args:
            grid: A list of lists of integers representing the grid.

        Returns:
            The number of 3x3 magic square subgrids.
        """
        rows = len(grid)
        cols = len(grid[0])

        # A 3x3 subgrid cannot exist if the grid is too small
        if rows < 3 or cols < 3:
            return 0

        count = 0

        # Helper function to check if a 3x3 subgrid starting at (r, c) is magic
        def is_magic(r, c):
            # 1. Check if all numbers are distinct and within the range [1, 9]
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    # Numbers must be between 1 and 9 inclusive
                    if not (1 <= val <= 9):
                        return False
                    # Numbers must be distinct
                    if val in seen:
                        return False
                    seen.add(val)
            
            # If we didn't find 9 distinct numbers from 1-9, it's not magic
            # (This check is implicitly covered by the loop above, but good for clarity)
            # if len(seen) != 9:
            #    return False 

            # 2. Check if the sum of rows, columns, and diagonals is 15
            # The magic sum for a 3x3 square with distinct numbers 1-9 is always 15.
            magic_sum = 15

            # Check rows
            if sum(grid[r][c:c+3]) != magic_sum: return False
            if sum(grid[r+1][c:c+3]) != magic_sum: return False
            if sum(grid[r+2][c:c+3]) != magic_sum: return False

            # Check columns
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != magic_sum: return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != magic_sum: return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != magic_sum: return False

            # Check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != magic_sum: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != magic_sum: return False

            # If all checks pass, it's a magic square
            return True

        # Iterate through all possible top-left corners of 3x3 subgrids
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1

        return count

    # --- Testing ---
    test_cases = [
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1),
        ([[8]], 0),
        ([[4,4],[3,3]], 0),
        ([[4,7,8],[9,5,1],[2,3,6]], 0),
        ([[5,5,5],[5,5,5],[5,5,5]], 0), # Not distinct 1-9
        ([[1,8,6],[3,5,7],[4,9,2]], 0), # Not magic (row 1 sum != 15)
        ([[8,1,6],[3,5,7],[4,9,2]], 1), # A standard magic square
        ([[2,7,6],[9,5,1],[4,3,8],[1,8,1]], 1), # Test with extra row
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2],[8,1,6,3],[3,5,7,5],[4,9,2,7]], 2), # Two magic squares
        ([[10,3,8],[9,5,1],[2,7,6]], 0), # Contains number > 9
        ([[4,3,8],[9,5,1],[2,7,0]], 0), # Contains number < 1
        ([[4,3,8],[9,5,1],[4,7,6]], 0), # Contains duplicate number (4)
    ]

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    correct_count = 0
    total_tests = len(test_cases)

    for i, (grid, expected_output) in enumerate(test_cases):
        result = numMagicSquaresInside(grid)
        passed = result == expected_output
        print(f"{passed}") # Print True or False for each test
        if passed:
            correct_count += 1

    # Restore stdout
    sys.stdout = old_stdout

    # Print the captured output (True/False for each test)
    print(captured_output.getvalue(), end="")

    # Print the final summary
    print(f"{correct_count}/{total_tests}")

# Execute the solve function
solve()