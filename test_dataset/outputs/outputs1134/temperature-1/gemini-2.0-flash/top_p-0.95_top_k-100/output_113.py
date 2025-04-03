class SparseVector:
    def __init__(self, nums):
        self.nums = nums
        self.sparse_vector = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.sparse_vector[i] = num

    def dotProduct(self, vec):
        result = 0
        if isinstance(vec, SparseVector):
            for i, num in self.sparse_vector.items():
                if i in vec.sparse_vector:
                    result += num * vec.sparse_vector[i]
        else:
            for i, num in self.sparse_vector.items():
                if i < len(vec):
                    result += num * vec[i]
        return result

def test_sparse_vector():
    tests = [
        {
            "nums1": [1, 0, 0, 2, 3],
            "nums2": [0, 3, 0, 4, 0],
            "expected": 8,
        },
        {
            "nums1": [0, 1, 0, 0, 0],
            "nums2": [0, 0, 0, 0, 2],
            "expected": 0,
        },
        {
            "nums1": [0, 1, 0, 0, 2, 0, 0],
            "nums2": [1, 0, 0, 0, 3, 0, 4],
            "expected": 6,
        },
        {
            "nums1": [1,2,3],
            "nums2": [4,5,6],
            "expected": 32
        },
        {
            "nums1": [0,0,0],
            "nums2": [1,2,3],
            "expected": 0
        },
        {
            "nums1": [1,0,0],
            "nums2": [0,0,1],
            "expected": 0
        },

    ]

    correct_count = 0
    total_tests = len(tests)

    for i, test in enumerate(tests):
        nums1 = test["nums1"]
        nums2 = test["nums2"]
        expected = test["expected"]

        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        actual = v1.dotProduct(v2)

        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: nums1={nums1}, nums2={nums2}")
            print(f"  Expected: {expected}, Actual: {actual}")

    print(f"\nCorrect tests: {correct_count}/{total_tests}")


if __name__ == "__main__":
    test_sparse_vector()