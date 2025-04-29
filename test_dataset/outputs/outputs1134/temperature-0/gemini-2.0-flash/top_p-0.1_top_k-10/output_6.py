def reconstruct_matrix(upper, lower, colsum):
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
    test_cases = [
        (2, 1, [1, 1, 1], [[1, 1, 0], [0, 0, 1]]),
        (2, 3, [2, 2, 1, 1], []),
        (5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1], [[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]]),
        (2, 2, [2, 0, 2, 0], [[1, 0, 1, 0], [1, 0, 1, 0]]),
        (0, 0, [0, 0, 0, 0], [[0, 0, 0, 0], [0, 0, 0, 0]]),
        (1, 0, [1, 0], [[1, 0], [0, 0]]),
        (0, 1, [0, 1], [[0, 0], [0, 1]]),
        (1, 1, [2], [[1], [1]]),
        (1, 1, [0], []),
        (1, 1, [1,1], [[1,0],[0,1]])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for upper, lower, colsum, expected in test_cases:
        result = reconstruct_matrix(upper, lower, colsum)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: upper={upper}, lower={lower}, colsum={colsum}")
            print(f"Expected: {expected}")
            print(f"Got: {result}")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_reconstruct_matrix()