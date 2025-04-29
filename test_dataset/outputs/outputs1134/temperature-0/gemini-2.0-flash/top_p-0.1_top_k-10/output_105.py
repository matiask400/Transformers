def num_distinct_islands2(grid):
    """
    Counts the number of distinct islands in a 2D grid, considering rotations and reflections.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        The number of distinct islands.
    """

    def dfs(i, j, path):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        path.append((i, j))
        dfs(i + 1, j, path)
        dfs(i - 1, j, path)
        dfs(i, j + 1, path)
        dfs(i, j - 1, path)

    def normalize(island):
        min_i = min(i for i, j in island)
        min_j = min(j for i, j in island)
        return tuple(sorted((i - min_i, j - min_j) for i, j in island))

    def rotate(island):
        return tuple(sorted((j, -i) for i, j in island))

    def reflect(island):
        return tuple(sorted((i, -j) for i, j in island))

    def get_transforms(island):
        transforms = set()
        for _ in range(4):
            island = rotate(island)
            transforms.add(normalize(island))
            transforms.add(normalize(reflect(island)))
        return transforms

    islands = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island = []
                dfs(i, j, island)
                transforms = get_transforms(normalize(tuple(island)))
                islands.add(tuple(transforms))

    return len(islands)


def test_num_distinct_islands2():
    test_cases = [
        (
            [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]],
            1,
        ),
        (
            [[1, 1, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]],
            2,
        ),
        (
            [[1, 1], [1, 0]],
            1,
        ),
        (
            [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
            1,
        ),
        (
            [[1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
            1,
        ),
        (
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            1,
        ),
        (
            [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]],
            1,
        ),
        (
            [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]],
            1,
        ),
        (
            [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]],
            1,
        ),
        (
            [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]],
            1,
        ),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (grid, expected) in enumerate(test_cases):
        result = num_distinct_islands2(grid)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"\n{correct_count}/{total_count}")


if __name__ == "__main__":
    test_num_distinct_islands2()