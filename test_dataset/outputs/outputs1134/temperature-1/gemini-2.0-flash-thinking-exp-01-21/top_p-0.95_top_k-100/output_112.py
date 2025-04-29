def find_longest_line(matrix):
    """
    Given a 01 matrix M, find the longest line of consecutive one in the matrix.
    The line could be horizontal, vertical, diagonal or anti-diagonal.

    Args:
        matrix: A list of lists representing the 01 matrix.

    Returns:
        The length of the longest line of consecutive ones.
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_length = 0

    # Check horizontal lines
    for i in range(rows):
        current_length = 0
        for j in range(cols):
            if matrix[i][j] == 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 0
        max_length = max(max_length, current_length)

    # Check vertical lines
    for j in range(cols):
        current_length = 0
        for i in range(rows):
            if matrix[i][j] == 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 0
        max_length = max(max_length, current_length)

    # Check diagonal lines (top-left to bottom-right)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                current_length = 0
                r, c = i, j
                while r < rows and c < cols and matrix[r][c] == 1:
                    current_length += 1
                    r += 1
                    c += 1
                max_length = max(max_length, current_length)

    # Check diagonal lines (top-right to bottom-left)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                current_length = 0
                r, c = i, j
                while r < rows and c >= 0 and matrix[r][c] == 1:
                    current_length += 1
                    r += 1
                    c -= 1
                max_length = max(max_length, current_length)

    return max_length

def run_tests():
    test_cases = [
        {
            "input": [[0,1,1,0], [0,1,1,0], [0,0,0,1]],
            "expected": 3
        },
        {
            "input": [[1,0,1,0], [1,1,1,1], [0,0,1,0]],
            "expected": 4
        },
        {
            "input": [[0,0,0,0], [0,0,0,0], [0,0,0,0]],
            "expected": 0
        },
        {
            "input": [[1,1,1,1], [1,1,1,1], [1,1,1,1]],
            "expected": 4
        },
        {
            "input": [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]],
            "expected": 1
        },
        {
            "input": [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]],
            "expected": 1
        },
        {
            "input": [[0,1,0,1],[1,1,1,1],[0,1,0,1]],
            "expected": 4
        },
        {
            "input": [[1]],
            "expected": 1
        },
        {
            "input": [[0]],
            "expected": 0
        },
        {
            "input": [],
            "expected": 0
        }
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        input_matrix = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = find_longest_line(input_matrix)
        if actual_output == expected_output:
            print(f"True")
            correct_count += 1
        else:
            print(f"False")
        # print(f"Test {i+1}: Input: {input_matrix}, Expected: {expected_output}, Actual: {actual_output}, Result: {'True' if actual_output == expected_output else 'False'}")

    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()