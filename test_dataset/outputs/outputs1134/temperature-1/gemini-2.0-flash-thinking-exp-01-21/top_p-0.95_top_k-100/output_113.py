class SparseVector:
    def __init__(self, nums):
        self.sparse_vector = {}
        for index, num in enumerate(nums):
            if num != 0:
                self.sparse_vector[index] = num

    def dotProduct(self, vec):
        dot_product_result = 0
        for index, value in self.sparse_vector.items():
            if index in vec.sparse_vector:
                dot_product_result += value * vec.sparse_vector[index]
        return dot_product_result

def test_sparse_vector_dot_product():
    test_cases = [
        (([1,0,0,2,3], [0,3,0,4,0]), 8),
        (([0,1,0,0,0], [0,0,0,0,2]), 0),
        (([0,1,0,0,2,0,0], [1,0,0,0,3,0,4]), 6),
        (([0,0,0], [0,0,0]), 0),
        (([1,2,3], [4,5,6]), 32),
        (([1,0,0], [1,0,0]), 1),
        (([0,1,0], [0,1,0]), 1),
        (([0,0,1], [0,0,1]), 1),
        (([1,0,1], [0,1,0]), 0),
        (([1,2,0,0,3], [0,0,4,5,0]), 0)
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (inputs, expected_output) in enumerate(test_cases):
        nums1, nums2 = inputs
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        actual_output = v1.dotProduct(v2)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)
        # print(f"Test {i+1}: Input={inputs}, Expected={expected_output}, Actual={actual_output}, Result={'True' if actual_output == expected_output else 'False'}")

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_sparse_vector_dot_product()