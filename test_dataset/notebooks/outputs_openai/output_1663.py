def smallestString(n, k):
    res = ['a'] * n
    extra = k - n
    i = n - 1
    while extra > 0 and i >= 0:
        add = min(extra, 25)
        res[i] = chr(ord('a') + add)
        extra -= add
        i -= 1
    return ''.join(res)

def run_tests():
    tests = [
        {'n': 3, 'k': 27, 'expected': 'aay'},
        {'n': 5, 'k': 73, 'expected': 'aaszz'},
        {'n': 1, 'k': 1, 'expected': 'a'},
        {'n': 2, 'k': 52, 'expected': 'az'},
        {'n': 4, 'k': 100, 'expected': 'aazz'},
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        output = smallestString(test['n'], test['k'])
        result = output == test['expected']
        print(result)
        if result:
            correct += 1
    print(f"{correct}/{total}")

run_tests()