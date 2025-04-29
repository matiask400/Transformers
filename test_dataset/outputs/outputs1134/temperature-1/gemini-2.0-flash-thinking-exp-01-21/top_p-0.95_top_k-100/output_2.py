def smallest_length_n_divisible_by_k(k):
    if k == 1:
        return 1
    if k % 2 == 0 or k % 5 == 0:
        return -1
    remainder = 0
    for length in range(1, k + 1):
        remainder = (remainder * 10 + 1) % k
        if remainder == 0:
            return length
    return -1

def run_tests():
    tests = [
        (1, 1),
        (2, -1),
        (3, 3),
        (7, 6),
        (9, 9),
        (11, 2),
        (37, 3),
        (99, 18),
        (999, 27),
        (1000, -1),
        (10000, -1),
        (12345, -1),
        (123, -1),
        (12347, 12346),
        (17, 16),
        (19, 18),
        (23, 22),
        (13, 6),
        (101, 4),
        (103, 34),
        (107, 53),
        (109, 36),
        (100000, -1),
        (99999, 9),
        (99991, 99990)
    ]
    correct_count = 0
    for input_k, expected_output in tests:
        actual_output = smallest_length_n_divisible_by_k(input_k)
        if actual_output == expected_output:
            print('True')
            correct_count += 1
        else:
            print('False')
    print(f"{correct_count}/{len(tests)}")

if __name__ == '__main__':
    run_tests()