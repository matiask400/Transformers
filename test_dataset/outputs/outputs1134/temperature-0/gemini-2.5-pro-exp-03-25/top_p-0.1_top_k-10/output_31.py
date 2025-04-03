import collections

def findCenter(edges: list[list[int]]) -> int:
    """
    Finds the center of a star graph given its edges.

    A star graph has one central node connected to all other n-1 nodes.
    Since every edge must connect to the center, the center node must
    be present in every edge. Therefore, we only need to look at the
    first two edges. The node common to both edges is the center.

    Args:
        edges: A list of lists, where each inner list [u, v] represents
               an edge between nodes u and v.

    Returns:
        The label of the center node.
    """
    # The center node must be present in the first edge.
    node1 = edges[0][0]
    node2 = edges[0][1]

    # The center node must also be present in the second edge.
    # Check if node1 from the first edge is present in the second edge.
    if node1 == edges[1][0] or node1 == edges[1][1]:
        return node1
    else:
        # If node1 is not in the second edge, then node2 must be the center.
        return node2

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the findCenter function and prints the results.
    """
    test_cases = [
        # Format: (input_edges, expected_output)
        ([[1, 2], [2, 3], [4, 2]], 2),
        ([[1, 2], [5, 1], [1, 3], [1, 4]], 1),
        ([[3, 5], [1, 5], [2, 5], [4, 5]], 5), # Center not 1 or 2
        ([[1, 100], [2, 100], [3, 100]], 100), # Larger node labels
        ([[9, 7], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 8]], 7), # Center is 7
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (edges, expected) in enumerate(test_cases):
        result = findCenter(edges)
        is_correct = (result == expected)
        print(f"{is_correct}")
        if is_correct:
            correct_count += 1

    print(f"\n{correct_count} / {total_tests} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()