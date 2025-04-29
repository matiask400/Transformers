def numDistinctIslands2(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False] * cols for _ in range(rows)]
    distinct_islands = set()

    def normalize_island(island):
        min_r = min(r for r, c in island)
        min_c = min(c for r, c in island)
        return tuple(sorted([(r - min_r, c - min_c) for r, c in island]))

    def get_island_shape(r, c):
        island = []
        stack = [(r, c)]
        visited[r][c] = True
        while stack:
            row, col = stack.pop()
            island.append((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
        return normalize_island(island)

    def rotate(island):
        return normalize_island([(c, -r) for r, c in island])

    def reflect(island):
        return normalize_island([(r, -c) for r, c in island])

    def get_transformations(island):
        transformations = set()
        current_island = island
        for _ in range(4):
            transformations.add(current_island)
            transformations.add(reflect(current_island))
            current_island = rotate(current_island)
        return transformations

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                island_shape = get_island_shape(r, c)
                transformations = get_transformations(island_shape)
                if not any(trans in distinct_islands for trans in transformations):
                    distinct_islands.add(island_shape)

    return len(distinct_islands)


def test_numDistinctIslands2():
    test_cases = [
        (
            ["11000", "10000", "00001", "00011"],
            1
        ),
        (
            ["11100", "10001", "01001", "01110"],
            2
        ),
        (
            ["011", "111"],
            1
        ),
        (
            ["11", "1"],
            1
        ),
        (
            ["1", "11"],
            1
        ),
        (
            ["101", "111"],
            2
        ),
        (
            ["11", "11"],
            1
        ),
        (
            ["1"],
            1
        ),
        (
            ["0"],
            0
        ),
        (
            [],
            0
        ),
        (
            ["110", "011"],
            1
        ),
        (
            ["10", "10"],
            1
        ),
        (
            ["10", "01"],
            2
        )
    ]

    correct_count = 0
    for i, (grid, expected) in enumerate(test_cases):
        actual = numDistinctIslands2(grid)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Actual: {actual})")

    print(f"\nCorrect tests: {correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    test_numDistinctIslands2()