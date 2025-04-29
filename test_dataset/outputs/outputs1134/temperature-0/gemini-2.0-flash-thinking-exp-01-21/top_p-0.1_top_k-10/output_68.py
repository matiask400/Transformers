from typing import List

def numMagicSquaresInside(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    def is_magic_square(subgrid):
        nums = []
        for r in range(3):
            for c in range(3):
                nums.append(subgrid[r][c])

        if len(set(nums)) != 9:
            return False

        for num in nums:
            if not (1 <= num <= 9):
                return False

        magic_sum = sum(subgrid[0])

        for r in range(3):
            if sum(subgrid[r]) != magic_sum:
                return False

        for c in range(3):
            col_sum = 0
            for r in range(3):
                col_sum += subgrid[r][c]
            if col_sum != magic_sum:
                return False

        diag1_sum = 0
        diag2_sum = 0
        for i in range(3):
            diag1_sum += subgrid[i][i]
            diag2_sum += subgrid[i][2 - i]

        if diag1_sum != magic_sum or diag2_sum != magic_sum:
            return False

        return True

    if rows < 3 or cols < 3:
        return 0

    for r in range(rows - 2):
        for c in range(cols - 2):
            subgrid = [
                [grid[r][c], grid[r][c+1], grid[r][c+2]],
                [grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2]],
                [grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]]
            ]
            if is_magic_square(subgrid):
                count += 1
    return count

def test_numMagicSquaresInside():
    test_cases = [
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1),
        ([[8]], 0),
        ([[4,4],[3,3]], 0),
        ([[4,7,8],[9,5,1],[2,3,6]], 0),
        ([[2,7,6],[9,5,1],[4,3,8]], 1),
        ([[5,5,5],[5,5,5],[5,5,5]], 0),
        ([[1,2,3],[4,5,6],[7,8,9]], 0),
        ([[4,9,2],[3,5,7],[8,1,6]], 1),
        ([[4,9,2,4],[3,5,7,3],[8,1,6,8],[4,9,2,4]], 1),
        ([[7,0,5],[2,4,6],[3,8,1]], 0),
        ([[10,3,5],[1,6,12],[7,9,2]], 0)
    ]
    correct_count = 0
    for i, (input_grid, expected_output) in enumerate(test_cases):
        output = numMagicSquaresInside(input_grid)
        if output == expected_output:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False')
    print(f'{correct_count}/{len(test_cases)}')

if __name__ == '__main__':
    test_numMagicSquaresInside()