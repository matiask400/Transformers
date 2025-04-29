def count_prime_set_bits(L, R):
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    count = 0
    for num in range(L, R + 1):
        set_bits = bin(num).count('1')
        if set_bits in primes:
            count += 1
    return count

def run_tests():
    test_cases = [
        {'L': 6, 'R': 10, 'expected': 4},
        {'L': 10, 'R': 15, 'expected': 5},
        # You can add more test cases here
    ]
    
    correct = 0
    total = len(test_cases)
    
    for test in test_cases:
        result = count_prime_set_bits(test['L'], test['R'])
        if result == test['expected']:
            print('True')
            correct += 1
        else:
            print('False')
    
    print(f"{correct} / {total}")

run_tests()