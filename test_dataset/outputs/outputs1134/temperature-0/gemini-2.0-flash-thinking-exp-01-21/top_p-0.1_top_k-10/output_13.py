def advantage_count(A, B):
    n = len(A)
    sorted_A = sorted(A)
    sorted_B_indices = sorted([(B[i], i) for i in range(n)])
    res = [0] * n
    remaining_A = list(sorted_A)

    for b_val, b_idx in sorted_B_indices:
        found_greater = False
        for i in range(len(remaining_A)):
            if remaining_A[i] > b_val:
                res[b_idx] = remaining_A.pop(i)
                found_greater = True
                break
        if not found_greater:
            res[b_idx] = remaining_A.pop(0)
    return res

def test_advantage_count():
    test_cases = [
        (([2,7,11,15], [1,10,4,11]), [2,11,7,15]),
        (([12,24,8,32], [13,25,32,11]), [24,32,8,12]),
        (([0,0,0,0], [0,0,0,0]), [0,0,0,0]),
        (([1,2,3,4], [4,3,2,1]), [2,3,4,1]),
        (([4,3,2,1], [1,2,3,4]), [2,1,4,3]),
        (([5,6,7,8], [1,2,3,4]), [5,6,7,8]),
        (([1,2,3,4], [5,6,7,8]), [1,2,3,4]),
    ]

    num_correct = 0
    for i, (input_args, expected_output) in enumerate(test_cases):
        A, B = input_args
        actual_output = advantage_count(A, B)
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            num_correct += 1
        else:
            print(f'Test {i+1}: False')
            print(f'  Input: A={A}, B={B}')
            print(f'  Expected: {expected_output}')
            print(f'  Actual:   {actual_output}')

    print(f'Correct tests: {num_correct}/{len(test_cases)}')

if __name__ == '__main__':
    test_advantage_count()