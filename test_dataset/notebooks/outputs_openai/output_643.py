def max_average_subarray(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum / k

def run_tests():
    tests = [
        {
            'input': {
                'nums': [1, 12, -5, -6, 50, 3],
                'k': 4
            },
            'expected': 12.75
        },
        {
            'input': {
                'nums': [5],
                'k': 1
            },
            'expected': 5.0
        },
        {
            'input': {
                'nums': [0, 0, 0, 0],
                'k': 2
            },
            'expected': 0.0
        },
        {
            'input': {
                'nums': [-1, -12, -5, -6, -50, -3],
                'k': 4
            },
            'expected': -17.0
        },
        {
            'input': {
                'nums': [1, 2, 3, 4, 5],
                'k': 2
            },
            'expected': 4.5
        },
        {
            'input': {
                'nums': [4, 4, 4, 4],
                'k': 4
            },
            'expected': 4.0
        },
        {
            'input': {
                'nums': [1, -1, 1, -1, 1, -1, 1],
                'k': 3
            },
            'expected': 0.3333333333333333
        },
        {
            'input': {
                'nums': [7, 4, -1, 8, -15, 3, 16, 12],
                'k': 3
            },
            'expected': 10.333333333333334
        },
        {
            'input': {
                'nums': [10, 20, 30, 40, 50],
                'k': 5
            },
            'expected': 30.0
        },
        {
            'input': {
                'nums': [1, 12, -5, -6, 50, 3, 4, -2],
                'k': 4
            },
            'expected': 12.75
        }
    ]

    correct = 0
    total = len(tests)
    for test in tests:
        nums = test['input']['nums']
        k = test['input']['k']
        expected = test['expected']
        result = max_average_subarray(nums, k)
        # To handle floating point precision, use a tolerance
        if abs(result - expected) < 1e-6:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()