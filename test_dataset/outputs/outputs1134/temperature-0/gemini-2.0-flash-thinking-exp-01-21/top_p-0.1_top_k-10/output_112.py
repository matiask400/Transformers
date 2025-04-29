def longest_line_of_ones(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_length = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                # Horizontal
                count = 0
                for k in range(j, cols):
                    if matrix[i][k] == 1:
                        count += 1
                    else:
                        break
                max_length = max(max_length, count)

                # Vertical
                count = 0
                for k in range(i, rows):
                    if matrix[k][j] == 1:
                        count += 1
                    else:
                        break
                max_length = max(max_length, count)

                # Diagonal
                count = 0
                for k in range(min(rows - i, cols - j)):
                    if matrix[i + k][j + k] == 1:
                        count += 1
                    else:
                        break
                max_length = max(max_length, count)

                # Anti-diagonal
                count = 0
                for k in range(min(rows - i, j + 1)):
                    if matrix[i + k][j - k] == 1:
                        count += 1
                    else:
                        break
                max_length = max(max_length, count)

    return max_length

def run_tests():
    test_cases = [
        {
            "input": [[0,1,1,0], [0,1,1,0], [0,0,0,1]],
            "expected": 3
        },
        {
            "input": [[1,0,1,0], [1,1,1,1], [0,1,1,0]],
            "expected": 4
        },
        {
            "input": [[0,0,0], [0,0,0]],
            "expected": 0
        },
        {
            "input": [[1,1,1], [1,1,1], [1,1,1]],
            "expected": 3
        },
        {
            "input": [[1]],
            "expected": 1
        },
        {
            "input": [[]],
            "expected": 0
        },
        {
            "input": [[0, 1], [1, 0]],
            "expected": 1
        },
        {
            "input": [[1, 1], [1, 1]],
            "expected": 2
        },
        {
            "input": [[0,0,1,0,0],
                      [0,0,1,1,0],
                      [0,1,1,1,0],
                      [1,1,1,1,1],
                      [0,0,0,0,0]],
            "expected": 5
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        actual_output = longest_line_of_ones(test["input"])
        if actual_output == test["expected"]:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()