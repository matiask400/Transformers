def find_center(edges):
    """
    Finds the center of a star graph given the edges.

    Args:
        edges: A 2D integer array where edges[i] = [ui, vi] indicates an edge between nodes ui and vi.

    Returns:
        The center node of the star graph.
    """
    node1, node2 = edges[0]
    candidate1 = node1
    candidate2 = node2

    is_center1 = True
    for edge in edges:
        u, v = edge
        if candidate1 != u and candidate1 != v:
            is_center1 = False
            break

    if is_center1:
        return candidate1

    is_center2 = True
    for edge in edges:
        u, v = edge
        if candidate2 != u and candidate2 != v:
            is_center2 = False
            break

    if is_center2:
        return candidate2

    return -1 # Should not reach here as per problem description


def run_tests():
    test_cases = [
        {
            "edges": [[1, 2], [2, 3], [4, 2]],
            "expected_output": 2
        },
        {
            "edges": [[1, 2], [5, 1], [1, 3], [1, 4]],
            "expected_output": 1
        },
        {
            "edges": [[2,1],[3,1],[4,1]],
            "expected_output": 1
        },
        {
            "edges": [[2,1],[3,2],[4,2],[5,2]],
            "expected_output": 2
        }
    ]
    num_correct = 0
    for i, test_case in enumerate(test_cases):
        edges = test_case["edges"]
        expected_output = test_case["expected_output"]
        actual_output = find_center(edges)
        if actual_output == expected_output:
            print(True)
            num_correct += 1
        else:
            print(False)
    print(f"{num_correct}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()