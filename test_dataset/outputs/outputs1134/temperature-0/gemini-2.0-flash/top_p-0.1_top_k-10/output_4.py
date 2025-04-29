from collections import deque

def sliding_puzzle(board):
    """
    Solves the sliding puzzle problem.

    Args:
        board: A 2x3 list of lists representing the puzzle board.

    Returns:
        The least number of moves required to solve the puzzle, or -1 if it is impossible.
    """

    def board_to_string(board):
        return ''.join(str(x) for row in board for x in row)

    def string_to_board(s):
        return [list(map(int, s[:3])), list(map(int, s[3:]))]

    def get_neighbors(board_str):
        board = string_to_board(board_str)
        zero_index = board_str.index('0')
        zero_row = zero_index // 3
        zero_col = zero_index % 3
        neighbors = []
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in moves:
            new_row = zero_row + dr
            new_col = zero_col + dc
            if 0 <= new_row < 2 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_board_list = list(board_str)
                new_board_list[zero_index], new_board_list[new_index] = new_board_list[new_index], new_board_list[zero_index]
                neighbors.append("".join(new_board_list))
        return neighbors

    start_state = board_to_string(board)
    target_state = "123450"

    if start_state == target_state:
        return 0

    queue = deque([(start_state, 0)])
    visited = {start_state}

    while queue:
        current_state, moves = queue.popleft()
        for neighbor in get_neighbors(current_state):
            if neighbor == target_state:
                return moves + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, moves + 1))

    return -1

def test_sliding_puzzle():
    test_cases = [
        ([[1, 2, 3], [4, 0, 5]], 1, True),
        ([[1, 2, 3], [5, 4, 0]], -1, True),
        ([[4, 1, 2], [5, 0, 3]], 5, True),
        ([[3, 2, 4], [1, 5, 0]], 14, True),
        ([[1, 2, 3], [4, 5, 0]], 0, True),
        ([[0, 1, 2], [3, 4, 5]], -1, True),
        ([[1, 0, 3], [4, 2, 5]], -1, True),
        ([[1, 2, 0], [4, 5, 3]], -1, True),
        ([[1, 2, 3], [0, 4, 5]], 2, True),
        ([[1, 2, 3], [5, 0, 4]], 2, True),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for board, expected_output, should_pass in test_cases:
        actual_output = sliding_puzzle(board)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

test_sliding_puzzle()