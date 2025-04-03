import collections
import sys

# Increase recursion depth limit for potential deep DFS paths, though unlikely needed for m, n <= 200
# sys.setrecursionlimit(40000) # LeetCode usually has higher limits than default Python

def solve_surrounded_regions(board):
    """
    Modifies the board in-place to capture surrounded regions.
    An 'O' region is captured if it's not connected to the border.
    Uses DFS to find 'O's connected to the border.
    """
    if not board or not board[0]:
        return

    m = len(board)
    n = len(board[0])

    # Use Depth First Search (DFS)
    def dfs(r, c):
        # Check boundaries and if the cell is 'O'
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
            return
        
        # Mark the current 'O' as safe (temporarily using 'S')
        board[r][c] = 'S'
        
        # Recursively call DFS for adjacent cells
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # 1. Start DFS from all 'O's on the border
    # Top and Bottom rows
    for c in range(n):
        if board[0][c] == 'O':
            dfs(0, c)
        if board[m - 1][c] == 'O':
            dfs(m - 1, c)
            
    # Left and Right columns (excluding corners already checked)
    for r in range(1, m - 1):
        if board[r][0] == 'O':
            dfs(r, 0)
        if board[r][n - 1] == 'O':
            dfs(r, n - 1)

    # 2. Iterate through the board to flip remaining 'O's and revert 'S's
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O':
                # This 'O' was not reached from the border, so it's surrounded
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                # This 'O' was connected to the border, revert it back to 'O'
                board[r][c] = 'O'
    
    # The board is modified in-place, no return value needed for the core logic.
    # However, for testing consistency, we can return the modified board.
    return board # Returning for test harness comparison convenience


# --- Test Harness ---

def run_tests():
    """
    Runs test cases against the solve_surrounded_regions function.
    """
    test_cases = [
        (
            [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]],
            [["X","X","X","X"],
             ["X","X","X","X"],
             ["X","X","X","X"],
             ["X","O","X","X"]]
        ),
        (
            [["X"]],
            [["X"]]
        ),
        (
            [["O","O","O"],
             ["O","O","O"],
             ["O","O","O"]],
            [["O","O","O"],
             ["O","O","O"],
             ["O","O","O"]]
        ),
        (
            [["X","O","X"],
             ["X","O","X"],
             ["X","O","X"]],
            [["X","O","X"],
             ["X","O","X"],
             ["X","O","X"]]
        ),
         (
            [["X","X","X"],
             ["X","O","X"],
             ["X","X","X"]],
            [["X","X","X"],
             ["X","X","X"],
             ["X","X","X"]]
        ),
         (
            [["O","X","X","O","X"],
             ["X","O","O","X","O"],
             ["X","O","X","O","X"],
             ["O","X","O","O","O"],
             ["X","X","O","X","O"]],
            [["O","X","X","O","X"],
             ["X","X","X","X","O"],
             ["X","X","X","O","X"],
             ["O","X","O","O","O"],
             ["X","X","O","X","O"]]
         )
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_board, expected_output) in enumerate(test_cases):
        # Create a deep copy to avoid modifying the original test case input
        board_copy = [row[:] for row in input_board]
        
        # Run the solve function (modifies board_copy in-place)
        solve_surrounded_regions(board_copy)
        
        # Compare the modified board with the expected output
        result = board_copy == expected_output
        print(f"{result}")
        if result:
            correct_count += 1
        # Optional: Print details on failure
        # else:
        #     print(f"Test Case {i+1} Failed")
        #     print(f"Input:\n{input_board}")
        #     print(f"Expected:\n{expected_output}")
        #     print(f"Got:\n{board_copy}")


    print(f"{correct_count}/{total_tests}")

# Execute the tests
if __name__ == "__main__":
    run_tests()