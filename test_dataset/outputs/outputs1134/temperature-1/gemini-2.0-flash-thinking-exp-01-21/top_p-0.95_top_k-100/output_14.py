def pacific_atlantic_water_flow(heights):
    rows = len(heights)
    cols = len(heights[0])

    pacific_reachable = [[False] * cols for _ in range(rows)]
    atlantic_reachable = [[False] * cols for _ in range(rows)]

    def dfs(row, col, reachable):
        if reachable[row][col]:
            return
        reachable[row][col] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and heights[new_row][new_col] >= heights[row][col]:
                dfs(new_row, new_col, reachable)

    for col in range(cols):
        dfs(0, col, pacific_reachable)
        dfs(rows - 1, col, atlantic_reachable)

    for row in range(rows):
        dfs(row, 0, pacific_reachable)
        dfs(row, cols - 1, atlantic_reachable)

    result = []
    for row in range(rows):
        for col in range(cols):
            if pacific_reachable[row][col] and atlantic_reachable[row][col]:
                result.append([row, col])
    return result

def test_pacific_atlantic_water_flow():
    test_cases = [
        {
            "heights": [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
            "expected_output": [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        },
        {
            "heights": [[2,1],[1,2]],
            "expected_output": [[0,0],[0,1],[1,0],[1,1]]
        },
        {
            "heights": [[1]],
            "expected_output": [[0,0]]
        },
        {
            "heights": [[1,2],[3,4]],
            "expected_output": [[0,0],[0,1],[1,0],[1,1]]
        }

    ]

    correct_tests = 0
    for i, test_case in enumerate(test_cases):
        heights = test_case["heights"]
        expected_output = test_case["expected_output"]
        output = pacific_atlantic_water_flow(heights)
        if sorted(output) == sorted(expected_output):
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    test_pacific_atlantic_water_flow()