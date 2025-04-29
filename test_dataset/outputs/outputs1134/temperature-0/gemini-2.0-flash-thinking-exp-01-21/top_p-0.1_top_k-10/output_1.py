def count_set_bits(n):
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count

def is_prime(n):
    if n <= 1:
        return False
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # Precomputed primes up to 31, more than enough for set bits of 10^6
    return n in primes

def solve(L, R):
    count = 0
    for i in range(L, R + 1):
        set_bits = count_set_bits(i)
        if is_prime(set_bits):
            count += 1
    return count

def run_tests():
    test_cases = [
        {"input": {"L": 6, "R": 10}, "expected": 4},
        {"input": {"L": 10, "R": 15}, "expected": 5},
        {"input": {"L": 1, "R": 5}, "expected": 2},
        {"input": {"L": 1, "R": 1}, "expected": 0},
        {"input": {"L": 2, "R": 2}, "expected": 0},
        {"input": {"L": 3, "R": 3}, "expected": 1},
        {"input": {"L": 4, "R": 4}, "expected": 0},
        {"input": {"L": 5, "R": 5}, "expected": 1},
        {"input": {"L": 1, "R": 100}, "expected": 25},
        {"input": {"L": 100, "R": 200}, "expected": 24},
        {"input": {"L": 1000, "R": 1100}, "expected": 27},
        {"input": {"L": 999900, "R": 1000000}, "expected": 25}
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        actual_output = solve(test_case["input"]["L"], test_case["input"]["R"])
        expected_output = test_case["expected"]
        if actual_output == expected_output:
            print(True)
            num_correct += 1
        else:
            print(False)
        # print(f"Test case {i+1}: Input={test_case['input']}, Expected={expected_output}, Actual={actual_output}")

    print(f"{num_correct}/{len(test_cases)}")

if __name__ == "__main__":
    run_tests()