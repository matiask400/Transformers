from collections import deque

def sliding_puzzle(board):
    def get_inversions(board_list):
        inversions = 0
        arr = [x for x in board_list if x != 0]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inversions += 1
        return inversions

    initial_board_list = []
    for row in board:
        initial_board_list.extend(row)

    if get_inversions(initial_board_list) % 2 != 0:
        return -1

    target_board = [[1, 2, 3], [4, 5, 0]]
    target_board_tuple = tuple(tuple(row) for row in target_board)
    start_board_tuple = tuple(tuple(row) for row in board)

    if start_board_tuple == target_board_tuple:
        return 0

    queue = deque([(start_board_tuple, 0)])
    visited = {start_board_tuple}

    while queue:
        current_board_tuple, moves = queue.popleft()
        current_board_list = []
        for row in current_board_tuple:
            current_board_list.extend(row)

        if current_board_tuple == target_board_tuple:
            return moves

        zero_index = current_board_list.index(0)
        zero_row, zero_col = divmod(zero_index, 3)

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 2 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_board_list = list(current_board_list)
                new_board_list[zero_index], new_board_list[new_index] = new_board_list[new_index], new_board_list[zero_index]
                new_board_tuple = tuple(tuple(new_board_list[i:i+3]) for i in range(0, 6, 3))

                if new_board_tuple not in visited:
                    visited.add(new_board_tuple)
                    queue.append((new_board_tuple, moves + 1))

    return -1

def test_sliding_puzzle():
    test_cases = [
        ([[1, 2, 3], [4, 0, 5]], 1),
        ([[1, 2, 3], [5, 4, 0]], -1),
        ([[4, 1, 2], [5, 0, 3]], 5),
        ([[3, 2, 4], [1, 5, 0]], 14),
        ([[1, 2, 3], [4, 5, 0]], 0),
        ([[0, 1, 2], [3, 4, 5]], -1),
        ([[1, 0, 3], [4, 2, 5]], 2),
        ([[1, 2, 0], [4, 5, 3]], 3),
        ([[1, 2, 3], [0, 4, 5]], 4),
        ([[1, 2, 3], [4, 5, 0]], 0),
        ([[4, 3, 2], [1, 0, 5]], -1),
        ([[5, 4, 3], [2, 1, 0]], -1),
        ([[0, 5, 4], [3, 2, 1]], -1),
        ([[3, 0, 5], [4, 2, 1]], -1),
    ]

    correct_count = 0
    for i, (board, expected_output) in enumerate(test_cases):
        actual_output = sliding_puzzle(board)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    test_sliding_puzzle()