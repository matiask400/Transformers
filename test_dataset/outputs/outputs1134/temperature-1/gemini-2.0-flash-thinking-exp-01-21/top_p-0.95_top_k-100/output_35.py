def rotate_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

def test_rotate_matrix():
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
        ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
        ([[1]], [[1]]),
        ([[1,2],[3,4]], [[3,1],[4,2]])
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for input_matrix, expected_output in test_cases:
        matrix_copy = [row[:] for row in input_matrix] # Create a copy to avoid modifying original test case
        rotate_matrix(matrix_copy)
        if matrix_copy == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')
            print(f"Input: {input_matrix}")
            print(f"Expected: {expected_output}")
            print(f"Output: {matrix_copy}")

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_rotate_matrix()