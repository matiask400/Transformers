def solve():
    def maxIncreaseKeepingSkyline(grid):
        rows = len(grid)
        cols = len(grid[0])
        row_skyline = [0] * rows
        col_skyline = [0] * cols

        for i in range(rows):
            row_max = 0
            for j in range(cols):
                row_max = max(row_max, grid[i][j])
            row_skyline[i] = row_max

        for j in range(cols):
            col_max = 0
            for i in range(rows):
                col_max = max(col_max, grid[i][j])
            col_skyline[j] = col_max

        total_increase = 0
        for i in range(rows):
            for j in range(cols):
                new_height = min(row_skyline[i], col_skyline[j])
                total_increase += new_height - grid[i][j]

        return total_increase

    def run_test(grid, expected_output):
        output = maxIncreaseKeepingSkyline(grid)
        if output == expected_output:
            print('True')
        else:
            print('False')

    # Test case 1
    grid1 = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    expected_output1 = 35
    run_test(grid1, expected_output1)

    # Test case 2
    grid2 = [[0,0,0],[0,0,0],[0,0,0]]
    expected_output2 = 0
    run_test(grid2, expected_output2)

    # Test case 3
    grid3 = [[1,1],[1,1]]
    expected_output3 = 0
    run_test(grid3, expected_output3)

    # Test case 4
    grid4 = [[100]]
    expected_output4 = 0
    run_test(grid4, expected_output4)

    # Test case 5
    grid5 = [[1,2,3],[4,5,6],[7,8,9]]
    row_maxes_5 = [3, 6, 9]
    col_maxes_5 = [7, 8, 9]
    expected_increase_5 = 0
    expected_output5 = 0
    for r in range(len(grid5)):
        for c in range(len(grid5[0])):
            expected_increase_5 += min(row_maxes_5[r], col_maxes_5[c]) - grid5[r][c]
    run_test(grid5, expected_output5)

    test_grids = [grid1, grid2, grid3, grid4, grid5]
    expected_outputs = [expected_output1, expected_output2, expected_output3, expected_output4, expected_output5]
    correct_tests = 0
    for i in range(len(test_grids)):
        output = maxIncreaseKeepingSkyline(test_grids[i])
        if output == expected_outputs[i]:
            print('True')
            correct_tests += 1
        else:
            print('False')
    print(f'{correct_tests}/{len(test_grids)}')

solve()