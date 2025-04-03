def possible_bipartition(N, dislikes):
    """
    Checks if it is possible to split N people into two groups such that
    no two disliked people are in the same group.

    Args:
        N: The number of people.
        dislikes: A list of tuples, where each tuple (a, b) indicates that
            people a and b dislike each other and should not be in the same group.

    Returns:
        True if it is possible to split the people into two groups, False otherwise.
    """

    graph = [[] for _ in range(N)]
    for u, v in dislikes:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    color = [0] * N  # 0: uncolored, 1: group 1, -1: group 2

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                if not dfs(neighbor, -c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(N):
        if color[i] == 0:
            if not dfs(i, 1):
                return False

    return True

def test_possible_bipartition():
    """
    Tests the possible_bipartition function with several test cases.
    """

    test_cases = [
        (4, [[1, 2], [1, 3], [2, 4]], True),
        (3, [[1, 2], [1, 3], [2, 3]], False),
        (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], False),
        (1, [], True),
        (2, [[1,2]], True),
        (6, [[1,2],[1,3],[2,4],[5,6]], True),
        (4, [], True),
        (7, [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[1,7]], False)
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (N, dislikes, expected) in enumerate(test_cases):
        result = possible_bipartition(N, dislikes)
        if result == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"\nCorrect tests: {num_correct}/{total_tests}")

if __name__ == "__main__":
    test_possible_bipartition()