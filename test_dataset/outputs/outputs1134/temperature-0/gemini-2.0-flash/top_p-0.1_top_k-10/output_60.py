def matrix_rank_transform(matrix):
    """
    Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

    The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:
    The rank is an integer starting from 1.

    If two elements p and q are in the same row or column, then:

    If p < q then rank(p) < rank(q)
    If p == q then rank(p) == rank(q)
    If p > q then rank(p) > rank(q)
    The rank should be as small as possible.

    It is guaranteed that answer is unique under the given rules.
    """
    m = len(matrix)
    n = len(matrix[0])
    ranks = [0] * (m + n)
    indices = sorted([(matrix[i][j], i, j) for i in range(m) for j in range(n)])
    answer = [[0] * n for _ in range(m)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    i = 0
    while i < len(indices):
        j = i
        group = []
        while j < len(indices) and indices[i][0] == indices[j][0]:
            _, row, col = indices[j]
            group.append((row, col))
            j += 1

        parent = list(range(m + n))
        row_ranks = ranks[:m]
        col_ranks = ranks[m:]

        for row, col in group:
            union(row, col + m)

        temp_ranks = {}
        for row, col in group:
            root = find(row)
            temp_ranks[root] = max(row_ranks[row], col_ranks[col])

        for row, col in group:
            root = find(row)
            rank = temp_ranks[root] + 1
            answer[row][col] = rank
            ranks[row] = max(ranks[row], rank)
            ranks[col + m] = max(ranks[col + m], rank)

        i = j

    return answer


def test_matrix_rank_transform():
    test_cases = [
        ([[1, 2], [3, 4]], [[1, 2], [2, 3]]),
        ([[7, 7], [7, 7]], [[1, 1], [1, 1]]),
        ([[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]],
         [[4, 2, 3], [1, 3, 4], [5, 1, 6], [1, 3, 4]]),
        ([[7, 3, 6], [1, 4, 5], [9, 8, 2]], [[5, 1, 4], [1, 2, 3], [6, 3, 1]]),
    ]

    num_correct = 0
    for i, (matrix, expected) in enumerate(test_cases):
        result = matrix_rank_transform(matrix)
        if result == expected:
            print(f"Test {i + 1}: True")
            num_correct += 1
        else:
            print(f"Test {i + 1}: False")
            print(f"  Input: {matrix}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    print(f"\n{num_correct}/{len(test_cases)} correct")


if __name__ == "__main__":
    test_matrix_rank_transform()