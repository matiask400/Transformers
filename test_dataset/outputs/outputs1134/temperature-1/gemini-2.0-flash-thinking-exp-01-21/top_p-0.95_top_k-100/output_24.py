import collections

def solve():
    def get_stable_bricks(grid_param):
        m, n = len(grid_param), len(grid_param[0])
        stable_bricks = set()
        visited = set()
        for c in range(n):
            if grid_param[0][c] == 1 and (0, c) not in visited:
                q = collections.deque([(0, c)])
                visited.add((0, c))
                component = set()
                component.add((0, c))
                while q:
                    r, c = q.popleft()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid_param[nr][nc] == 1 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            component.add((nr, nc))
                            q.append((nr, nc))
                stable_bricks.update(component)
        return stable_bricks

    def get_grid_value(grid_param, brick_coord):
        r, c = brick_coord
        if 0 <= r < len(grid_param) and 0 <= c < len(grid_param[0]):
            return grid_param[r][c]
        return 0

    def process_hits(grid, hits):
        m, n = len(grid), len(grid[0])
        current_grid = [row[:] for row in grid]
        result = []
        for hit in hits:
            hit_r, hit_c = hit
            grid_before_hit = [row[:] for row in current_grid]
            stable_before = get_stable_bricks(grid_before_hit)

            if 0 <= hit_r < m and 0 <= hit_c < n and current_grid[hit_r][hit_c] == 1:
                current_grid[hit_r][hit_c] = 0
            
            grid_after_hit = [row[:] for row in current_grid]
            stable_after = get_stable_bricks(grid_after_hit)

            fallen_count = 0
            for brick in stable_before:
                if brick not in stable_after and get_grid_value(grid_before_hit, brick) == 1:
                    fallen_count += 1
            result.append(fallen_count)
        return result

    grid1 = [[1,0,0,0],[1,1,1,0]]
    hits1 = [[1,0]]
    expected_output1 = [2]
    output1 = process_hits(grid1, hits1)
    test1_passed = output1 == expected_output1
    print(f'Test 1: {test1_passed}')

    grid2 = [[1,0,0,0],[1,1,0,0]]
    hits2 = [[1,1],[1,0]]
    expected_output2 = [0, 0]
    output2 = process_hits(grid2, hits2)
    test2_passed = output2 == expected_output2
    print(f'Test 2: {test2_passed}')

    grid3 = [[1,1,1],[0,1,0],[0,1,0]]
    hits3 = [[0,1],[1,1]]
    expected_output3 = [0, 1]
    output3 = process_hits(grid3, hits3)
    test3_passed = output3 == expected_output3
    print(f'Test 3: {test3_passed}')

    grid4 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    hits4 = [[9,5],[16,8],[17,8],[18,8],[19,