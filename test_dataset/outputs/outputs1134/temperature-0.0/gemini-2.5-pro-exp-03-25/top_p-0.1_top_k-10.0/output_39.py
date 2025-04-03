import copy
from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Captures surrounded regions of 'O's by flipping them to 'X's.
        An 'O' is not captured if it's on the border or connected to an 'O' on the border.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        # Helper function to check if coordinates are within bounds
        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        # Use BFS (or DFS) starting from border 'O's to mark connected 'O's
        # We'll temporarily mark these connected 'O's as 'S' (Safe)
        queue = deque()

        # 1. Add all border 'O's to the queue and mark them as 'S'
        for r in range(m):
            if board[r][0] == 'O':
                board[r][0] = 'S'
                queue.append((r, 0))
            if board[r][n - 1] == 'O':
                board[r][n - 1] = 'S'
                queue.append((r, n - 1))

        for c in range(1, n - 1): # Avoid double-checking corners
            if board[0][c] == 'O':
                board[0][c] = 'S'
                queue.append((0, c))
            if board[m - 1][c] == 'O':
                board[m - 1][c] = 'S'
                queue.append((m - 1, c))

        # 2. Perform BFS to find all 'O's connected to the border 'O's
        while queue:
            r, c = queue.popleft()
            # Check neighbors (up, down, left, right)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                # If neighbor is valid, is an 'O', add to queue and mark as 'S'
                if is_valid(nr, nc) and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'
                    queue.append((nr, nc))

        # 3. Iterate through the board:
        #    - Flip remaining 'O's (not marked 'S') to 'X' (these are surrounded)
        #    - Flip 'S's back to 'O' (these are safe/connected to border)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'


# --- Testing Framework ---
def run_tests():
    solver = Solution()
    tests = [
        # Test Case 1: Example 1
        {
            "input": [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
            "expected": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        },
        # Test Case 2: Example 2
        {
            "input": [["X"]],
            "expected": [["X"]]
        },
        # Test Case 3: All 'O's
        {
            "input": [["O","O","O"],["O","O","O"],["O","O","O"]],
            "expected": [["O","O","O"],["O","O","O"],["O","O","O"]]
        },
        # Test Case 4: All 'X's
        {
            "input": [["X","X"],["X","X"]],
            "expected": [["X","X"],["X","X"]]
        },
        # Test Case 5: Single 'O' surrounded
        {
            "input": [["X","X","X"],["X","O","X"],["X","X","X"]],
            "expected": [["X","X","X"],["X","X","X"],["X","X","X"]]
        },
        # Test Case 6: Single 'O' on border
        {
            "input": [["O","X","X"],["X","X","X"],["X","X","X"]],
            "expected": [["O","X","X"],["X","X","X"],["X","X","X"]]
        },
         # Test Case 7: More complex border connection
        {
            "input": [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]],
            "expected": [["X","O","X","O","X","O"],["O","X","X","X","X","X"],["X","X","X","X","X","O"],["O","X","O","X","O","X"]]
        },
        # Test Case 8: Empty board
        {
             "input": [],
             "expected": []
        },
        # Test Case 9: Board with empty row (invalid per constraints but good to check)
        # Note: The code handles this via the initial check `if not board or not board[0]:`
        {
             "input": [[]],
             "expected": [[]]
        },
        # Test Case 10: Larger board
        {
            "input": [
                ["X","X","X","X","X"],
                ["X","O","O","O","X"],
                ["X","O","X","O","X"],
                ["X","O","O","O","X"],
                ["X","X","X","X","X"]
            ],
            "expected": [
                ["X","X","X","X","X"],
                ["X","O","O","O","X"],
                ["X","O","X","O","X"],
                ["X","O","O","O","X"],
                ["X","X","X","X","X"] # Inner 'O's are connected to border 'O's
            ]
        },
        # Test Case 11: Larger board with capture
        {
            "input": [
                ["X","X","X","X","X"],
                ["X","O","X","O","X"],
                ["X","X","O","X","X"],
                ["X","O","X","O","X"],
                ["X","X","X","X","X"]
            ],
            "expected": [
                ["X","X","X","X","X"],
                ["X","O","X","O","X"],
                ["X","X","X","X","X"], # Middle 'O' captured
                ["X","O","X","O","X"],
                ["X","X","X","X","X"]
            ]
        }

    ]

    correct_count = 0
    for i, test in enumerate(tests):
        # Need a deep copy because the function modifies the board in-place
        board_copy = copy.deepcopy(test["input"])
        solver.solve(board_copy)
        result = board_copy
        expected = test["expected"]

        # Handle empty board/row cases explicitly for comparison logic
        is_result_empty = not result or not result[0]
        is_expected_empty = not expected or not expected[0]

        if is_result_empty and is_expected_empty:
             passed = True
        elif is_result_empty != is_expected_empty:
             passed = False # One is empty, the other isn't
        else:
             passed = (result == expected) # Compare non-empty boards

        print(f"Test {i+1}: {passed}")
        if passed:
            correct_count += 1

    print(f"\n{correct_count}/{len(tests)} tests passed.")

# Make the script executable
if __name__ == "__main__":
    run_tests()