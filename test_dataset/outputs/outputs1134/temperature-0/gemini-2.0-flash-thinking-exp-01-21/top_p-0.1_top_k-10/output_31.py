def find_center(edges):
    """
    Finds the center of a star graph given the edges.

    Args:
        edges: A 2D integer array where edges[i] = [ui, vi] indicates an edge between nodes ui and vi.

    Returns:
        The center node of the star graph.
    """
    u1, v1 = edges[0]
    u2, v2 = edges[1]
    if u1 == u2 or u1 == v2:
        return u1
    elif v1 == u2 or v1 == v2:
        return v1
    else:
        # This case should not happen in a valid star graph, but for completeness
        return -1

def test_find_center():
    test_cases = [
        ([[1,2],[2,3],[4,2]], 2),
        ([[1,2],[5,1],[1,3],[1,4]], 1),
        ([[7,1],[1,8],[1,2],[1,9],[1,10],[1,3],[1,4],[1,5],[1,6]], 1),
        ([[2,1],[3,1]], 1)
    ]
    num_correct = 0
    total_tests = len(test_cases)
    for i, (edges, expected_output) in enumerate(test_cases):
        actual_output = find_center(edges)
        if actual_output == expected_output:
            print(True)
            num_correct += 1
        else:
            print(False)
    print(f"{num_correct}/{total_tests}")

if __name__ == '__main__':
    test_find_center()