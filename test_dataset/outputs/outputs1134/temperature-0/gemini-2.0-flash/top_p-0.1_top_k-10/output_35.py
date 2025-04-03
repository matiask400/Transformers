def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp

def test_rotate_matrix():
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
         [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]])
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_matrix, expected_output) in enumerate(test_cases):
        matrix_copy = [row[:] for row in input_matrix]  # Create a deep copy
        rotate_matrix(matrix_copy)
        if matrix_copy == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    test_rotate_matrix()