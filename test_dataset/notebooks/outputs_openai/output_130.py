import copy
from collections import deque

def solve(board):
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])
    queue = deque()
    
    # Add all border 'O's to the queue
    for i in range(m):
        for j in [0, n-1]:
            if board[i][j] == 'O':
                queue.append((i, j))
                board[i][j] = 'E'
    for j in range(n):
        for i in [0, m-1]:
            if board[i][j] == 'O':
                queue.append((i, j))
                board[i][j] = 'E'
                
    # BFS to mark all 'O's connected to the border
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                queue.append((nx, ny))
                board[nx][ny] = 'E'
    
    # Flip all remaining 'O's to 'X' and 'E's back to 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'

def run_tests():
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
            [["X","O","X","O","X","O"],
             ["O","X","O","X","O","X"],
             ["X","O","X","O","X","O"],
             ["O","X","O","X","O","X"]],
            [["X","O","X","O","X","O"],
             ["O","X","O","X","O","X"],
             ["X","O","X","O","X","O"],
             ["O","X","O","X","O","X"]]
        ),
        (
            [["X","X","X"],
             ["X","O","X"],
             ["X","X","X"]],
            [["X","X","X"],
             ["X","X","X"],
             ["X","X","X"]]
        )
    ]
    
    correct = 0
    total = len(test_cases)
    for idx, (input_board, expected) in enumerate(test_cases):
        board_copy = copy.deepcopy(input_board)
        solve(board_copy)
        if board_copy == expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()