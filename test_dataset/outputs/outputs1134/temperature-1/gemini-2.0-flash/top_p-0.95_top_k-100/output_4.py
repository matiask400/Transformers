from collections import deque

def sliding_puzzle(board):
    """
    Solves the 2x3 sliding puzzle and returns the least number of moves required.

    Args:
        board (list[list[int]]): The initial state of the puzzle board.

    Returns:
        int: The least number of moves required to solve the puzzle, or -1 if unsolvable.
    """

    def board_to_string(board):
        return "".join(str(x) for row in board for x in row)

    def string_to_board(s):
        return [list(map(int, s[:3])), list(map(int, s[3:]))]

    def get_neighbors(board_str):
        board = string_to_board(board_str)
        zero_index = board_str.find('0')
        zero_row = zero_index // 3
        zero_col = zero_index % 3
        neighbors = []
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in moves:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 2 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_board_list = list(board_str)
                new_board_list[zero_index], new_board_list[new_index] = new_board_list[new_index], new_board_list[zero_index]
                neighbors.append("".join(new_board_list))
        return neighbors

    start = board_to_string(board)
    target = "123450"
    if start == target:
        return 0

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        curr_board, moves = queue.popleft()
        for neighbor in get_neighbors(curr_board):
            if neighbor == target:
                return moves + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, moves + 1))

    return -1

def test_sliding_puzzle():
    test_cases = [
        ([[1, 2, 3], [4, 0, 5]], 1),
        ([[1, 2, 3], [5, 4, 0]], -1),
        ([[4, 1, 2], [5, 0, 3]], 5),
        ([[3, 2, 4], [1, 5, 0]], 14),
        ([[1, 2, 3], [4, 5, 0]], 0),
        ([[0, 1, 2], [3, 4, 5]], -1),
        ([[1, 0, 2], [4, 5, 3]], 3)
    ]
    correct_count = 0
    total_count = len(test_cases)

    for board, expected_output in test_cases:
        output = sliding_puzzle(board)
        if output == expected_output:
            print('True')
            correct_count += 1
        else:
            print('False')
    print(f'{correct_count}/{total_count}')

if __name__ == '__main__':
    test_sliding_puzzle()