def smallest_length_n_divisible_by_k(k: int) -> int:
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
        (4, -1),
        (5, -1),
        (6, -1),
        (7, 6),
        (8, -1),
        (9, 9),
        (10, -1),
        (11, 2),
        (13, 6),
        (17, 16),
        (19, 18),
        (23, 22),
        (37, 3),
        (100000, -1),
        (99991, 99990)
    ]
    num_correct = 0
    for i, (k, expected_output) in enumerate(tests):
        actual_output = smallest_length_n_divisible_by_k(k)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{num_correct}/{len(tests)}")

if __name__ == '__main__':
    run_tests()