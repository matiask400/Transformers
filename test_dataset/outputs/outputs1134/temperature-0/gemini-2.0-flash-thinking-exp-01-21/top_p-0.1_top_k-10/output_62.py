def solve():
    def longest_subarray_with_ones_after_flip(A, K):
        left = 0
        zero_count = 0
        max_length = 0
        for right in range(len(A)):
            if A[right] == 0:
                zero_count += 1
            while zero_count > K:
                if A[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

    test_cases = [
        (([1,1,1,0,0,0,1,1,1,1,0], 2), 6),
        (([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10),
        (([1,1,1], 0), 3),
        (([0,0,0], 0), 0),
        (([0,0,0], 1), 1),
        (([0,0,0], 2), 2),
        (([0,0,0], 3), 3),
        (([1,0,0,1,0,1,0,1,1,1,1,0,0,0], 2), 8),
        (([0,0,0,1,1,1,0,0,1,1,1,1,1,0,0], 3), 10),
        (([0,0,0,1,1,1,0,0,1,1,1,1,1,0,0], 0), 5),
        (([1,0,0,1,0,1,0,1,1,1,1,0,0,0], 0), 4),
        (([0], 1), 1),
        (([0], 0), 0),
        (([1], 0), 1),
        (([1], 1), 1),
        (([0,1], 1), 2),
        (([0,1], 0), 1),
        (([1,0], 1), 2),
        (([1,0], 0), 1),
    ]

    correct_count = 0
    for i, ((A, K), expected_output) in enumerate(test_cases):
        result = longest_subarray_with_ones_after_flip(A, K)
        if result == expected_output:
            print(f'Test {i+1}: True')
            correct_count += 1
        else:
            print(f'Test {i+1}: False')

    print(f'{correct_count}/{len(test_cases)}')

solve()