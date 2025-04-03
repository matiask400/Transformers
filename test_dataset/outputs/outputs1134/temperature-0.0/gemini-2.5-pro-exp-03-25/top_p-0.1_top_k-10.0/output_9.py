import collections

def pacific_atlantic(heights):
    """
    Finds all grid coordinates where water can flow to both the Pacific and Atlantic oceans.

    Args:
        heights: An m x n integer matrix representing the height of each unit cell.

    Returns:
        A list of grid coordinates [r, c] where water can flow to both oceans.
    """
    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])
    pacific_reachable = set()
    atlantic_reachable = set()
    
    pacific_q = collections.deque()
    atlantic_q = collections.deque()

    # Initialize queues with border cells
    for r in range(m):
        pacific_q.append((r, 0))
        pacific_reachable.add((r, 0))
        atlantic_q.append((r, n - 1))
        atlantic_reachable.add((r, n - 1))
        
    for c in range(n):
        pacific_q.append((0, c))
        pacific_reachable.add((0, c))
        atlantic_q.append((m - 1, c))
        atlantic_reachable.add((m - 1, c))

    def bfs(queue, reachable_set):
        """Performs BFS starting from the ocean border cells."""
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # Check if not already visited
                    if (nr, nc) not in reachable_set:
                        # Check height condition (water flows backwards uphill or level)
                        if heights[nr][nc] >= heights[r][c]:
                            reachable_set.add((nr, nc))
                            queue.append((nr, nc))

    # Run BFS from Pacific border
    bfs(pacific_q, pacific_reachable)
    
    # Run BFS from Atlantic border
    bfs(atlantic_q, atlantic_reachable)

    # Find the intersection of the two reachable sets
    result_set = pacific_reachable.intersection(atlantic_reachable)
    
    # Convert set of tuples to list of lists and sort for consistent output
    result_list = sorted([list(coord) for coord in result_set])
    
    return result_list

# --- Testing Framework ---
def run_tests():
    test_cases = [
        ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
        ([[2,1],[1,2]], [[0,0],[0,1],[1,0],[1,1]]),
        ([[1]], [[0,0]]),
        ([[1,1],[1,1],[1,1]], [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]),
        ([[10,10,10],[10,1,10],[10,10,10]], [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]),
        ([[1,2,3],[8,9,4],[7,6,5]], [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]),
        ([], []), # Empty grid
        ([[]], []), # Grid with empty rows
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (inputs, expected_output) in enumerate(test_cases):
        # Sort expected output for consistent comparison
        expected_output.sort()
        
        # Handle potential empty grid input for the function call
        if not inputs or not inputs[0]:
             actual_output = pacific_atlantic(inputs)
        else:
             actual_output = pacific_atlantic(inputs)
        
        # The function already sorts its output
        # actual_output.sort() # No need to sort again if function guarantees sorted output

        passed = actual_output == expected_output
        print(f"Test {i+1}: {passed}")
        if passed:
            correct_count += 1
        # Optional: Print details on failure
        # else:
        #     print(f"  Input: {inputs}")
        #     print(f"  Expected: {expected_output}")
        #     print(f"  Actual: {actual_output}")


    print(f"\n{correct_count} / {total_tests} tests passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()