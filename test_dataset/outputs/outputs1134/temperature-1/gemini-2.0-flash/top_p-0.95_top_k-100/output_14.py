def pacific_atlantic(heights):
    """
    Finds the grid coordinates where water can flow to both the Pacific and Atlantic oceans.

    Args:
        heights: An m x n integer matrix representing the height of each unit cell in a continent.

    Returns:
        A list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
    """

    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(row, col, visited):
        if (row, col) in visited:
            return

        visited.add((row, col))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < m and 0 <= new_col < n and heights[new_row][new_col] >= heights[row][col]:
                dfs(new_row, new_col, visited)

    # Start DFS from Pacific ocean edges
    for i in range(m):
        dfs(i, 0, pacific)
    for j in range(n):
        dfs(0, j, pacific)

    # Start DFS from Atlantic ocean edges
    for i in range(m):
        dfs(i, n - 1, atlantic)
    for j in range(n):
        dfs(m - 1, j, atlantic)

    # Find the intersection of Pacific and Atlantic sets
    result = []
    for i in range(m):
        for j in range(n):
            if (i, j) in pacific and (i, j) in atlantic:
                result.append([i, j])

    return result


def test_pacific_atlantic():
    """Tests the pacific_atlantic function."""

    test_cases = [
        {
            "input": [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
            "expected": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        },
        {
            "input": [[2, 1], [1, 2]],
            "expected": [[0, 0], [0, 1], [1, 0], [1, 1]],
        },
        {
            "input": [[1, 1], [1, 1]],
            "expected": [[0, 0], [0, 1], [1, 0], [1, 1]],
        },
        {
            "input": [[1]],
            "expected": [[0, 0]],
        },
        {
            "input": [[1,2,3],[8,9,4],[7,6,5]],
            "expected": [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
        }
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        input_heights = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = pacific_atlantic(input_heights)

        # Sort both lists of lists to compare them correctly
        actual_output.sort()
        expected_output.sort()

        if actual_output == expected_output:
            print(f"Test {i + 1}: True")
            num_correct += 1
        else:
            print(f"Test {i + 1}: False")
            print(f"  Input: {input_heights}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")

    print(f"\n{num_correct}/{len(test_cases)} correct")

if __name__ == "__main__":
    test_pacific_atlantic()