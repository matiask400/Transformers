def solve():
    def get_stable_bricks(grid):
        rows = len(grid)
        cols = len(grid[0])
        stable_bricks = set()
        queue = []
        for j in range(cols):
            if grid[0][j] == 1:
                stable_bricks.add((0, j))
                queue.append((0, j))

        while queue:
            r, c = queue.pop(0)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in stable_bricks:
                    stable_bricks.add((nr, nc))
                    queue.append((nr, nc))
        return stable_bricks

    def check_test_case(grid, hits, expected_output):
        original_grid = [row[:] for row in grid]
        results = []
        current_grid = [row[:] for row in original_grid]

        for hit_r, hit_c in hits:
            previous_stable_bricks = get_stable_bricks(current_grid)
            if 0 <= hit_r < len(current_grid) and 0 <= hit_c < len(current_grid[0]) and current_grid[hit_r][hit_c] == 1:
                current_grid[hit_r][hit_c] = 0
            
            current_stable_bricks = get_stable_bricks(current_grid)
            fallen_count = 0
            fallen_bricks_coords = []
            for r in range(len(original_grid)):
                for c in range(len(original_grid[0])):
                    if original_grid[r][c] == 1 and (r, c) in previous_stable_bricks and (r, c) not in current_stable_bricks:
                        fallen_count += 1
                        fallen_bricks_coords.append((r,c))

            results.append(fallen_count)

            next_grid = [row[:] for row in current_grid]
            for r, c in fallen_bricks_coords:
                if 0 <= r < len(next_grid) and 0 <= c < len(next_grid[0]):
                    next_grid[r][c] = 0
            current_grid = next_grid


        if results == expected_output:
            print('True')
        else:
            print('False')
        return results == expected_output

    test_cases = [
        {
            "grid": [[1,0,0,0],[1,1,1,0]],
            "hits": [[1,0]],
            "expected_output": [2]
        },
        {
            "grid": [[1,0,0,0],[1,1,0,0]],
            "hits": [[1,1],[1,0]],
            "expected_output": [0,0]
        },
        {
            "grid": [[1,0],[1,1]],
            "hits": [[0,0],[0,1],[1,1]],
            "expected_output": [0,0,1]
        },
        {
            "grid": [[1,1,1],[0,1,0],[0,1,0]],
            "hits": [[1,1],[2,1]],
            "expected_output": [0,0]
        },
        {
            "grid": [[1,1,1],[0,1,0],[0,1,1]],
            "hits": [[1,1],[2,1]],
            "expected_output": [0,1]
        }
    ]

    correct_count = 0
    for i, case in enumerate(test_cases):
        if check_test_case(case["grid"], case["hits"], case["expected_output"]):
            correct_count += 1

    print(f"{correct_count}/{len(test_cases)}")

solve()