from collections import deque

def slidingPuzzle(board):
    target = '123450'
    start = ''.join(str(num) for row in board for num in row)
    neighbors = {
        0: [1,3],
        1: [0,2,4],
        2: [1,5],
        3: [0,4],
        4: [1,3,5],
        5: [2,4]
    }
    visited = set()
    queue = deque()
    queue.append((start, 0))
    visited.add(start)
    
    while queue:
        state, steps = queue.popleft()
        if state == target:
            return steps
        zero = state.index('0')
        for neighbor in neighbors[zero]:
            lst = list(state)
            lst[zero], lst[neighbor] = lst[neighbor], lst[zero]
            new_state = ''.join(lst)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))
    return -1

# Test cases
tests = [
    ([[1,2,3],[4,0,5]], 1),
    ([[1,2,3],[5,4,0]], -1),
    ([[4,1,2],[5,0,3]], 5),
    ([[3,2,4],[1,5,0]], 14)
]

correct = 0
total = len(tests)

for board, expected in tests:
    result = slidingPuzzle(board)
    if result == expected:
        print('True')
        correct +=1
    else:
        print('False')

print(f"{correct}/{total}")