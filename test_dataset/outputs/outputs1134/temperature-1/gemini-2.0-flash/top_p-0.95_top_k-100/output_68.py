def numMagicSquaresInside(grid):
    """
    Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?
    (Each subgrid is contiguous).

    Args:
        grid: A list of lists of integers.

    Returns:
        The number of 3 x 3 magic square subgrids.
    """

    def is_magic_square(subgrid):
        """
        Checks if a 3 x 3 grid is a magic square.

        Args:
            subgrid: A 3 x 3 grid of integers.

        Returns:
            True if the grid is a magic square, False otherwise.
        """

        if len(subgrid) != 3 or len(subgrid[0]) != 3:
            return False

        nums = set()
        for row in subgrid:
            for num in row:
                if num < 1 or num > 9 or num in nums:
                    return False
                nums.add(num)

        magic_constant = 15  # Sum of each row, column, and diagonal in a 3x3 magic square with numbers 1-9

        # Check rows
        for row in subgrid:
            if sum(row) != magic_constant:
                return False

        # Check columns
        for col in range(3):
            if sum(subgrid[row][col] for row in range(3)) != magic_constant:
                return False

        # Check diagonals
        if subgrid[0][0] + subgrid[1][1] + subgrid[2][2] != magic_constant:
            return False

        if subgrid[0][2] + subgrid[1][1] + subgrid[2][0] != magic_constant:
            return False

        return True

    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = [
                [grid[i][j], grid[i][j + 1], grid[i][j + 2]],
                [grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2]],
                [grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]],
            ]
            if is_magic_square(subgrid):
                count += 1

    return count


def test_numMagicSquaresInside():
    test_cases = [
        ([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]], 1),
        ([[8]], 0),
        ([[4, 4], [3, 3]], 0),
        ([[4, 7, 8], [9, 5, 1], [2, 3, 6]], 0),
        ([[1,8,6],[10,5,0],[4,2,9]], 0),
        ([[5,5,5],[5,5,5],[5,5,5]], 0),
        ([[3,2,9,2],[4,5,6,8],[6,7,1,9],[8,9,2,4],[5,1,3,8]], 0),
        ([[7,2,5],[4,5,8],[1,6,9]], 0),
        ([[5, 8, 1, 6],[2, 3, 4, 7],[9, 5, 7, 6],[4, 1, 2, 8]], 0),
        ([[10,3,5],[1,6,11],[7,9,2]],0)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (grid, expected) in enumerate(test_cases):
        result = numMagicSquaresInside(grid)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"\nCorrect: {correct_count}/{total_tests}")


if __name__ == "__main__":
    test_numMagicSquaresInside()