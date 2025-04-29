import collections

def solve(isConnected):
    """
    Finds the number of provinces (connected components) in a graph represented 
    by an adjacency matrix. Uses Depth First Search (DFS).

    Args:
        isConnected: An n x n matrix where isConnected[i][j] = 1 if city i 
                     and city j are directly connected, and 0 otherwise.

    Returns:
        The total number of provinces.
    """
    n = len(isConnected)
    visited = [False] * n
    count = 0

    def dfs(city):
        """Helper function to perform DFS starting from a given city."""
        visited[city] = True
        # Check all potential neighbors
        for neighbor in range(n):
            # If there's a connection and the neighbor hasn't been visited yet
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor) # Recursively visit the neighbor

    # Iterate through all cities
    for i in range(n):
        # If a city hasn't been visited, it means we found a new province
        if not visited[i]:
            dfs(i) # Explore this province completely using DFS
            count += 1 # Increment the province count

    return count

# --- Testing Framework ---
def run_tests():
    """Runs predefined tests for the solve function."""
    tests = [
        # Input: isConnected matrix, Expected Output: number of provinces
        ([[1,1,0],[1,1,0],[0,0,1]], 2),
        ([[1,0,0],[0,1,0],[0,0,1]], 3),
        ([[1]], 1),
        ([[1,1],[1,1]], 1),
        ([[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]], 2),
        ([[1,1,1],[1,1,1],[1,1,1]], 1),
        ([[1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,0],[0,1,0,1,0],[0,0,0,0,1]], 3),
        ([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]], 3),
    ]

    correct_count = 0
    print("Running Tests...")
    for i, (test_input, expected_output) in enumerate(tests):
        # It's good practice to copy input if the function might modify it,
        # although this specific DFS implementation doesn't modify isConnected.
        # test_input_copy = [row[:] for row in test_input]
        
        result = solve(test_input)
        is_correct = (result == expected_output)
        print(f"Test {i+1}: {is_correct}")
        # Optional: Print details on failure
        # if not is_correct:
        #    print(f"  Input: {test_input}")
        #    print(f"  Expected: {expected_output}")
        #    print(f"  Got: {result}")
            
        if is_correct:
            correct_count += 1

    print(f"\nResult: {correct_count} / {len(tests)} correct tests.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()