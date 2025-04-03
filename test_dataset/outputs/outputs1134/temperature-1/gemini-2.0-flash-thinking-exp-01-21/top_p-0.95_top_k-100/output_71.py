import collections

def can_reorder(arr):
    counts = collections.Counter(arr)
    unique_keys = sorted(counts.keys(), key=abs)
    for x in unique_keys:
        while counts[x] > 0:
            target = 2 * x
            if counts[target] > 0:
                counts[x] -= 1
                counts[target] -= 1
            else:
                return False
    return True

def run_tests():
    tests = [
        ([3, 1, 3, 6], False),
        ([2, 1, 2, 6], False),
        ([4, -2, 2, -4], True),
        ([1, 2, 4, 16, 8, 4], False),
        ([0, 0], True),
        ([0, 0, 0, 0], True),
        ([5, 10, 2, 4], True),
        ([1, 2, 4, 8], True),
        ([1, 2, 4, 4], False),
        ([-2,-4], True),
        ([-2, -4, 2, 4], True),
        ([6, 3], True),
        ([6, 3, 6, 3], True),
        ([6, 3, 6, 4], False),
        ([-1,-2], True),
        ([-1, -2, 1, 2], True),
        ([-1, -2, 1, 3], False),
        ([], True)
    ]
    correct_count = 0
    for i, (arr, expected_output) in enumerate(tests):
        result = can_reorder(arr)
        if result == expected_output:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False')
    print(f'{correct_count}/{len(tests)}')

if __name__ == '__main__':
    run_tests()