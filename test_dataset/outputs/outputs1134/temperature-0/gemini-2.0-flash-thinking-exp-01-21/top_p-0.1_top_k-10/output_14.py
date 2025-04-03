def pacific_atlantic(heights):
    rows = len(heights)
    cols = len(heights[0])

    pacific_reachable = [[False] * cols for _ in range(rows)]
    atlantic_reachable = [[False] * cols for _ in range(rows)]

    def dfs(row, col, reachable):
        if reachable[row][col]:
            return
        reachable[row][col] = True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and heights[new_row][new_col] >= heights[row][col]:
                dfs(new_row, new_col, reachable)

    for c in range(cols):
        dfs(0, c, pacific_reachable)
    for r in range(rows):
        dfs(r, 0, pacific_reachable)

    for c in range(cols):
        dfs(rows - 1, c, atlantic_reachable)
    for r in range(rows):
        dfs(r, cols - 1, atlantic_reachable)

    result = []
    for r in range(rows):
        for c in range(cols):
            if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                result.append([r, c])
    return result

def test_pacific_atlantic(heights, expected_output):
    actual_output = pacific_atlantic(heights)
    actual_output.sort(key=lambda x: (x[0], x[1]))
    expected_output.sort(key=lambda x: (x[0], x[1]))
    if actual_output == expected_output:
        print('True')
        return True
    else:
        print('False')
        return False

if __name__ == '__main__':
    test_cases = [
        ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
        ([[2,1],[1,2]], [[0,0],[0,1],[1,0],[1,1]]),
        ([[1]], [[0,0]]),
        ([[1,2,3],[8,9,4],[7,6,5]], [[0,2],[1,2],[2,2]]),
        ([[10,10,10],[10,1,10],[10,10,10]], [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]])
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for heights, expected_output in test_cases:
        if test_pacific_atlantic(heights, expected_output):
            correct_tests += 1

    print(f"{correct_tests}/{total_tests}")