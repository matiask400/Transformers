def is_magic_square(grid):
    if not grid or len(grid) != 3 or len(grid[0]) != 3:
        return False

    nums = []
    for r in range(3):
        for c in range(3):
            nums.append(grid[r][c])

    for num in nums:
        if not (1 <= num <= 9):
            return False
    if len(set(nums)) != 9:
        return False

    magic_sum = 15
    for r in range(3):
        if sum(grid[r]) != magic_sum:
            return False
    for c in range(3):
        if sum(grid[r][c] for r in range(3)) != magic_sum:
            return False
    if sum(grid[i][i] for i in range(3)) != magic_sum:
        return False
    if sum(grid[i][2 - i] for i in range(3)) != magic_sum:
        return False

    return True

def numMagicSquaresInsideGrid(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    if rows < 3 or cols < 3:
        return 0

    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = [grid[r][j:j+3] for r in range(i, i+3)]
            if is_magic_square(subgrid):
                count += 1
    return count

def run_tests():
    test_cases = [
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1),
        ([[8]], 0),
        ([[4,4],[3,3]], 0),
        ([[4,7,8],[9,5,1],[2,3,6]], 0),
        ([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], 0),
        ([[2,7,6],[9,5,1],[4,3,8]], 1),
        ([[4,9,2],[3,5,7],[8,1,6]], 1),
        ([[8,1,6],[3,5,7],[4,9,2]], 1),
        ([[6,1,8],[7,5,3],[2,9,4]], 1),
        ([[2,9,4],[7,5,3],[6,1,8]], 1),
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2],[4,3,8,4]], 1),
        ([[4,3,8,4,4],[9,5,1,9,4],[2,7,6,2,4],[4,3,8,4,4],[4,3,8,4,4]], 1),
        ([[1,2,3],[4,5,6],[7,8,9]], 0),
        ([[10,11,12],[13,14,15],[16,17,18]], 0),
        ([[1,1,1],[1,1,1],[1,1,1]], 0)
    ]

    correct_count = 0
    for i, (input_grid, expected_output) in enumerate(test_cases):
        actual_output = numMagicSquaresInsideGrid(input_grid)
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()