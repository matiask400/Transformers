import collections
import sys

# Increase recursion depth limit for potentially deep BFS, although unlikely needed for 10k states
# sys.setrecursionlimit(2000) 

def solve():
    """
    Solves the lock problem using Breadth-First Search (BFS).
    Finds the minimum number of turns to reach the target combination
    from "0000", avoiding deadends.
    """
    def openLock(deadends, target):
        """
        Calculates the minimum turns to open the lock.

        Args:
            deadends: A list of strings representing deadend combinations.
            target: A string representing the target combination.

        Returns:
            The minimum number of turns, or -1 if impossible.
        """
        dead_set = set(deadends)
        start_node = "0000"

        # Edge case: If the starting position is a deadend, we can't move.
        if start_node in dead_set:
            return -1
        
        # Edge case: If the target is the start, 0 moves are needed.
        if target == start_node:
            return 0

        # Initialize BFS queue with (combination, distance)
        queue = collections.deque([(start_node, 0)])
        # Keep track of visited states to avoid cycles and redundant work
        # Add deadends to visited initially so we don't explore them
        visited = set(deadends)
        visited.add(start_node)

        while queue:
            current_combination, distance = queue.popleft()

            # Generate neighbors (next possible combinations)
            for i in range(4): # Iterate through each wheel
                current_digit = int(current_combination[i])
                
                # Turn wheel forward
                next_digit_fwd = (current_digit + 1) % 10
                neighbor_fwd_list = list(current_combination)
                neighbor_fwd_list[i] = str(next_digit_fwd)
                neighbor_fwd = "".join(neighbor_fwd_list)

                if neighbor_fwd == target:
                    return distance + 1
                if neighbor_fwd not in visited:
                    visited.add(neighbor_fwd)
                    queue.append((neighbor_fwd, distance + 1))

                # Turn wheel backward
                next_digit_bwd = (current_digit - 1 + 10) % 10 # +10 handles wrap-around from 0 to 9
                neighbor_bwd_list = list(current_combination)
                neighbor_bwd_list[i] = str(next_digit_bwd)
                neighbor_bwd = "".join(neighbor_bwd_list)

                if neighbor_bwd == target:
                    return distance + 1
                if neighbor_bwd not in visited:
                    visited.add(neighbor_bwd)
                    queue.append((neighbor_bwd, distance + 1))

        # If the queue becomes empty and we haven't found the target, it's unreachable
        return -1

    # --- Testing Framework ---
    test_cases = [
        # Example 1
        ({"deadends": ["0201", "0101", "0102", "1212", "2002"], "target": "0202"}, 6),
        # Example 2
        ({"deadends": ["8888"], "target": "0009"}, 1),
        # Example 3
        ({"deadends": ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "target": "8888"}, -1),
        # Example 4
        ({"deadends": ["0000"], "target": "8888"}, -1),
        # Additional Test Cases
        ({"deadends": [], "target": "0000"}, 0), # Target is start
        ({"deadends": [], "target": "0001"}, 1), # Simple move
        ({"deadends": [], "target": "1111"}, 4), # Multiple moves
        ({"deadends": ["0001"], "target": "0002"}, 2), # Path blocked initially
        ({"deadends": ["1000", "0100", "0010", "0001"], "target": "0002"}, -1), # Target unreachable
        ({"deadends": ["0101"], "target": "9999"}, 16), # Long path (4*4 = 16 max distance in one direction)
        ({"deadends": ["0000"], "target": "0000"}, -1), # Start is deadend, but target is also start (should be -1 based on problem logic)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (inputs, expected_output) in enumerate(test_cases):
        # print(f"--- Test Case {i+1} ---")
        # print(f"Input: deadends={inputs['deadends']}, target={inputs['target']}")
        # print(f"Expected Output: {expected_output}")
        
        result = openLock(inputs["deadends"], inputs["target"])
        
        # print(f"Actual Output: {result}")
        
        if result == expected_output:
            print(f"True")
            correct_count += 1
        else:
            print(f"False")
            # Optional: Print details on failure
            # print(f"  Failed for Input: {inputs}")
            # print(f"  Expected: {expected_output}, Got: {result}")
        # print("-" * 20)

    print(f"{correct_count}/{total_tests}")

# Execute the solve function that includes the testing
solve()