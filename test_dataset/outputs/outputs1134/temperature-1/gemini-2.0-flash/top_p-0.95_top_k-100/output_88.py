def solve():
    def solve_board(board):
        if not board:
            return board

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'  # Temporarily mark as visited
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Mark 'O's connected to the border
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        # Flip 'O's to 'X' and 'T's back to 'O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

        return board

    test_cases = [
        (
            [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
            [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
        ),
        (
            [["X"]],
            [["X"]]
        ),
        (
            [["O"]],
            [["O"]]
        ),
        (
            [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
            [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
        ),
        (
            [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
            [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
        )
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (input_board, expected_output) in enumerate(test_cases):
        input_copy = [row[:] for row in input_board]  # Create a deep copy
        result = solve_board(input_copy)
        if result == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_count}/{total_count}")

solve()