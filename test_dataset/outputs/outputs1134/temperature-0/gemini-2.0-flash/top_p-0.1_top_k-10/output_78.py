def largest_component_size(A):
    """
    Given a non-empty array of unique positive integers `A`, consider the following graph:
    There are `A.length` nodes, labelled `A[0]` to `A[A.length - 1];`
    There is an edge between `A[i]` and `A[j]` if and only if `A[i]` and `A[j]` share a common factor greater than 1.

    Return the size of the largest connected component in the graph.
    """

    def find(parent, i):
        if parent[i] == i:
            return i
        parent[i] = find(parent, parent[i])
        return parent[i]

    def union(parent, size, i, j):
        root_i = find(parent, i)
        root_j = find(parent, j)
        if root_i != root_j:
            if size[root_i] < size[root_j]:
                parent[root_i] = root_j
                size[root_j] += size[root_i]
            else:
                parent[root_j] = root_i
                size[root_i] += size[root_j]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    n = len(A)
    parent = list(range(n))
    size = [1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if gcd(A[i], A[j]) > 1:
                union(parent, size, i, j)

    max_size = 0
    for i in range(n):
        if parent[i] == i:
            max_size = max(max_size, size[i])
    
    counts = {}
    for i in range(n):
        root = find(parent, i)
        if root not in counts:
            counts[root] = 0
        counts[root] += 1
    
    return max(counts.values()) if counts else 0

def test_largest_component_size():
    test_cases = [
        ([4, 6, 15, 35], 4),
        ([20, 50, 9, 63], 2),
        ([2, 3, 6, 7, 4, 12, 21, 39], 8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 12),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], 14),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 16),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], 18),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], 20),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], 22),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], 24),
    ]

    num_correct = 0
    for input_array, expected_output in test_cases:
        actual_output = largest_component_size(input_array)
        if actual_output == expected_output:
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Input: {input_array}")
            print(f"Expected: {expected_output}")
            print(f"Actual: {actual_output}")

    print(f"{num_correct}/{len(test_cases)}")

if __name__ == "__main__":
    test_largest_component_size()