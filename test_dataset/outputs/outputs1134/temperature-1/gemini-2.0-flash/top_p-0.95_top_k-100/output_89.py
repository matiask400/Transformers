class GridMaster:

    def __init__(self, grid):
        self.grid = grid
        self.robot_row, self.robot_col = self.find_robot_location()

    def find_robot_location(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == -1:
                    return r, c
        return None, None

    def canMove(self, direction: str) -> bool:
        r, c = self.robot_row, self.robot_col
        if direction == 'U':
            if r > 0 and self.grid[r - 1][c] != 0:
                return True
        elif direction == 'D':
            if r < len(self.grid) - 1 and self.grid[r + 1][c] != 0:
                return True
        elif direction == 'L':
            if c > 0 and self.grid[r][c - 1] != 0:
                return True
        elif direction == 'R':
            if c < len(self.grid[r]) - 1 and self.grid[r][c + 1] != 0:
                return True
        return False

    def move(self, direction: str) -> None:
        r, c = self.robot_row, self.robot_col
        if direction == 'U' and self.canMove(direction):
            self.robot_row -= 1
        elif direction == 'D' and self.canMove(direction):
            self.robot_row += 1
        elif direction == 'L' and self.canMove(direction):
            self.robot_col -= 1
        elif direction == 'R' and self.canMove(direction):
            self.robot_col += 1

    def isTarget(self) -> bool:
        return self.grid[self.robot_row][self.robot_col] == 2


def find_shortest_path(grid):
    master = GridMaster(grid)
    start_row, start_col = master.find_robot_location()
    target_row, target_col = None, None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 2:
                target_row, target_col = r, c

    if target_row is None or target_col is None:
        return -1

    def bfs(start_row, start_col, target_row, target_col, grid):
        q = [(start_row, start_col, 0)]
        visited = set()
        visited.add((start_row, start_col))

        while q:
            row, col, dist = q.pop(0)

            if row == target_row and col == target_col:
                return dist

            directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
            for dr, dc, direction_char in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and \
                   grid[new_row][new_col] != 0 and (new_row, new_col) not in visited:
                    q.append((new_row, new_col, dist + 1))
                    visited.add((new_row, new_col))

        return -1

    return bfs(start_row, start_col, target_row, target_col, grid)


def solve():
    tests = [
        ([[1, 2], [-1, 0]], 2),
        ([[0, 0, -1], [1, 1, 1], [2, 0, 0]], 4),
        ([[-1, 0], [0, 2]], -1),
        ([[1, 1, 1], [1, -1, 1], [1, 1, 2]], 4)

    ]

    correct_count = 0
    for i, (grid, expected) in enumerate(tests):
        result = find_shortest_path(grid)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{len(tests)}")


solve()