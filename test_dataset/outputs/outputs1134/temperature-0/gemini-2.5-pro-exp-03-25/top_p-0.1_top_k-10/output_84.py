import collections

# Solution function
def findCircleNum(isConnected: list[list[int]]) -> int:
    """
    Finds the total number of provinces (connected components) in a graph
    represented by an adjacency matrix.

    Args:
        isConnected: An n x n matrix where isConnected[i][j] = 1 if city i
                     and city j are directly connected, and 0 otherwise.

    Returns:
        The total number of provinces.
    """
    n = len(isConnected)
    if n == 0:
        return 0

    visited = [False] * n
    num_provinces = 0

    def dfs(city):
        """Performs Depth First Search starting from a given city."""
        visited[city] = True
        for neighbor in range(n):
            # Check for direct connection and if the neighbor hasn't been visited
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    # Iterate through all cities
    for i in range(n):
        # If a city hasn't been visited, it's the start of a new province
        if not visited[i]:
            dfs(i)  # Explore all cities connected to city i
            num_provinces += 1 # Increment the province count

    return num_provinces

# Test framework
def run_tests():
    """
    Runs predefined test cases against the findCircleNum function and prints the results.
    """
    tests = [
        # Test Case 1: Example 1
        {"input": [[1,1,0],[1,1,0],[0,0,1]], "expected": 2},
        # Test Case 2: Example 2
        {"input": [[1,0,0],[0,1,0],[0,0,1]], "expected": 3},
        # Test Case 3: Single city
        {"input": [[1]], "expected": 1},
        # Test Case 4: Two connected cities
        {"input": [[1,1],[1,1]], "expected": 1},
        # Test Case 5: Two disconnected cities
        {"input": [[1,0],[0,1]], "expected": 2},
        # Test Case 6: Four cities, two provinces
        {"input": [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]], "expected": 2},
        # Test Case 7: Four cities, one province (fully connected)
        {"input": [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], "expected": 1},
        # Test Case 8: Four cities, different connections
        {"input": [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]], "expected": 2},
         # Test Case 9: Five cities
        {"input": [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]], "expected": 3},
    ]

    correct_count = 0
    total_tests = len(tests)

    for i, test in enumerate(tests):
        isConnected_input = test["input"]
        expected_output = test["expected"]
        # Make a copy if the function modifies the input, though this one doesn't
        # isConnected_copy = [row[:] for row in isConnected_input]
        actual_output = findCircleNum(isConnected_input)

        if actual_output == expected_output:
            print(f"True")
            correct_count += 1
        else:
            print(f"False")
            # Optional: Print details on failure
            # print(f"  Input: {isConnected_input}")
            # print(f"  Expected: {expected_output}")
            # print(f"  Actual: {actual_output}")

    print(f"{correct_count}/{total_tests} tests passed")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()