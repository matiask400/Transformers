def pacific_atlantic(heights):
    """
    Finds the grid coordinates where water can flow to both the Pacific and Atlantic oceans.

    Args:
        heights: An m x n integer matrix representing the height of each unit cell.

    Returns:
        A list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
    """

    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(i, j, visited):
        if (i, j) in visited:
            return

        visited.add((i, j))

        # Move up
        if i > 0 and heights[i - 1][j] >= heights[i][j]:
            dfs(i - 1, j, visited)
        # Move down
        if i < m - 1 and heights[i + 1][j] >= heights[i][j]:
            dfs(i + 1, j, visited)
        # Move left
        if j > 0 and heights[i][j - 1] >= heights[i][j]:
            dfs(i, j - 1, visited)
        # Move right
        if j < n - 1 and heights[i][j + 1] >= heights[i][j]:
            dfs(i, j + 1, visited)

    # Pacific Ocean (left and top edges)
    for i in range(m):
        dfs(i, 0, pacific)
    for j in range(n):
        dfs(0, j, pacific)

    # Atlantic Ocean (right and bottom edges)
    for i in range(m):
        dfs(i, n - 1, atlantic)
    for j in range(n):
        dfs(m - 1, j, atlantic)

    # Find the intersection of Pacific and Atlantic reachable cells
    result = []
    for i in range(m):
        for j in range(n):
            if (i, j) in pacific and (i, j) in atlantic:
                result.append([i, j])

    return result


def test_pacific_atlantic():
    """
    Tests the pacific_atlantic function with the provided examples.
    """

    tests = [
        {
            "input": [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
            "expected": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        },
        {
            "input": [[2, 1], [1, 2]],
            "expected": [[0, 0], [0, 1], [1, 0], [1, 1]]
        }
    ]

    correct_tests = 0
    total_tests = len(tests)

    for i, test in enumerate(tests):
        input_heights = test["input"]
        expected_output = test["expected"]
        actual_output = pacific_atlantic(input_heights)

        # Sort both lists to ensure order doesn't matter
        actual_output.sort()
        expected_output.sort()

        if actual_output == expected_output:
            print(f"Test {i + 1}: True")
            correct_tests += 1
        else:
            print(f"Test {i + 1}: False")
            print(f"  Input: {input_heights}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")


if __name__ == "__main__":
    test_pacific_atlantic()