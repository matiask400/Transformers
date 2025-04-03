def maximize_advantage(A, B):
    sorted_A = sorted(A)
    sorted_B = sorted([(b, i) for i, b in enumerate(B)], reverse=True)
    result = [0] * len(A)
    left, right = 0, len(A) -1
    for b, i in sorted_B:
        if sorted_A[right] > b:
            result[i] = sorted_A[right]
            right -=1
        else:
            result[i] = sorted_A[left]
            left +=1
    return result

def run_tests():
    tests = [
        {
            'A': [2,7,11,15],
            'B': [1,10,4,11],
            'expected': [2,11,7,15]
        },
        {
            'A': [12,24,8,32],
            'B': [13,25,32,11],
            'expected': [24,32,8,12]
        }
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        output = maximize_advantage(test['A'], test['B'])
        if output == test['expected']:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct} / {total}")

run_tests()