def count_subarrays_with_sum_s(A, S):
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            subarray = A[i:j+1]
            if sum(subarray) == S:
                count += 1
    return count

def test_count_subarrays_with_sum_s():
    test_cases = [
        ([1,0,1,0,1], 2, 4),
        ([0,0,0], 0, 6),
        ([0,0,0], 1, 0),
        ([1,1,1], 2, 3),
        ([1,1,1], 3, 1),
        ([1,0,0,1,0], 1, 6),
        ([1,0,0,1,0], 2, 1),
        ([1,0,0,1,0], 0, 4),
        ([], 0, 0),
        ([1], 1, 1),
        ([1], 0, 0),
        ([0], 0, 1),
        ([0], 1, 0),
    ]
    correct_tests = 0
    total_tests = len(test_cases)
    for A, S, expected_output in test_cases:
        actual_output = count_subarrays_with_sum_s(A, S)
        if actual_output == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')
    print(f'{correct_tests}/{total_tests}')

if __name__ == '__main__':
    test_count_subarrays_with_sum_s()