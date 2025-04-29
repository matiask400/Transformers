def subarrays_divisible_by_k(A, K):
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            subarray = A[i:j+1]
            subarray_sum = sum(subarray)
            if subarray_sum % K == 0:
                count += 1
    return count

def test_subarrays_divisible_by_k():
    test_cases = [
        (([4,5,0,-2,-3,1], 5), 7),
        (([5], 5), 1),
        (([5, 5], 5), 3),
        (([1, 2, 3, 4, 5], 5), 2),
        (([-5, -5], 5), 3),
        (([0, 0, 0], 5), 6),
        (([1, -1], 5), 1),
    ]
    correct_count = 0
    total_count = len(test_cases)
    for i, (input_args, expected_output) in enumerate(test_cases):
        A, K = input_args
        actual_output = subarrays_divisible_by_k(A, K)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_count}/{total_count}")

if __name__ == '__main__':
    test_subarrays_divisible_by_k()