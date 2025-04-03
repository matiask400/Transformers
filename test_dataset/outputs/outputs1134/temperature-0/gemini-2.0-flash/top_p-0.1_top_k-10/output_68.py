def numMagicSquaresInside(grid):
    def isMagicSquare(grid):
        if len(grid) != 3 or len(grid[0]) != 3:
            return False
        nums = set()
        for i in range(3):
            for j in range(3):
                num = grid[i][j]
                if num < 1 or num > 9 or num in nums:
                    return False
                nums.add(num)
        row_sums = [sum(grid[i]) for i in range(3)]
        col_sums = [sum(grid[i][j] for i in range(3)) for j in range(3)]
        diag1_sum = sum(grid[i][i] for i in range(3))
        diag2_sum = sum(grid[i][2 - i] for i in range(3))
        if len(set(row_sums + col_sums + [diag1_sum, diag2_sum])) != 1:
            return False
        return True

    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = [grid[i + r][j:j + 3] for r in range(3)]
            if isMagicSquare(subgrid):
                count += 1
    return count

def test_numMagicSquaresInside():
    test_cases = [
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1),
        ([[8]], 0),
        ([[4,4],[3,3]], 0),
        ([[4,7,8],[9,5,1],[2,3,6]], 0),
        ([[1,8,6],[10,5,0],[4,2,9]], 0),
        ([[3,9,8,5,1],[9,2,5,4,3],[7,6,1,8,0],[0,4,9,2,7],[5,2,6,3,4]], 0),
        ([[5,5,5],[5,5,5],[5,5,5]], 0),
        ([[2,2,2],[2,2,2],[2,2,2]], 0),
        ([[1,2,3],[4,5,6],[7,8,9]], 0),
        ([[2,7,6],[9,5,1],[4,3,8]], 1),
        ([[4,9,2],[3,5,7],[8,1,6]], 1),
        ([[8,1,6],[3,5,7],[4,9,2]], 1),
        ([[6,1,8],[7,5,3],[2,9,4]], 1),
        ([[6,7,2],[1,5,9],[8,3,4]], 1),
        ([[8,3,4],[1,5,9],[6,7,2]], 1),
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2],[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1),
        ([[4,3,8,4,4],[9,5,1,9,4],[2,7,6,2,4],[4,3,8,4,4],[9,5,1,9,4],[2,7,6,2,4]], 1),
        ([[4,3,8,4,4,4],[9,5,1,9,4,4],[2,7,6,2,4,4],[4,3,8,4,4,4],[9,5,1,9,4,4],[2,7,6,2,4,4]], 1),
        ([[4,3,8,4,4,4,4],[9,5,1,9,4,4,4],[2,7,6,2,4,4,4],[4,3,8,4,4,4,4],[9,5,1,9,4,4,4],[2,7,6,2,4,4,4]], 1),
        ([[4,3,8,4,4,4,4,4],[9,5,1,9,4,4,4,4],[2,7,6,2,4,4,4,4],[4,3,8,4,4,4,4,4],[9,5,1,9,4,4,4,4],[2,7,6,2,4,4,4,4]], 1),
        ([[4,3,8,4,4,4,4,4,4],[9,5,1,9,4,4,4,4,4],[2,7,6,2,4,4,4,4,4],[4,3,8,4,4,4,4,4,4],[9,5,1,9,4,4,4,4,4],[2,7,6,2,4,4,4,4,4]], 1),
        ([[4,3,8,4,4,4,4,4,4,4],[9,5,1,9,4,4,4,4,4,4],[2,7,6,2,4,4,4,4,4,4],[4,3,8,4,4,4,4,4,4,4],[9,5,1,9,4,4,4,4,4,4],[2,7,6,2,4,4,4,4,4,4]], 1),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for grid, expected in test_cases:
        result = numMagicSquaresInside(grid)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
    
    print(f"{correct_count}/{total_count}")

test_numMagicSquaresInside()