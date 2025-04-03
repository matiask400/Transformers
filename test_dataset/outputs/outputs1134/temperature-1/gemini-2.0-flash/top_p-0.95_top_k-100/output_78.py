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
        return find(parent, parent[i])

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

    n = len(A)
    parent = list(range(n))
    size = [1] * n

    def get_factors(num):
        factors = set()
        d = 2
        while d * d <= num:
            if num % d == 0:
                factors.add(d)
                while num % d == 0:
                    num //= d
            d += 1
        if num > 1:
            factors.add(num)
        return factors

    num_to_index = {}
    for i, num in enumerate(A):
        factors = get_factors(num)
        for factor in factors:
            if factor in num_to_index:
                union(parent, size, i, num_to_index[factor])
            else:
                num_to_index[factor] = i

    max_size = 0
    for i in range(n):
        max_size = max(max_size, size[find(parent, i)])

    return max_size


def test_largest_component_size():
    test_cases = [
        ([4, 6, 15, 35], 4),
        ([20, 50, 9, 63], 2),
        ([2, 3, 6, 7, 4, 12, 21, 39], 8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6),
        ([71,83,53,47,73,61,79,43,7,59,67,23,31,29], 1),
        ([4,6,15], 3),
        ([10, 20, 30, 40, 50], 5),
        ([2, 4, 6, 8, 10], 5),
        ([3, 6, 9, 12, 15], 5)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (input_arr, expected_output) in enumerate(test_cases):
        actual_output = largest_component_size(input_arr)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {input_arr}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"\nCorrect: {correct_count}/{total_count}")


if __name__ == "__main__":
    test_largest_component_size()