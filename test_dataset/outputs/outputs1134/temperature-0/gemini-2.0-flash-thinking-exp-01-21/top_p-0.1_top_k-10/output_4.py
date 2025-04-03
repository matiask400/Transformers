import collections

def find_zero(board):
    for r in range(2):
        for c in range(3):
            if board[r][c] == 0:
                return r, c

def get_neighbors(board):
    r0, c0 = find_zero(board)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    for dr, dc in dirs:
        nr, nc = r0 + dr, c0 + dc
        if 0 <= nr < 2 and 0 <= nc < 3:
            new_board = [list(row) for row in board]
            new_board[r0][c0], new_board[nr][nc] = new_board[nr][nc], new_board[r0][c0]
            neighbors.append(tuple(tuple(row) for row in new_board))
    return neighbors

def sliding_puzzle(board):
    target = tuple(tuple([1, 2, 3]), tuple([4, 5, 0]))
    start_board = tuple(tuple(row) for row in board)
    if start_board == target:
        return 0

    q = collections.deque([(start_board, 0)])
    visited = {start_board}

    while q:
        curr_board, moves = q.popleft()

        if curr_board == target:
            return moves

        for neighbor in get_neighbors(list(list(row) for row in curr_board)):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, moves + 1))
    return -1

def test_sliding_puzzle():
    tests = [
        ([[1, 2, 3], [4, 0, 5]], 1),
        ([[1, 2, 3], [5, 4, 0]], -1),
        ([[4, 1, 2], [5, 0, 3]], 5),
        ([[3, 2, 4], [1, 5, 0]], 14),
        ([[1, 2, 3], [4, 5, 0]], 0),
        ([[0, 1, 2], [3, 4, 5]], -1), # Example of unsolvable from parity perspective
        ([[1, 0, 3], [4, 2, 5]], 2),
        ([[1, 2, 0], [4, 5, 3]], 1),
        ([[1, 2, 3], [0, 4, 5]], 1),
        ([[0, 2, 3], [1, 4, 5]], 2),
        ([[3, 2, 1], [4, 5, 0]], -1) # Another unsolvable example
    ]

    correct_tests = 0
    total_tests = len(tests)

    for i, (input_board, expected_output) in enumerate(tests):
        actual_output = sliding_puzzle(input_board)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_sliding_puzzle()