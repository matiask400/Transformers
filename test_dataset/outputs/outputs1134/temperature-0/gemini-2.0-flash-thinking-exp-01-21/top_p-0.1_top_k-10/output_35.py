def rotate_matrix(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    return matrix

def test_rotate_matrix():
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
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i in range(total_tests):
        test_case = test_cases[i]
        input_matrix = [row[:] for row in test_case["input"]] # Deep copy to avoid modifying original test input
        expected_output = test_case["expected"]
        rotated_matrix = rotate_matrix(input_matrix)

        if rotated_matrix == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_rotate_matrix()