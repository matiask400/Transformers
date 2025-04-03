def findCelebrity(n, knows_matrix):
    """
    Finds the celebrity in a party of n people.

    Args:
        n: The number of people in the party.
        knows_matrix: A 2D list representing the knowledge graph.
                       knows_matrix[i][j] == 1 means person i knows person j.

    Returns:
        The label of the celebrity if there is one, otherwise -1.
    """

    def knows(a, b):
        return knows_matrix[a][b]

    # Find a potential celebrity
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    # Verify the candidate is a celebrity
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1

    return candidate


def test_findCelebrity():
    test_cases = [
        {
            "n": 3,
            "graph": [[1, 1, 0], [0, 1, 0], [1, 1, 1]],
            "expected": 1,
        },
        {
            "n": 3,
            "graph": [[1, 0, 1], [1, 1, 0], [0, 1, 1]],
            "expected": -1,
        },
        {
            "n": 2,
            "graph": [[1, 0], [1, 1]],
            "expected": 0,
        },
        {
            "n": 2,
            "graph": [[1, 1], [0, 1]],
            "expected": 1,
        },
        {
            "n": 4,
            "graph": [[1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0], [1, 1, 1, 1]],
            "expected": -1,
        },
        {
            "n": 4,
            "graph": [[1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]],
            "expected": -1,
        },
        {
            "n": 4,
            "graph": [[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]],
            "expected": 0,
        },
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        n = test_case["n"]
        graph = test_case["graph"]
        expected = test_case["expected"]
        result = findCelebrity(n, graph)

        if result == expected:
            print(f"Test {i + 1}: True")
            num_correct += 1
        else:
            print(
                f"Test {i + 1}: False (Expected: {expected}, Got: {result})"
            )

    print(f"\nCorrect: {num_correct}/{total_tests}")


if __name__ == "__main__":
    test_findCelebrity()