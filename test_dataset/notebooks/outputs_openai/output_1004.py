def longestOnes(A, K):
    left = 0
    max_len = 0
    zeros = 0
    for right in range(len(A)):
        if A[right] == 0:
            zeros += 1
        while zeros > K:
            if A[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

def run_tests():
    tests = [
        {
            'A': [1,1,1,0,0,0,1,1,1,1,0],
            'K': 2,
            'expected': 6
        },
        {
            'A': [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],
            'K': 3,
            'expected': 10
        }
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        output = longestOnes(test['A'], test['K'])
        if output == test['expected']:
            print('True')
            correct += 1
        else:
            print('False')
    print(f'{correct}/{total}')

run_tests()