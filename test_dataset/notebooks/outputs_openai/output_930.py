def num_subarrays_with_sum_S(A, S):
    from collections import defaultdict
    count = 0
    current_sum = 0
    sums = defaultdict(int)
    sums[0] = 1
    for num in A:
        current_sum += num
        if (current_sum - S) in sums:
            count += sums[current_sum - S]
        sums[current_sum] += 1
    return count

def run_tests():
    tests = [
        {'A': [1,0,1,0,1], 'S': 2, 'expected': 4},
        {'A': [0,0,0,0,0], 'S': 0, 'expected': 15},
        {'A': [1,1,1], 'S': 2, 'expected': 2},
        {'A': [1,0,1,0,1], 'S': 3, 'expected': 2},
        {'A': [], 'S': 0, 'expected': 0},
        {'A': [1], 'S': 1, 'expected': 1},
        {'A': [0], 'S': 0, 'expected': 1},
        {'A': [1,0,0,1,0,1], 'S': 2, 'expected': 4},
        {'A': [1,1,1,1], 'S': 3, 'expected': 2},
        {'A': [0,1,0,1,0,1,0], 'S': 2, 'expected': 6},
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        output = num_subarrays_with_sum_S(test['A'], test['S'])
        if output == test['expected']:
            print("True")
            correct +=1
        else:
            print("False")
    print(f"{correct} / {total}")

run_tests()