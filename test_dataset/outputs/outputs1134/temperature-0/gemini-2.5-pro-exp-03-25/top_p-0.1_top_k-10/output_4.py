import collections
import itertools

def solve():
    """
    Solves the sliding puzzle problem using Breadth-First Search (BFS).
    Finds the minimum number of moves to reach the target state [[1,2,3],[4,5,0]].
    """
    def slidingPuzzle(board):
        """
        Calculates the minimum moves to solve the 2x3 sliding puzzle.

        Args:
            board: A list of lists representing the initial state of the board.

        Returns:
            The minimum number of moves, or -1 if unsolvable.
        """
        rows, cols = 2, 3
        target_tuple = ((1, 2, 3), (4, 5, 0))
        start_tuple = tuple(tuple(row) for row in board)

        if start_tuple == target_tuple:
            return 0

        # Find the initial position of the empty square (0)
        start_zero_pos = None
        for r in range(rows):
            for c in range(cols):
                if start_tuple[r][c] == 0:
                    start_zero_pos = (r, c)
                    break
            if start_zero_pos:
                break

        # --- Optional Parity Check (Optimization) ---
        # Flatten the board ignoring 0 for inversion count
        def get_inversions(board_tuple):
            flat = [val for row in board_tuple for val in row if val != 0]
            count = 0
            for i in range(len(flat)):
                for j in range(i + 1, len(flat)):
                    if flat[i] > flat[j]:
                        count += 1
            return count

        # Target state [[1,2,3],[4,5,0]] -> (1, 2, 3, 4, 5) -> 0 inversions (even)
        # Target zero row is 1.
        # For a 2x3 board, solvability depends only on the inversion count parity.
        # If the number of inversions is odd, it's unsolvable.
        # (This specific rule applies because the width 3 is odd. If width were even,
        # the row of the blank would also matter).
        # start_inversions = get_inversions(start_tuple)
        # if start_inversions % 2 != 0:
        #     return -1
        # --- End Optional Parity Check ---
        # Note: BFS will correctly determine unsolvability even without the parity check,
        # it just might take longer exploring the entire reachable state space.
        # Let's rely on BFS for correctness as requested by the problem structure.

        # BFS setup
        queue = collections.deque([(start_tuple, start_zero_pos, 0)]) # (state, zero_pos, moves)
        visited = {start_tuple}
        
        # Directions for moving the empty square
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while queue:
            current_state_tuple, zero_pos, moves = queue.popleft()

            if current_state_tuple == target_tuple:
                return moves

            zero_r, zero_c = zero_pos

            # Try moving the zero in all 4 directions
            for i in range(4):
                new_r, new_c = zero_r + dr[i], zero_c + dc[i]

                # Check if the new position is valid
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    # Create the next state by swapping
                    current_state_list = [list(row) for row in current_state_tuple]
                    
                    # Swap the zero and the adjacent tile
                    current_state_list[zero_r][zero_c], current_state_list[new_r][new_c] = \
                        current_state_list[new_r][new_c], current_state_list[zero_r][zero_c]

                    next_state_tuple = tuple(tuple(row) for row in current_state_list)
                    
                    # If this state hasn't been visited, add it to the queue and visited set
                    if next_state_tuple not in visited:
                        visited.add(next_state_tuple)
                        queue.append((next_state_tuple, (new_r, new_c), moves + 1))

        # If the queue becomes empty and target wasn't found, it's impossible
        return -1

    # --- Test Cases ---
    test_cases = [
        ([[1, 2, 3], [4, 0, 5]], 1),
        ([[1, 2, 3], [5, 4, 0]], -1),
        ([[4, 1, 2], [5, 0, 3]], 5),
        ([[3, 2, 4], [1, 5, 0]], 14),
        ([[1, 2, 3], [4, 5, 0]], 0), # Already solved
        ([[5, 1, 3], [4, 0, 2]], 8), # Another solvable case
        ([[2, 3, 4], [1, 5, 0]], -1), # Unsolvable (odd inversions)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (board, expected_output) in enumerate(test_cases):
        result = slidingPuzzle(board)
        passed = result == expected_output
        print(f"Test {i+1}: Input={board}, Output={result}, Expected={expected_output} -> {passed}")
        if passed:
            correct_count += 1

    print(f"\n{correct_count}/{total_tests} tests passed.")

# Execute the solution and tests
solve()