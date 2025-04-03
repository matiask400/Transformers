from collections import defaultdict

def numSubarraysDivByK(A, K):
    count = defaultdict(int)
    count[0] = 1
    total = 0
    prefix = 0
    for num in A:
        prefix = (prefix + num) % K
        total += count[prefix]
        count[prefix] += 1
    return total

def run_tests():
    tests = [
        {
            'A': [4,5,0,-2,-3,1],
            'K': 5,
            'expected': 7
        },
        {
            'A': [5],
            'K': 9,
            'expected': 0
        },
        {
            'A': [1,2,3,4,5],
            'K': 3,
            'expected': 4
        },
        {
            'A': [0,0,0,0,0],
            'K': 1,
            'expected': 15
        },
        {
            'A': [-1,2,9],
            'K': 2,
            'expected': 2
        },
        {
            'A': [7, -5, -7, 19, 1, -1, 4],
            'K': 3,
            'expected': 5
        }
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        output = numSubarraysDivByK(test['A'], test['K'])
        if output == test['expected']:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()