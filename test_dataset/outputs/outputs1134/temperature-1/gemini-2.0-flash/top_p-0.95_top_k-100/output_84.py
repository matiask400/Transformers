def find_num_provinces(isConnected):
    """
    Finds the total number of provinces in a given graph represented by an adjacency matrix.

    Args:
      isConnected: An n x n matrix where isConnected[i][j] = 1 if the ith city and the jth city
        are directly connected, and isConnected[i][j] = 0 otherwise.

    Returns:
      The total number of provinces.
    """

    n = len(isConnected)
    visited = [False] * n
    num_provinces = 0

    def dfs(city):
        visited[city] = True
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for city in range(n):
        if not visited[city]:
            dfs(city)
            num_provinces += 1

    return num_provinces


def test_find_num_provinces():
    """
    Tests the find_num_provinces function with several test cases.
    """

    test_cases = [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1),
        ([[1]], 1),
        ([[1, 0], [0, 1]], 2),
        ([[1, 1], [1, 1]], 1),
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (isConnected, expected) in enumerate(test_cases):
        result = find_num_provinces(isConnected)
        if result == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"\nCorrect tests: {num_correct}/{total_tests}")


if __name__ == "__main__":
    test_find_num_provinces()