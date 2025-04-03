def reconstruct_matrix(upper, lower, colsum):
    """
    Reconstructs a 2-D binary matrix given the sum of elements in the upper row,
    the sum of elements in the lower row, and the sum of elements in each column.

    Args:
        upper: The sum of elements in the upper row.
        lower: The sum of elements in the lower row.
        colsum: An integer array representing the sum of elements in each column.

    Returns:
        A 2-D integer array representing the reconstructed matrix, or an empty
        array if no valid solution exists.
    """

    n = len(colsum)
    matrix = [[0] * n for _ in range(2)]

    for i in range(n):
        if colsum[i] == 2:
            matrix[0][i] = 1
            matrix[1][i] = 1
            upper -= 1
            lower -= 1
        elif colsum[i] == 1:
            if upper > lower:
                matrix[0][i] = 1
                upper -= 1
            else:
                matrix[1][i] = 1
                lower -= 1

    if upper == 0 and lower == 0:
        return matrix
    else:
        return []


def test_reconstruct_matrix():
    """
    Tests the reconstruct_matrix function with several test cases.
    """

    test_cases = [
        {
            "upper": 2,
            "lower": 1,
            "colsum": [1, 1, 1],
            "expected": [[1, 1, 0], [0, 0, 1]],
        },
        {
            "upper": 2,
            "lower": 3,
            "colsum": [2, 2, 1, 1],
            "expected": [],
        },
        {
            "upper": 5,
            "lower": 5,
            "colsum": [2, 1, 2, 0, 1, 0, 1, 2, 0, 1],
            "expected": [[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]],
        },
        {
            "upper": 4,
            "lower": 7,
            "colsum": [2,1,2,1,1,1,2,2,1,1],
            "expected": [[1,0,1,0,1,0,1,1,0,0],[1,1,1,1,0,1,1,1,1,1]]
        },

        {
            "upper": 1,
            "lower": 1,
            "colsum": [2],
            "expected": [[1], [1]]
        },

        {
            "upper": 0,
            "lower": 0,
            "colsum": [0],
            "expected": [[0], [0]]
        },
        {
           "upper": 1,
           "lower": 0,
           "colsum": [1,0],
           "expected": [[1,0],[0,0]]
        }
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        upper = test_case["upper"]
        lower = test_case["lower"]
        colsum = test_case["colsum"]
        expected = test_case["expected"]

        result = reconstruct_matrix(upper, lower, colsum)
        
        passed = False
        if result is None and expected is None:
          passed = True
        elif result is not None and expected is not None:
            if len(result) == len(expected):
                if all(result[i] == expected[i] for i in range(len(result))):
                    passed = True
        if passed:
            print(f"Test {i + 1}: True")
            correct_count += 1
        else:
            print(f"Test {i + 1}: False")
            print(f"  Input: upper={upper}, lower={lower}, colsum={colsum}")
            print(f"  Expected: {expected}")
            print(f"  Result: {result}")

    print(f"\nCorrect: {correct_count}/{total_count}")


if __name__ == "__main__":
    test_reconstruct_matrix()