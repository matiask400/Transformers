def hitBricks(grid, hits):
    m, n = len(grid), len(grid[0])
    parent = [i for i in range(m * n +1)]
    size = [1] * (m * n +1)
    dummy = m * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        xr, yr = find(x), find(y)
        if xr == yr:
            return
        if size[xr] < size[yr]:
            xr, yr = yr, xr
        parent[yr] = xr
        size[xr] += size[yr]

    copy = [row[:] for row in grid]
    for x, y in hits:
        copy[x][y] = copy[x][y] & 1 ^1

    for y in range(n):
        if copy[0][y]:
            union(y, dummy)
    for x in range(1, m):
        for y in range(n):
            if copy[x][y]:
                index = x * n + y
                if copy[x-1][y]:
                    union(index, (x-1)*n + y)
                if y >0 and copy[x][y-1]:
                    union(index, x*n + y-1)
                if x ==0:
                    union(index, dummy)

    res = [0] * len(hits)
    for i in reversed(range(len(hits))):
        x, y = hits[i]
        if grid[x][y] ==0:
            continue
        copy[x][y] =1
        prev = size[find(dummy)]
        if x ==0:
            union(y, dummy)
        index = x * n + y
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0<=nx<m and 0<=ny<n and copy[nx][ny]:
                union(index, nx * n + ny)
        curr = size[find(dummy)]
        res[i] = max(0, curr - prev -1)
    return res

# Test cases
test_cases = [
    {
        "grid": [[1,0,0,0],[1,1,1,0]],
        "hits": [[1,0]],
        "expected": [2]
    },
    {
        "grid": [[1,0,0,0],[1,1,0,0]],
        "hits": [[1,1],[1,0]],
        "expected": [0,0]
    }
]

correct = 0
total = len(test_cases)
for test in test_cases:
    output = hitBricks(test["grid"], test["hits"])
    if output == test["expected"]:
        print("True")
        correct +=1
    else:
        print("False")
print(f"{correct}/{total}")