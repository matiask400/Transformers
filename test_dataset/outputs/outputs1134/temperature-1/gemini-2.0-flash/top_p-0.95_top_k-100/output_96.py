def findCelebrity(n, knows_matrix):
    """
    Finds the celebrity in a group of n people using the given knows function.

    Args:
        n: The number of people in the group.
        knows_matrix: A matrix representing who knows whom.

    Returns:
        The label of the celebrity if there is one, or -1 if there is no celebrity.
    """

    def knows(a, b):
        """Helper function to check if person a knows person b."""
        return knows_matrix[a][b]

    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    for i in range(n):
        if i == candidate:
            continue
        if knows(candidate, i) or not knows(i, candidate):
            return -1

    return candidate


def test_findCelebrity():
    """
    Tests the findCelebrity function with various test cases.
    """

    test_cases = [
        {
            "input": {
                "n": 3,
                "knows_matrix": [[1, 1, 0], [0, 1, 0], [1, 1, 1]]
            },
            "expected": 1
        },
        {
            "input": {
                "n": 3,
                "knows_matrix": [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
            },
            "expected": -1
        },
        {
            "input": {
                "n": 2,
                "knows_matrix": [[1, 0], [0, 1]]
            },
            "expected": 1
        },
        {
            "input": {
                "n": 2,
                "knows_matrix": [[1, 0], [1, 1]]
            },
            "expected": -1
        },
        {
            "input": {
                "n": 4,
                "knows_matrix": [[1, 1, 1, 1], [0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1]]
            },
            "expected": 1
        }
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        n = test_case["input"]["n"]
        knows_matrix = test_case["input"]["knows_matrix"]
        expected = test_case["expected"]
        result = findCelebrity(n, knows_matrix)

        if result == expected:
            print(f"True")
            num_correct += 1
        else:
            print(f"False")

    print(f"{num_correct}/{total_tests}")


if __name__ == "__main__":
    test_findCelebrity()