def count_distinct_islands(grid):
    from collections import deque

    def dfs(x, y, island):
        stack = [(x, y)]
        grid[x][y] = 0
        while stack:
            i, j = stack.pop()
            island.append((i, j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    stack.append((ni, nj))

    def normalize(shape):
        transformations = []
        for k in range(8):
            transformed = []
            for x, y in shape:
                if k == 0:
                    tx, ty = x, y
                elif k == 1:
                    tx, ty = x, -y
                elif k == 2:
                    tx, ty = -x, y
                elif k == 3:
                    tx, ty = -x, -y
                elif k == 4:
                    tx, ty = y, x
                elif k == 5:
                    tx, ty = y, -x
                elif k == 6:
                    tx, ty = -y, x
                elif k == 7:
                    tx, ty = -y, -x
                transformed.append((tx, ty))
            transformed.sort()
            min_x = transformed[0][0]
            min_y = transformed[0][1]
            normalized = tuple((x - min_x, y - min_y) for x, y in transformed)
            transformations.append(normalized)
        return min(transformations)

    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    unique_islands = set()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                island = []
                dfs(i, j, island)
                norm = normalize(island)
                unique_islands.add(norm)

    return len(unique_islands)

# Test cases
def run_tests():
    tests = [
        {
            "grid": [
                [1,1,0,0,0],
                [1,0,0,0,0],
                [0,0,0,0,1],
                [0,0,0,1,1]
            ],
            "expected": 1
        },
        {
            "grid": [
                [1,1,1,0,0],
                [1,0,0,0,1],
                [0,1,0,0,1],
                [0,1,1,1,0]
            ],
            "expected": 2
        }
    ]
    
    correct = 0
    for test in tests:
        # Deep copy the grid to avoid mutation
        from copy import deepcopy
        grid_copy = deepcopy(test["grid"])
        result = count_distinct_islands(grid_copy)
        pass_test = result == test["expected"]
        print(pass_test)
        if pass_test:
            correct += 1
    print(f"{correct}/{len(tests)}")

run_tests()