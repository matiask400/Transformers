class GridMaster:
    def __init__(self, grid):
        self.grid = grid
        self.robot_pos = None
        self.target_pos = None
        self.rows = len(grid)
        self.cols = len(grid[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == -1:
                    self.robot_pos = [r, c]
                elif grid[r][c] == 2:
                    self.target_pos = [r, c]

    def canMove(self, direction):
        r, c = self.robot_pos
        if direction == 'U':
            nr, nc = r - 1, c
        elif direction == 'D':
            nr, nc = r + 1, c
        elif direction == 'L':
            nr, nc = r, c - 1
        elif direction == 'R':
            nr, nc = r, c + 1
        else:
            return False

        if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != 0:
            return True
        return False

    def move(self, direction):
        if self.canMove(direction):
            r, c = self.robot_pos
            if direction == 'U':
                self.robot_pos = [r - 1, c]
            elif direction == 'D':
                self.robot_pos = [r + 1, c]
            elif direction == 'L':
                self.robot_pos = [r, c - 1]
            elif direction == 'R':
                self.robot_pos = [r, c + 1]

    def isTarget(self):
        return self.robot_pos == self.target_pos

def find_shortest_path(grid):
    master = GridMaster(grid)

    def solve():
        grid_map = {}
        target_pos = None

        def explore(r, c):
            nonlocal target_pos
            grid_map[(r, c)] = 1  # Mark as visited and empty initially
            if master.isTarget():
                grid_map[(r, c)] = 2
                target_pos = (r, c)

            for direction in ['U', 'D', 'L', 'R']:
                nr, nc = r, c
                if direction == 'U': nr -= 1
                elif direction == 'D': nr += 1
                elif direction == 'L': nc -= 1
                elif direction == 'R': nc += 1

                if master.canMove(direction):
                    if (nr, nc) not in grid_map:
                        master.move(direction)
                        explore(nr, nc)
                        reverse_direction = ''
                        if direction == 'U': reverse_direction = 'D'
                        elif direction == 'D': reverse_direction = 'U'
                        elif direction == 'L': reverse_direction = 'R'
                        elif direction == 'R': reverse_direction = 'L'
                        master.move(reverse_direction) # Backtrack

        explore(0, 0) # Start exploration from assumed (0,0) relative to start

        if target_pos is None:
            return -1

        q = [(0, 0, 0)] # (r, c, distance)
        visited_bfs = {(0, 0)}

        while q:
            r, c, dist = q.pop(0)
            if (r, c) == target_pos:
                return dist

            for direction in ['U', 'D', 'L', 'R']:
                nr, nc = r, c
                if direction == 'U': nr -= 1
                elif direction == 'D': nr += 1
                elif direction == 'L': nc -= 1
                elif direction == 'R': nc += 1

                if (nr, nc) in grid_map and grid_map[(nr, nc)] != 0 and (nr, nc) not in visited_bfs:
                    visited_bfs.add((nr, nc))
                    q.append((nr, nc, dist + 1))
        return -1

    return solve()


def run_tests():
    test_cases = [
        ([[1, 2], [-1, 0]], 2),
        ([[0, 0, -1], [1, 1, 1], [2, 0, 0]], 4),
        ([[-1, 0], [0, 2]], -1),
        ([[1,1,1],[1,-1,1],[1,1,2]], 2),
        ([[1,1,1],[1,-1,0],[1,1,2]], 4),
        ([[0,0,0],[-1,1,2],[0,0,0]], -1),
        ([[-1,1,1],[0,1,1],[2,1,1]], 4),
        ([[1,1,1],[1,1,1],[-1,1,2]], 2),
        ([[1,1,1],[1,1,1],[1,1,-1],[1,1,2]], 3),
        ([[1,1,1],[1,1,1],[1,1,1],[-1,1,2]], 4),
        ([[1,1,1],[1,1,1],[1,1,1],[1,1,1],[-1,1,2]], 5),
        ([[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[-1,1,2]], 6),
        ([[1,1,1,1,1,1],[-1,1,1,1,1,1],[1,1,1,1,1,2]], 2),
        ([[1,1,1,1,1,1],[1,1,1,1,1,1],[-1,1,1,1,1,2]], 3),
        ([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[-1,1,1,1,1,2]], 4),
        ([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[-1,1,1,1,1,2]], 5),
        ([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[-1,1,1,1,1,2]], 6),
        ([[1,1,1,1,1,1,1],[-1,1,1,1,1,1,1],[1,1,1,1,1,1,2]], 2),
        ([[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[-1,1,1,1,1,1,2]], 3),
        ([[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[-1,1,1,1,1,1,2]], 4),
        ([[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[-1,1,1,1,1,1,2]], 5),
        ([[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[-1,1,1,1,1,1,2]], 6),
        ([[1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,2]], 2),
        ([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,2]], 3),
        ([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,2]], 4),
        ([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,2]], 5),
        ([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,2]], 6),
        ([[1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,2]], 2),
        ([[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,2]], 3),
        ([[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,2]], 4),
        ([[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,2]], 5),
        ([[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,2]], 6),
        ([[1,1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,2]], 2),
        ([[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,1,2]], 3),
        ([[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,1,2]], 4),
        ([[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,1,2]], 5),
        ([[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,1,2]], 6),

    ]

    correct_count = 0
    for i, (grid, expected_output) in enumerate(test_cases):
        result = find_shortest_path(grid)
        if result == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected_output}, Got: {result})")

    print(f"\n{correct_count}/{len(test_cases)} correct")

if __name__ == '__main__':
    run_tests()