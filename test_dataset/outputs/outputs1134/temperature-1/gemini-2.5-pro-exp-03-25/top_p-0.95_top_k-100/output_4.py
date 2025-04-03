import collections
import itertools

def sliding_puzzle(board):
    """
    Solves the sliding puzzle problem using Breadth-First Search (BFS).

    Args:
        board: A list of lists representing the 2x3 puzzle board.

    Returns:
        The minimum number of moves required to solve the puzzle, or -1 if impossible.
    """
    rows, cols = 2, 3
    target_tuple = (1, 2, 3, 4, 5, 0)
    start_tuple = tuple(itertools.chain(*board)) # Flatten the board into a tuple

    if start_tuple == target_tuple:
        return 0

    # Precompute neighbors for each possible zero position (index 0 to 5)
    # Index mapping:
    # 0 1 2
    # 3 4 5
    neighbors_map = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
    }

    # BFS setup
    queue = collections.deque([(start_tuple, 0)])  # Store (state_tuple, moves)
    visited = {start_tuple}                     # Store visited states (tuples)

    while queue:
        current_state, moves = queue.popleft()

        # Find the index of the empty square (0)
        zero_idx = -1
        try:
             zero_idx = current_state.index(0)
        except ValueError:
             # Should not happen if input is valid permutation
             return -1 # Or raise an error

        # Explore neighbors by swapping 0 with adjacent tiles
        for neighbor_idx in neighbors_map[zero_idx]:
            # Create the next state tuple by swapping
            next_state_list = list(current_state)
            next_state_list[zero_idx], next_state_list[neighbor_idx] = \
                next_state_list[neighbor_idx], next_state_list[zero_idx]
            next_state_tuple = tuple(next_state_list)

            # Check if we reached the target
            if next_state_tuple == target_tuple:
                return moves + 1

            # If the new state hasn't been visited, add it to the queue and visited set
            if next_state_tuple not in visited:
                visited.add(next_state_tuple)
                queue.append((next_state_tuple, moves + 1))

    # If the queue becomes empty and target wasn't reached, it's impossible
    return -1

# --- Test Harness ---
def run_tests(test_cases):
    """
    Runs the provided test cases against the sliding_puzzle function.

    Args:
        test_cases: A list of tuples, where each tuple contains (input_board, expected_output).
    """
    correct_count = 0
    total_tests = len(test_cases)

    for i, (board, expected_output) in enumerate(test_cases):
        # Make a deep copy if necessary, although tuples make the state immutable inside BFS
        board_copy = [row[:] for row in board]
        result = sliding_puzzle(board_copy)
        passed = (result == expected_output)
        print(f"{passed}") # Print True or False for each test
        if passed:
            correct_count += 1

    print(f"\n{correct_count}/{total_tests}") # Print overall result

# --- Test Cases ---
test_cases = [
    ([[1,2,3],[4,0,5]], 1),
    ([[1,2,3],[5,4,0]], -1),
    ([[4,1,2],[5,0,3]], 5),
    ([[3,2,4],[1,5,0]], 14),
    ([[1,2,3],[4,5,0]], 0), # Test case: already solved
    ([[0,1,2],[3,4,5]], 6)  # Another test case
]

# --- Run Tests ---
if __name__ == "__main__":
    run_tests(test_cases)