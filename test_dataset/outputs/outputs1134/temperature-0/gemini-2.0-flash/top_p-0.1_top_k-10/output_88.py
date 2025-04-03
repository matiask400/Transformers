def solve():
    def solve_board(board):
        if not board:
            return board

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'  # Mark as temporary 'O'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Mark 'O's connected to the border as temporary 'O's
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

        # Flip remaining 'O's to 'X's and restore temporary 'O's to 'O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

        return board

    # Test cases
    test_cases = [
        {
            "input": [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
            "expected": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        },
        {
            "input": [["X"]],
            "expected": [["X"]]
        },
        {
            "input": [["O","O","O"],["O","O","O"],["O","O","O"]],
            "expected": [["O","O","O"],["O","O","O"],["O","O","O"]]
        },
        {
            "input": [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]],
            "expected": [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
        },
        {
            "input": [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","O","O","O","X","O"],["O","O","X","O","X","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"]],
            "expected": [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","O","O","O","X","O"],["O","O","X","O","X","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"]]
        }
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_board = [row[:] for row in test_case["input"]]  # Create a deep copy
        expected_output = test_case["expected"]
        
        result = solve_board([row[:] for row in input_board]) # Create a deep copy for the function
        
        if result == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_board}")
            print(f"  Expected: {expected_output}")
            print(f"  Got: {result}")

    print(f"\nCorrect: {num_correct}/{total_tests}")

solve()