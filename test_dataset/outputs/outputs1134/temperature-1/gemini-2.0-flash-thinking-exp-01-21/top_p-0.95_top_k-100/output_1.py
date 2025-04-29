def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_set_bits(n):
    return bin(n).count('1')

def count_numbers_with_prime_set_bits(L, R):
    count = 0
    for i in range(L, R + 1):
        set_bits = count_set_bits(i)
        if is_prime(set_bits):
            count += 1
    return count

def run_tests():
    test_cases = [
        ((6, 10), 4),
        ((10, 15), 5),
        ((1, 5), 2),
        ((1, 1), 0),
        ((2, 2), 0),
        ((2, 3), 1),
        ((1, 10), 4),
        ((1, 20), 6),
        ((1, 30), 8),
        ((990, 1000), 3),
        ((1, 1000000), 167370) # Added a larger test case
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_val, expected_output) in enumerate(test_cases):
        L, R = input_val
        actual_output = count_numbers_with_prime_set_bits(L, R)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()