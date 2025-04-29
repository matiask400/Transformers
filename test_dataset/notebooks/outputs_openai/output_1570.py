class SparseVector:
    def __init__(self, nums):
        self.dict = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.dict[i] = num

    def dotProduct(self, vec):
        result = 0
        # Iterate over the smaller dictionary for efficiency
        if len(self.dict) < len(vec.dict):
            for i in self.dict:
                if i in vec.dict:
                    result += self.dict[i] * vec.dict[i]
        else:
            for i in vec.dict:
                if i in self.dict:
                    result += self.dict[i] * vec.dict[i]
        return result

def run_tests():
    tests = [
        {
            'nums1': [1, 0, 0, 2, 3],
            'nums2': [0, 3, 0, 4, 0],
            'expected': 8
        },
        {
            'nums1': [0, 1, 0, 0, 0],
            'nums2': [0, 0, 0, 0, 2],
            'expected': 0
        },
        {
            'nums1': [0, 1, 0, 0, 2, 0, 0],
            'nums2': [1, 0, 0, 0, 3, 0, 4],
            'expected': 6
        },
    ]

    correct = 0
    total = len(tests)
    for test in tests:
        v1 = SparseVector(test['nums1'])
        v2 = SparseVector(test['nums2'])
        output = v1.dotProduct(v2)
        if output == test['expected']:
            print('True')
            correct += 1
        else:
            print('False')
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()