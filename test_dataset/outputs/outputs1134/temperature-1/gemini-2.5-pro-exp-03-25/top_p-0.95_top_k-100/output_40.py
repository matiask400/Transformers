import collections
import sys

# Increase recursion depth for potentially deep BFS, although iterative BFS is used.
# This might not be strictly necessary for iterative BFS but is sometimes a good precaution.
# sys.setrecursionlimit(2000) # Not actually needed for iterative BFS

def openLock(deadends, target):
    """
    Finds the minimum number of turns to reach the target lock combination,
    avoiding the deadends.

    Args:
        deadends: A list of strings representing dead-end combinations.
        target: A string representing the target combination.

    Returns:
        The minimum number of turns, or -1 if the target is unreachable.
    """
    deadends_set = set(deadends)
    start_node = "0000"

    # Edge case: If the starting node itself is a deadend, we can't move.
    if start_node in deadends_set:
        return -1

    # Edge case: If the target is the start node, 0 moves are needed.
    if target == start_node:
        return 0

    # Initialize BFS queue with the starting state and 0 moves.
    # Each element is a tuple: (current_combination, number_of_moves)
    queue = collections.deque([(start_node, 0)])

    # Keep track of visited states to avoid cycles and redundant work.
    # Add the starting node and all deadends to visited initially.
    visited = {start_node}
    visited.update(deadends_set) # Efficiently add all deadends

    while queue:
        current_state, current_moves = queue.popleft()

        # If we reached the target, return the number of moves.
        if current_state == target:
            return current_moves

        # Generate neighbors (next possible states by turning one wheel)
        for i in range(4):  # Iterate through each of the 4 wheels
            digit = int(current_state[i])
            for move in [1, -1]:  # Turn forward (+1) or backward (-1)
                # Calculate the next digit with wrap-around
                # (digit + move + 10) % 10 correctly handles 0 -> 9 and 9 -> 0
                next_digit = (digit + move + 10) % 10
                
                # Create the next state string
                next_state_list = list(current_state)
                next_state_list[i] = str(next_digit)
                next_state = "".join(next_state_list)

                # If the neighbor state hasn't been visited (and is not a deadend)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, current_moves + 1))

    # If the queue becomes empty and we haven't found the target, it's unreachable.
    return -1

# --- Test Runner ---
def solve():
    """
    Runs test cases against the openLock function and prints the results.
    """
    test_cases = [
        (["0201", "0101", "0102", "1212", "2002"], "0202", 6),
        (["8888"], "0009", 1),
        (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888", -1),
        (["0000"], "8888", -1),
        (["1111"], "0000", 0), # Target is start
        ([], "1234", 10), # No deadends, calculate moves for 1234 (1+2+3+4 or less via wrap)
        (["0001"], "0002", 2), # Need to go around 0001
        (["0009"], "0001", 2), # Need to go around 0009
        (["0010", "0090", "0100", "0900", "1000", "9000"], "0000", 0) # Start is not deadend, target is start
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (deadends, target, expected) in enumerate(test_cases):
        # Deep copy deadends if modifying it, though set conversion handles this implicitly
        result = openLock(list(deadends), target) # Pass a copy if needed
        passed = result == expected
        print(str(passed)) # Print True or False for each test
        if passed:
            correct_count += 1
        # Optional: Detailed logging during development/debugging
        # else:
        #     print(f"Test {i+1} Failed: Input=(deadends={deadends}, target={target}), Output={result}, Expected={expected}")

    # Print the final summary
    print(f"{correct_count}/{total_tests}")

# Execute the test runner function
if __name__ == "__main__":
    solve()