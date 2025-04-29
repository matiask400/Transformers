def solve_board(board):
    if not board or not board[0]:
        return board
    m = len(board)
    n = len(board[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = 'S'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    # Iterate through the border
    for j in range(n):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[m - 1][j] == 'O':
            dfs(m - 1, j)
    for i in range(m):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][n - 1] == 'O':
            dfs(i, n - 1)

    # Capture 'O' regions and restore 'S' regions
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'
    return board

def run_tests():
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
            "input": [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","X"]],
            "expected": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
        },
        {
            "input": [["O","X","X","O","X"],["X","O","O","X","O"],["X","X","O","X","X"],["O","O","X","O","O"],["X","X","O","X","O"]],
            "expected": [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","X","X"],["O","O","X","O","O"],["X","X","O","X","O"]]
        }
    ]
    correct_count = 0
    for i, test in enumerate(tests):
        board_input = [row[:] for row in test["input"]] # Deep copy to avoid modifying original input
        original_board = [row[:] for row in test["input"]]
        solved_board = solve_board(board_input)
        expected_output = test["expected"]
        if solved_board == expected_output:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False')
            print(f'Input: {original_board}')
            print(f'Output: {solved_board}')
            print(f'Expected: {expected_output}')

    print(f'Correct tests: {correct_count}/{len(tests)}')

if __name__ == '__main__':
    run_tests()