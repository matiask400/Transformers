def numMagicSquaresInside(grid):
    def isMagic(r, c):
        s = grid[r][c+0] + grid[r][c+1] + grid[r][c+2]
        # Check all unique and in 1..9
        nums = {grid[r+i][c+j] for i in range(3) for j in range(3)}
        if nums != set(range(1,10)):
            return False
        # Check rows
        for i in range(3):
            if grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != s:
                return False
        # Check columns
        for j in range(3):
            if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] != s:
                return False
        # Check diagonals
        if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
            return False
        if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
            return False
        return True

    count = 0
    rows = len(grid)
    cols = len(grid[0]) if grid else 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            if isMagic(r, c):
                count +=1
    return count

# Test cases
tests = [
    {
        "input": [[4,3,8,4],[9,5,1,9],[2,7,6,2]],
        "expected": 1
    },
    {
        "input": [[8]],
        "expected": 0
    },
    {
        "input": [[4,4],[3,3]],
        "expected": 0
    },
    {
        "input": [[4,7,8],[9,5,1],[2,3,6]],
        "expected": 0
    }
]

correct = 0
total = len(tests)
for test in tests:
    output = numMagicSquaresInside(test["input"])
    if output == test["expected"]:
        print("True")
        correct +=1
    else:
        print("False")
print(f"{correct}/{total}")