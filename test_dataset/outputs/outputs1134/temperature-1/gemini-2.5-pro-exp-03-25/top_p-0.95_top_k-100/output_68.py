import sys
import io

class Solution:
    """
    Solves the problem of finding the number of 3x3 magic square subgrids 
    within a larger grid.
    """
    def is_magic(self, grid, r, c):
        """
        Checks if the 3x3 subgrid starting at (r, c) is a magic square.
        
        A 3x3 magic square:
        1. Contains distinct numbers from 1 to 9.
        2. All rows, columns, and both diagonals sum to 15.
        """
        
        # Optimization: A standard 1-9 magic square must have 5 in the center.
        if grid[r+1][c+1] != 5:
            return False

        # Check 1: Distinct numbers from 1 to 9.
        # Collect all 9 numbers and check if they are exactly the set {1, ..., 9}.
        seen = set()
        expected_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        subgrid_nums = []
        for i in range(3):
            for j in range(3):
                num = grid[r+i][c+j]
                # Check if number is within the valid range [1, 9] and not seen before.
                # Although checking set equality later covers this, an early exit is efficient.
                if not (1 <= num <= 9) or num in seen:
                    return False
                seen.add(num)
                subgrid_nums.append(num)

        # Ensure all numbers from 1 to 9 are present exactly once.
        if seen != expected_nums:
             return False # Should ideally be caught by the inner checks, but double-check size/content.


        # Check 2: All sums (rows, columns, diagonals) must be 15.
        
        # Check rows
        if grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15: return False
        if grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15: return False
        if grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15: return False
        
        # Check columns
        if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15: return False
        if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15: return False
        if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15: return False
        
        # Check diagonals
        if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15: return False
        if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15: return False

        # If all checks pass, it's a magic square.
        return True

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        """
        Counts the number of 3x3 magic square subgrids within the given grid.
        """
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
             return 0

        # Cannot form a 3x3 subgrid if the grid is too small.
        if rows < 3 or cols < 3:
            return 0

        magic_squares_count = 0
        
        # Iterate through all possible top-left corners (r, c) of a 3x3 subgrid.
        # The row index r can go from 0 to rows - 3.
        # The column index c can go from 0 to cols - 3.
        for r in range(rows - 2):
            for c in range(cols - 2):
                # Check if the subgrid starting at (r, c) is magic.
                if self.is_magic(grid, r, c):
                    magic_squares_count += 1
                    
        return magic_squares_count

# --- Test Harness ---

def run_tests():
    """
    Runs test cases against the Solution class.
    Prints 'True' for passed tests, 'False' for failed tests,
    and the final count of correct tests.
    """
    solver = Solution()
    
    test_cases = [
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1),
        ([[8]], 0),
        ([[4,4],[3,3]], 0),
        ([[4,7,8],[9,5,1],[2,3,6]], 0),
        ([[5,5,5],[5,5,5],[5,5,5]], 0), # Not distinct 1-9
        ([[1,8,6],[3,5,7],[4,9,2]], 1), # A valid magic square itself
        ([[1,8,6,1],[3,5,7,1],[4,9,2,1]], 1), # Valid square on left
        ([[1,1,1],[1,1,1],[1,1,1]], 0), # Fails distinct and sum
        ([[2,9,4],[7,5,3],[6,1,8]], 1), # Another valid magic square
        ([[2,9,4,2],[7,5,3,9],[6,1,8,4],[2,7,6,2],[9,5,1,7],[4,3,8,6]], 2), # Two overlapping magic squares
        ([
          [10,3,5,6],
          [4,6,6,8],
          [5,7,7,2]
        ], 0), # Contains numbers > 9
        ([
          [4,3,8,4],
          [9,5,1,9],
          [2,7,6,2],
          [4,3,8,4], # Duplicate row, doesn't affect count if not part of a magic square
          [9,5,1,9],
          [2,7,6,2]
        ], 2), # Two identical magic squares vertically
        ([ # Grid larger than 10x10 for testing robustness (if constraints allowed)
          [4,3,8,4, 4,3,8,4, 4,3,8],
          [9,5,1,9, 9,5,1,9, 9,5,1],
          [2,7,6,2, 2,7,6,2, 2,7,6],
          [4,3,8,4, 4,3,8,4, 4,3,8],
          [9,5,1,9, 9,5,1,9, 9,5,1],
          [2,7,6,2, 2,7,6,2, 2,7,6],
          [4,3,8,4, 4,3,8,4, 4,3,8],
          [9,5,1,9, 9,5,1,9, 9,5,1],
          [2,7,6,2, 2,7,6,2, 2,7,6],
          [4,3,8,4, 4,3,8,4, 4,3,8],
          [9,5,1,9, 9,5,1,9, 9,5,1] # 11 rows
        ], 9 * 2), # Should find 2 squares in each 3x3 capable block
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    # Capture print output
    original_stdout = sys.stdout
    string_io = io.StringIO()
    sys.stdout = string_io

    print("Running Tests:")
    for i, (grid_input, expected_output) in enumerate(test_cases):
        # Test case number 13 has a grid larger than constraints, adjust it
        if i == 12: 
             grid_input_constrained = [row[:10] for row in grid_input[:10]]
             # Recalculate expected for 10x10 based on the pattern
             # Original 11x11 had 9x9 possible top-left corners.
             # Each 3x_ block had 2 magic squares. 9*2 = 18 expected.
             # Constrained 10x10 has 8x8 possible top-left corners.
             # Number of 3x_ blocks horizontally = 8. Vertically = 8.
             # Check original structure: 
             # [[M, 4],
             #  [2, M]] where M is magic
             # In the 10x10 version:
             # Top-left at (0,0), (0,4), (0,8) - No, (0,7) max c. 
             # c can be 0, 1, ..., 7. r can be 0, 1, ..., 7
             # Magic squares start at c=0 and c=4.
             # Magic squares start at r=0 and r=3 and r=6.
             # Valid (r,c): (0,0), (0,4), (3,0), (3,4), (6,0), (6,4) -> 6 magic squares
             expected_output_constrained = 6
             result = solver.numMagicSquaresInside(grid_input_constrained)
             passed = (result == expected_output_constrained)
             print(f"Test {i+1}: {passed}")

        else:
            result = solver.numMagicSquaresInside(grid_input)
            passed = (result == expected_output)
            print(f"Test {i+1}: {passed}")
            
        if passed:
            correct_tests += 1

    print(f"\nResult: {correct_tests} / {total_tests} tests passed.")
    
    # Restore stdout and print captured output
    sys.stdout = original_stdout
    captured_output = string_io.getvalue()
    print(captured_output)


if __name__ == '__main__':
    run_tests()