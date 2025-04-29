class SparseVector:
    def __init__(self, nums):
        self.sparse_representation = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.sparse_representation[i] = num

    def dotProduct(self, vec):
        dot_product = 0
        for index, value in self.sparse_representation.items():
            if index in vec.sparse_representation:
                dot_product += value * vec.sparse_representation[index]
        return dot_product

def test_sparse_vector():
    test_cases = [
        (([1, 0, 0, 2, 3], [0, 3, 0, 4, 0]), 8),
        (([0, 1, 0, 0, 0], [0, 0, 0, 0, 2]), 0),
        (([0, 1, 0, 0, 2, 0, 0], [1, 0, 0, 0, 3, 0, 4]), 6),
        (([1, 2, 3], [4, 5, 6]), 32),
        (([0, 0, 0], [0, 0, 0]), 0),
        (([1, 0, 0], [0, 1, 0]), 0),
        (([0, 1, 0], [0, 1, 0]), 1),
        (([100, 0, 100], [0, 100, 0]), 0),
        (([100, 0, 100], [1, 0, 1]), 200),
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_vectors, expected_output) in enumerate(test_cases):
        nums1, nums2 = input_vectors
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        actual_output = v1.dotProduct(v2)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)
            print(f"Test case {i+1} failed: Input={input_vectors}, Expected={expected_output}, Actual={actual_output}")

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_sparse_vector()