from collections import deque

def find_min_distance(grid):
    m, n = len(grid), len(grid[0])
    start = None
    target = None
    # Find start and target positions
    for i in range(m):
        for j in range(n):
            if grid[i][j] == -1:
                start = (i, j)
            elif grid[i][j] == 2:
                target = (i, j)
    if not start or not target:
        return -1
    # BFS to find shortest path
    queue = deque()
    visited = set()
    queue.append((start[0], start[1], 0))
    visited.add((start[0], start[1]))
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == target:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<=nx<m and 0<=ny<n and grid[nx][ny]!=0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist+1))
    return -1

# Test cases
test_cases = [
    {
        "grid": [
            [1,2],
            [-1,0]
        ],
        "expected": 2
    },
    {
        "grid": [
            [0,0,-1],
            [1,1,1],
            [2,0,0]
        ],
        "expected": 4
    },
    {
        "grid": [
            [-1,0],
            [0,2]
        ],
        "expected": -1
    },
    {
        "grid": [
            [-1,1,1,1],
            [0,0,0,1],
            [1,1,1,2]
        ],
        "expected": 5
    },
    {
        "grid": [
            [-1,1,0,2]
        ],
        "expected": 3
    },
    {
        "grid": [
            [-1]
        ],
        "expected": -1  # No target
    },
    {
        "grid": [
            [-1,1,1],
            [1,0,1],
            [1,1,2]
        ],
        "expected": 4
    }
]

correct = 0
total = len(test_cases)
for idx, test in enumerate(test_cases):
    grid = test["grid"]
    expected = test["expected"]
    result = find_min_distance(grid)
    if result == expected:
        print(True)
        correct +=1
    else:
        print(False)
print(f"{correct}/{total}")