def max_generated(n):
    if n == 0:
        return 0
    nums = [0] * (n + 1)
    nums[0] = 0
    if n >=1:
        nums[1] = 1
    for i in range(1, (n//2)+1):
        if 2 * i <= n:
            nums[2 * i] = nums[i]
        if 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]
    return max(nums)

def run_tests():
    tests = [
        {'input': 7, 'output': 3},
        {'input': 2, 'output': 1},
        {'input': 3, 'output': 2},
        {'input': 0, 'output': 0},
        {'input': 1, 'output': 1},
        {'input': 4, 'output': 2},
        {'input': 5, 'output': 3},
        {'input': 6, 'output': 3},
        {'input': 8, 'output': 3},
        {'input': 9, 'output': 3},
        {'input': 10, 'output': 3},
        {'input': 100, 'output': 7},
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        actual = max_generated(test['input'])
        expected = test['output']
        if actual == expected:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()