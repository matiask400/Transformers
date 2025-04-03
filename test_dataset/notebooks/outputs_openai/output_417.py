def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    m, n = len(heights), len(heights[0])
    from collections import deque

    def bfs(starts):
        visited = set()
        q = deque(starts)
        for x, y in starts:
            visited.add((x, y))
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m and 0 <= ny < n and
                    (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]):
                    visited.add((nx, ny))
                    q.append((nx, ny))
        return visited

    pacific_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
    atlantic_starts = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]

    pacific_reachable = bfs(pacific_starts)
    atlantic_reachable = bfs(atlantic_starts)

    result = list(map(list, pacific_reachable & atlantic_reachable))
    return sorted(result)

def run_tests():
    tests = [
        (
            [[1,2,2,3,5],
             [3,2,3,4,4],
             [2,4,5,3,1],
             [6,7,1,4,5],
             [5,1,1,2,4]],
            [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        ),
        (
            [[2,1],
             [1,2]],
            [[0,0],[0,1],[1,0],[1,1]]
        )
    ]
    passed = 0
    for idx, (input_heights, expected) in enumerate(tests):
        output = pacificAtlantic(input_heights)
        sorted_output = sorted(output)
        sorted_expected = sorted(expected)
        if sorted_output == sorted_expected:
            print('True')
            passed +=1
        else:
            print('False')
    print(f"{passed}/{len(tests)}")

run_tests()