def solve():
    def max_consecutive_ones(A, K):
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
        (([0,0,0], 0), 0),
        (([0,0,0], 1), 1),
        (([0,0,0], 2), 2),
        (([0,0,0], 3), 3),
        (([1,1,1], 0), 3),
        (([1,0,1], 1), 3),
        (([0,1,0], 1), 2),
        (([1,1,0,1,1,0,0,1,1,1], 2), 9),
    ]

    correct_count = 0
    for i, (input_args, expected_output) in enumerate(test_cases):
        A, K = input_args
        actual_output = max_consecutive_ones(A, K)
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)
            print(f"Test case {i+1} failed: Input={input_args}, Expected={expected_output}, Actual={actual_output}")

    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    solve()