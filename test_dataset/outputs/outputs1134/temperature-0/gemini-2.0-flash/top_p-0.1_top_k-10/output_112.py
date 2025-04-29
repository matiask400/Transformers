def longest_line(matrix):
    """
    Finds the longest line of consecutive ones in a 01 matrix.

    Args:
        matrix: A list of lists representing the 01 matrix.

    Returns:
        The length of the longest line of consecutive ones.
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_len = 0

    # Horizontal
    for i in range(rows):
        count = 0
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0

    # Vertical
    for j in range(cols):
        count = 0
        for i in range(rows):
            if matrix[i][j] == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0

    # Diagonal (top-left to bottom-right)
    for i in range(rows):
        count = 0
        r, c = i, 0
        while r < rows and c < cols:
            if matrix[r][c] == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0
            r += 1
            c += 1

    for j in range(1, cols):
        count = 0
        r, c = 0, j
        while r < rows and c < cols:
            if matrix[r][c] == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0
            r += 1
            c += 1

    # Anti-diagonal (top-right to bottom-left)
    for i in range(rows):
        count = 0
        r, c = i, cols - 1
        while r < rows and c >= 0:
            if matrix[r][c] == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0
            r += 1
            c -= 1

    for j in range(cols - 2, -1, -1):
        count = 0
        r, c = 0, j
        while r < rows and c >= 0:
            if matrix[r][c] == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0
            r += 1
            c -= 1

    return max_len


def test_longest_line():
    test_cases = [
        ([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]], 3),
        ([[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]], 4),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 1),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3),
        ([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]], 1),
        ([[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1]], 2),
        ([], 0),
        ([[]], 0),
        ([[1]], 1)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (matrix, expected) in enumerate(test_cases):
        result = longest_line(matrix)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_longest_line()