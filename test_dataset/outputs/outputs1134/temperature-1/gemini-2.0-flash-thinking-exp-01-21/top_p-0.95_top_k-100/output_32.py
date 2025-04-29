def count_subarrays_divisible_by_k(A, K):
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            sub_array = A[i:j+1]
            sub_array_sum = sum(sub_array)
            if sub_array_sum % K == 0:
                count += 1
    return count

def run_tests():
    test_cases = [
        (([4, 5, 0, -2, -3, 1], 5), 7),
        (([5], 5), 1),
        (([0], 5), 1),
        (([-5], 5), 1),
        (([5, 5], 5), 3),
        (([1, 2, 3, 4, 5], 5), 3),
        (([1, 2, 3, 4], 5), 0),
        (([2, 2, 2, 2, 2], 2), 15),
        (([1, 2, 3, 4, 5, 6], 3), 6),
        (([-1, -2, -3, -4, -5], 3), 5),
        (([1, -2, 3, -4, 5], 3), 2),
        (([1, -2, 3, -4, 5], 2), 6),
        (([0, 0, 0, 0, 0], 5), 15),
    ]

    correct_count = 0
    for i, (input_args, expected_output) in enumerate(test_cases):
        A, K = input_args
        actual_output = count_subarrays_divisible_by_k(A, K)
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)
            print(f"Test {i+1} failed: Input={input_args}, Expected={expected_output}, Actual={actual_output}")

    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()