def solve_board(board):
    if not board or not board[0]:
        return board

    rows = len(board)
    cols = len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'T'  # Mark as temporary
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # 1. Mark 'O's connected to the border as 'T'
    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                dfs(r, c)

    # 2. Capture remaining 'O's (change to 'X') and revert 'T's back to 'O's
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'T':
                board[r][c] = 'O'
    return board

def test_solve_board():
    tests = [
        {
            "input": [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
            "expected": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        },
        {
            "input": [["X"]],
            "expected": [["X"]]
        },
        {
            "input": [["O","O"],["O","O"]],
            "expected": [["O","O"],["O","O"]]
        },
        {
            "input": [["X","O","X"],["O","X","O"],["X","O","X"]],
            "expected": [["X","O","X"],["O","X","O"],["X","O","X"]]
        },
        {
            "input": [["O","X","O"],["X","O","X"],["O","X","O"]],
            "expected": [["O","X","O"],["X","X","X"],["O","X","O"]]
        },
        {
            "input": [["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"]],
            "expected": [["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"]]
        },
        {
            "input": [["X","X","X","X","X","X"],["X","O","O","O","O","X"],["X","O","X","X","O","X"],["X","O","X","X","O","X"],["X","O","O","O","O","X"],["X","X","X","X","X","X"]],
            "expected": [["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"]]
        },
        {
            "input": [["X","X","X","X","X","X"],["X","O","O","O","O","X"],["X","O","X","X","O","X"],["X","O","X","O","O","X"],["X","O","O","O","O","X"],["X","X","X","X","X","X"]],
            "expected": [["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","O","X","X","O","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"]]
        }
    ]

    correct_tests = 0
    for i, test in enumerate(tests):
        input_board = [row[:] for row in test["input"]] # Create a copy to avoid modifying original test input
        output_board = solve_board(input_board)
        expected_board = test["expected"]

        if output_board == expected_board:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\nCorrect tests: {correct_tests}/{len(tests)}")

if __name__ == '__main__':
    test_solve_board()