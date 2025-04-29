def matrix_rank_transform(matrix):
    """
    Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
    """
    m, n = len(matrix), len(matrix[0])
    ranks = [0] * (m + n)  # Separate ranks for rows and columns
    answer = [[0] * n for _ in range(m)]

    # Sort elements with their row and col indices
    elements = []
    for r in range(m):
        for c in range(n):
            elements.append((matrix[r][c], r, c))
    elements.sort()

    i = 0
    while i < len(elements):
        j = i
        group = []
        while j < len(elements) and elements[i][0] == elements[j][0]:
            val, r, c = elements[j]
            group.append((r, c))
            j += 1

        # Find maximum ranks from row and column
        row_max_ranks = [ranks[r] for r in range(m)]
        col_max_ranks = [ranks[m + c] for c in range(n)]

        for r, c in group:
            max_rank = max(row_max_ranks[r], col_max_ranks[c])
            answer[r][c] = max_rank + 1

        # Update ranks for row and column
        for r, c in group:
            ranks[r] = answer[r][c]
            ranks[m + c] = answer[r][c]

        i = j

    return answer

def test_matrix_rank_transform():
    """Tests the matrix_rank_transform function with several test cases."""

    test_cases = [
        {
            "input": [[1, 2], [3, 4]],
            "expected": [[1, 2], [2, 3]],
        },
        {
            "input": [[7, 7], [7, 7]],
            "expected": [[1, 1], [1, 1]],
        },
        {
            "input": [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]],
            "expected": [[4, 2, 3], [1, 3, 4], [5, 1, 6], [1, 3, 4]],
        },
        {
            "input": [[7, 3, 6], [1, 4, 5], [9, 8, 2]],
            "expected": [[5, 1, 4], [1, 2, 3], [6, 3, 1]],
        },
        {
          "input": [[-1, 0, 2], [0, -2, 1], [-2, 1, -3]],
          "expected": [[2, 3, 4], [3, 1, 3], [1, 4, 1]]
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_matrix = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = matrix_rank_transform(input_matrix)

        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_matrix}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")

if __name__ == "__main__":
    test_matrix_rank_transform()