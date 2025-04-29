def solve():
    def reconstruct_matrix(upper, lower, colsum):
        n = len(colsum)
        if sum(colsum) != upper + lower:
            return []
        matrix = [[0] * n for _ in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                matrix[0][i] = 1
                matrix[1][i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 0:
                pass # already 0

        if upper < 0 or lower < 0:
            return []

        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    matrix[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    matrix[1][i] = 1
                    lower -= 1

        if upper == 0 and lower == 0:
            return matrix
        else:
            return []

    def run_test(upper, lower, colsum, expected_output):
        result = reconstruct_matrix(upper, lower, colsum)
        if result == expected_output:
            return True
        if expected_output == []:
            if result == []:
                return True
            else:
                return False
        if not result:
            return False

        rows = len(result)
        cols = len(result[0]) if rows > 0 else 0

        if rows != 2 or cols != len(colsum):
            return False

        actual_upper_sum = sum(result[0])
        actual_lower_sum = sum(result[1])
        actual_colsum = [0] * cols
        for j in range(cols):
            actual_colsum[j] = result[0][j] + result[1][j]

        if actual_upper_sum != upper:
            return False
        if actual_lower_sum != lower:
            return False
        if actual_colsum != colsum:
            return False
        return True

    test_cases = [
        {"upper": 2, "lower": 1, "colsum": [1, 1, 1], "expected_output": [[1, 1, 0], [0, 0, 1]]},
        {"upper": 2, "lower": 3, "colsum": [2, 2, 1, 1], "expected_output": []},
        {"upper": 5, "lower": 5, "colsum": [2, 1, 2, 0, 1, 0, 1, 2, 0, 1], "expected_output": [[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]]},
        {"upper": 0, "lower": 0, "colsum": [0], "expected_output": [[0], [0]]},
        {"upper": 1, "lower": 0, "colsum": [1], "expected_output": [[1], [0]]},
        {"upper": 0, "lower": 1, "colsum": [1], "expected_output": [[0], [1]]},
        {"upper": 0, "lower": 0, "colsum": [1], "expected_output": []},
        {"upper": 1, "lower": 1, "colsum": [0], "expected_output": []},
        {"upper": 1, "lower": 1, "colsum": [2], "expected_output": [[1], [1]]},
        {"upper": 2, "lower": 0, "colsum": [1, 1], "expected_output": [[1, 1], [0, 0]]},
        {"upper": 0, "lower": 2, "colsum": [1, 1], "expected_output": [[0, 0], [1, 1]]},
        {"upper": 1, "lower": 1, "colsum": [1, 1], "expected_output": [[1, 0], [0, 1]]},
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        upper = test["upper"]
        lower = test["lower"]
        colsum = test["colsum"]
        expected_output = test["expected_output"]
        passed = run_test(upper, lower, colsum, expected_output)
        print(passed)
        if passed:
            correct_tests += 1

    print(f"{correct_tests}/{total_tests}")

solve()