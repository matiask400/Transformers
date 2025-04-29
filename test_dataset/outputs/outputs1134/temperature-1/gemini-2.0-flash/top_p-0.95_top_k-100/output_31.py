def find_center(edges):
    """
    Finds the center of a star graph.

    Args:
        edges: A 2D integer array where each edges[i] = [ui, vi] indicates an edge between nodes ui and vi.

    Returns:
        The center of the star graph.
    """
    if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
        return edges[0][0]
    else:
        return edges[0][1]

def test_find_center():
    """
    Tests the find_center function with multiple test cases.
    """
    test_cases = [
        ([[1, 2], [2, 3], [4, 2]], 2),
        ([[1, 2], [5, 1], [1, 3], [1, 4]], 1),
        ([[1, 2], [1,3]], 1),
        ([[2,1], [3,1]], 1)
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, (edges, expected) in enumerate(test_cases):
        result = find_center(edges)
        if result == expected:
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Test case {i+1} failed: expected {expected}, got {result}")

    print(f"{num_correct}/{total_tests}")

if __name__ == "__main__":
    test_find_center()