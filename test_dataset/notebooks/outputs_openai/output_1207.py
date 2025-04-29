def uniqueOccurrences(arr):
    from collections import Counter
    counts = Counter(arr).values()
    return len(counts) == len(set(counts))

def run_tests():
    test_cases = [
        {'input': [1,2,2,1,1,3], 'expected': True},
        {'input': [1,2], 'expected': False},
        {'input': [-3,0,1,-3,1,1,1,-3,10,0], 'expected': True},
        {'input': [1,1,2,2,2,3], 'expected': True},
        {'input': [1], 'expected': True},
        {'input': [1,1,1,1,1], 'expected': True},
        {'input': [1,2,3,4,5,6,7,8,9,10], 'expected': True},
        {'input': [1,1,2,2,3,3], 'expected': False},
    ]
    
    correct = 0
    total = len(test_cases)
    
    for test in test_cases:
        result = uniqueOccurrences(test['input'])
        if result == test['expected']:
            print(True)
            correct += 1
        else:
            print(False)
    
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()