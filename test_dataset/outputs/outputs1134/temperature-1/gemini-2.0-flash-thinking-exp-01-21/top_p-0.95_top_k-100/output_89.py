class GridMaster:
    def __init__(self, grid):
        self.grid = grid
        self.robot_pos = None
        self.target_pos = None
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
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

def find_shortest_path(master):
    grid_map = {}
    target_pos_relative = None

    def explore(r, c):
        nonlocal target_pos_relative
        grid_map[(r, c)] = 1  # Mark as visited/empty

        if master.isTarget():
            target_pos_relative = (r, c)

        for direction, dr, dc in [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]:
            if master.canMove(direction):
                nr, nc = r + dr, c + dc
                if (nr, nc) not in grid_map:
                    master.move(direction)
                    explore(nr, nc)
                    master.move(reverse_direction[direction]) # Backtrack

    reverse_direction = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
    explore(0, 0) # Start exploring from relative (0,0)


    if target_pos_relative is None:
        return -1

    q = [(0, 0, 0)] # (r, c, distance)
    visited_bfs = {(0, 0)}

    while q:
        r, c, dist = q.pop(0)
        if (r, c) == target_pos_relative:
            return dist

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in grid_map and (nr, nc) not in visited_bfs:
                visited_bfs.add((nr, nc))
                q.append((nr, nc, dist + 1))
    return -1


def solve_and_test(grid):
    master = GridMaster(grid)
    expected_output = 0
    start_pos = None
    target_pos = None
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    grid_for_bfs = [['#'] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                grid_for_bfs[r][c] = 'X' # Blocked
            elif grid[r][c] == -1:
                start_pos = (r,c)
                grid_for_bfs[r][c] = '.' # Start
            elif grid[r][c] == 2:
                target_pos = (r,c)
                grid_for_bfs[r][c] = 'T' # Target
            else:
                grid_for_bfs[r][c] = '.' # Empty

    if start_pos and target_pos:
        q = [(start_pos[0], start_pos[1], 0)]
        visited_expected = {start_pos}
        path_found = False
        while q:
            r, c, dist = q.pop(0)
            if (r, c) == target_pos:
                expected_output = dist
                path_found = True
                break

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid_for_bfs[nr][nc] != 'X' and (nr, nc) not in visited_expected:
                    visited_expected.add((nr, nc))
                    q.append((nr, nc, dist + 1))
        if not path_found:
            expected_output = -1
    else:
        expected_output = -1


    actual_output = find_shortest_path(master)
    return actual_output == expected_output, actual_output, expected_output


if __name__ == '__main__':
    test_cases = [
        ([[1, 2], [-1, 0]], 2),
        ([[0, 0, -1], [1, 1, 1], [2, 0, 0]], 4),
        ([[-1, 0], [0, 2]], -1),
        ([[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1],[-1,0,0,0,1],[1,1,1,1,2]], 8),
        ([[-1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,2]], 8),
        ([[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1],[1,0,0,0,1],[-1,1,1,1,2]], 8),
        ([[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1],[1,0,0,0,-1],[1,1,1,1,2]], 8),
        ([[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1],[1,0,0,0,1],[2,1,1,1,-1]], 8),
        ([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[-1,0,0,0,2]], -1),
        ([[1,1,1],[1,1,1],[-1,1,2]], 2),
        ([[1,1,1],[1,1,2],[-1,1,1]], 2),
        ([[1,1,2],[1,1,1],[-1,1,1]], 4),
        ([[2,1,1],[1,1,1],[-1,1,1]], 6),
        ([[-1,2]], 1),
        ([[-1],[2]], 1),
        ([[-1,0,2]], -1),
        ([[2,0,-1]], -1),
        ([[-1],[0],[2]], -1),
        ([[2],[0],[-1]], -1)

    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (grid_input, expected_distance) in enumerate(test_cases):
        test_passed, actual_output, expected_output_calc = solve_and_test(grid_input)
        if test_passed:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Actual: {actual_output}, Expected calculated: {expected_output_calc}, True Expected from problem: {expected_distance})")


    print(f"\n{correct_count} correct over {total_tests}")