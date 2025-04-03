def solve():
    def num_distinct_islands(grid):
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        visited = [[False] * cols for _ in range(rows)]
        distinct_islands = set()

        def get_island_shape(r, c):
            shape = []
            q = [(r, c)]
            visited[r][c] = True
            shape.append((0, 0))

            while q:
                row, col = q.pop(0)
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        shape.append((nr - r, nc - c))
                        q.append((nr, nc))
            return tuple(sorted(shape))

        def normalize_shape(shape):
            min_r = min(r for r, c in shape)
            min_c = min(c for r, c in shape)
            return tuple(sorted(tuple((r - min_r, c - min_c)) for r, c in shape))

        def rotate_shape(shape):
            return tuple(sorted(tuple((c, -r)) for r, c in shape))

        def reflect_shape(shape):
            return tuple(sorted(tuple((r, -c)) for r, c in shape))

        def get_transformations(shape):
            transformations = set()
            current_shape = shape
            for _ in range(4):
                transformations.add(normalize_shape(current_shape))
                transformations.add(normalize_shape(reflect_shape(current_shape)))
                current_shape = rotate_shape(current_shape)
            return transformations

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    island_shape = get_island_shape(r, c)
                    normalized_shapes = get_transformations(island_shape)
                    is_new_island = True
                    for shape in normalized_shapes:
                        if shape in distinct_islands:
                            is_new_island = False
                            break
                    if is_new_island:
                        distinct_islands.add(normalize_shape(island_shape))
                        count += 1
        return count

    def run_test(grid, expected_output):
        grid_list = [list(row) for row in grid.splitlines()]
        output = num_distinct_islands(grid_list)
        if output == expected_output:
            print('True')
            return True
        else:
            print('False')
            return False

    test_cases = [
        (
            """11000
10000
00001
00011""",
            1
        ),
        (
            """11100
10001
01001
01110""",
            2
        ),
        (
            """010
111
010""",
            1
        ),
        (
            """00100
01110
00100""",
            1
        ),
        (
            """11
1""",
            1
        ),
        (
            """ 1
11""",
            1
        ),
        (
            """110
110""",
            1
        ),
        (
            """10
11""",
            1
        ),
        (
            """11
01""",
            1
        ),
        (
            """11
11""",
            1
        ),
        (
            """1""",
            1
        ),
        (
            """0""",
            0
        ),
        (
            """00
00""",
            0
        ),
        (
            """101
010
101""",
            2
        )

    ]

    correct_count = 0
    for grid_str, expected in test_cases:
        if run_test(grid_str, expected):
            correct_count += 1

    print(f"{correct_count}/{len(test_cases)}")

solve()