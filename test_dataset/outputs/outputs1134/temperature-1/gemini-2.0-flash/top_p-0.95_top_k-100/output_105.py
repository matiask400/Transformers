def num_distinct_islands2(grid):
    """
    Counts the number of distinct islands in a grid, considering rotations and reflections.

    Args:
        grid: A 2D array of 0's and 1's representing the grid.

    Returns:
        The number of distinct islands.
    """

    def dfs(i, j, path):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        path.append((i - start_i, j - start_j))
        dfs(i + 1, j, path)
        dfs(i - 1, j, path)
        dfs(i, j + 1, path)
        dfs(i, j - 1, path)

    def normalize(path):
        normalized_path = []
        for i, j in path:
            normalized_path.append((i, j))
        return tuple(sorted(normalized_path))

    def rotate(island):
        new_island = []
        for x, y in island:
            new_island.append((-y, x))
        return normalize(new_island)

    def reflect(island):
        new_island = []
        for x, y in island:
            new_island.append((x, -y))
        return normalize(new_island)

    def all_transforms(island):
        transforms = set()
        for _ in range(4):
            island = rotate(island)
            transforms.add(island)
            transforms.add(reflect(island))
        return transforms

    islands = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                path = []
                start_i = i
                start_j = j
                dfs(i, j, path)
                normalized_island = normalize(path)

                transforms = all_transforms(normalized_island)

                islands.add(min(transforms))

    return len(islands)


def test_num_distinct_islands2():
    """
    Tests the num_distinct_islands2 function.
    """
    test_cases = [
        (
            [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]],
            1,
            "Test Case 1",
        ),
        (
            [[1, 1, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]],
            2,
            "Test Case 2",
        ),
        (
            [[1, 1], [1, 0]],
            1,
            "Test Case 3",
        ),
        (
            [[1, 0], [1, 1]],
            1,
            "Test Case 4",
        ),
        (
            [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
            1,
            "Test Case 5",
        ),
        (
            [[1, 1, 0], [1, 1, 0]],
            1,
            "Test Case 6",
        ),
        (
            [[1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
            1,
            "Test Case 7",
        ),
    ]

    num_correct = 0
    for grid, expected, test_name in test_cases:
        result = num_distinct_islands2(grid)
        if result == expected:
            print(f"True - {test_name}")
            num_correct += 1
        else:
            print(f"False - {test_name}: Expected {expected}, got {result}")

    print(f"\n{num_correct}/{len(test_cases)}")


if __name__ == "__main__":
    test_num_distinct_islands2()