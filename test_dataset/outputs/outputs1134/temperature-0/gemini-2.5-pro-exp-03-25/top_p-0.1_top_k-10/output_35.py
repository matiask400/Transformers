import copy

def solve():
    """
    Solves the Rotate Image problem and runs tests.
    """

    def rotate(matrix: list[list[int]]) -> None:
        """
        Rotates an n x n 2D matrix by 90 degrees clockwise in-place.

        Args:
            matrix: The n x n 2D list representing the image.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        # Swap matrix[i][j] with matrix[j][i]
        for i in range(n):
            # Only need to iterate through the upper triangle (j > i)
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reflect the matrix horizontally (reverse each row)
        for i in range(n):
            matrix[i].reverse() # Reverses the row in-place

    # --- Test Harness ---
    test_cases = [
        {
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "expected": [[7,4,1],[8,5,2],[9,6,3]]
        },
        {
            "input": [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
            "expected": [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        },
        {
            "input": [[1]],
            "expected": [[1]]
        },
        {
            "input": [[1,2],[3,4]],
            "expected": [[3,1],[4,2]]
        },
         {
            "input": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            "expected": [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        }
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        # Use deepcopy because the rotate function modifies the list in-place
        input_matrix = copy.deepcopy(test["input"])
        expected_output = test["expected"]

        # The function modifies input_matrix directly and returns None
        rotate(input_matrix)
        actual_output = input_matrix # The result is the modified input_matrix

        # Compare the modified matrix with the expected output
        result = actual_output == expected_output
        print(f"Test {i + 1}: {result}")
        if result:
            correct_count += 1

    print(f"{correct_count}/{total_tests} tests passed.")

# Execute the solve function
solve()