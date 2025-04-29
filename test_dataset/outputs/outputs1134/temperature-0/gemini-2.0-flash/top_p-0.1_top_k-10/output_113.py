class SparseVector:
    def __init__(self, nums):
        self.nums = nums
        self.sparse_vector = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.sparse_vector[i] = num

    def dotProduct(self, vec):
        result = 0
        for i, num in enumerate(vec.nums):
            if num != 0 and i in self.sparse_vector:
                result += self.sparse_vector[i] * num
        return result

def test_sparse_vector():
    test_cases = [
        (([1,0,0,2,3], [0,3,0,4,0]), 8),
        (([0,1,0,0,0], [0,0,0,0,2]), 0),
        (([0,1,0,0,2,0,0], [1,0,0,0,3,0,4]), 6),
        (([1,2,3], [4,5,6]), 32),
        (([0,0,0], [0,0,0]), 0),
        (([1,0,0], [0,1,0]), 0),
        (([0,0,1], [0,0,1]), 1),
        (([1,0,1], [1,0,1]), 2),
        (([1,1,1], [1,1,1]), 3),
        (([1,0,0,0,0], [0,0,0,0,1]), 0)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for (nums1, nums2), expected in test_cases:
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        actual = v1.dotProduct(v2)
        if actual == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: nums1={nums1}, nums2={nums2}")
            print(f"Expected: {expected}, Actual: {actual}")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_sparse_vector()