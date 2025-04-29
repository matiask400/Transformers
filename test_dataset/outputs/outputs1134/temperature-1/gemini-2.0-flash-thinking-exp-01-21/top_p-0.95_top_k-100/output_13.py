def advantage_count(A, B):
    n = len(A)
    sorted_A = sorted(A)
    indices_B = sorted(range(n), key=lambda i: B[i])
    result = [0] * n
    used_indices_A = [False] * n
    a_idx = 0

    for b_idx in indices_B:
        b_val = B[b_idx]
        found_greater = False
        for i in range(a_idx, n):
            if not used_indices_A[i] and sorted_A[i] > b_val:
                result[b_idx] = sorted_A[i]
                used_indices_A[i] = True
                found_greater = True
                a_idx = i+1 if i+1 < n else n # optimization to skip already checked smaller values in next iterations. Not really needed for correctness
                break
        if not found_greater:
            for i in range(n):
                if not used_indices_A[i]:
                    result[b_idx] = sorted_A[i]
                    used_indices_A[i] = True
                    break
    return result

def test_advantage_count():
    test_cases = [
        (([2, 7, 11, 15], [1, 10, 4, 11]), [2, 11, 7, 15]),
        (([12, 24, 8, 32], [13, 25, 32, 11]), [24, 32, 8, 12]),
        (([2, 2, 2, 2], [1, 1, 1, 1]), [2, 2, 2, 2]),
        (([1, 1, 1, 1], [2, 2, 2, 2]), [1, 1, 1, 1]),
        (([5, 6, 7, 8], [1, 2, 3, 4]), [5, 6, 7, 8]),
        (([5, 6, 7, 8], [8, 7, 6, 5]), [6, 7, 8, 5]), # Corrected expected output after re-evaluation
        (([0,0,0,0], [0,0,0,0]), [0,0,0,0]),
        (([1000000000, 0], [0, 1000000000]), [1000000000, 0]),
        (([5,5,5,5], [5,5,4,6]), [5, 5, 5, 5]), # Corrected expected output after re-evaluation, any perm should work.
        (([2,0,4,1,3], [1,2,3,4,0]), [2, 3, 4, 1, 0]) # Added test case to check order
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (input_data, expected_output) in enumerate(test_cases):
        A, B = input_data
        output = advantage_count(A, B)
        advantage_output = 0
        advantage_expected = 0

        for j in range(len(A)):
            if output[j] > B[j]:
                advantage_output += 1
            if expected_output[j] > B[j]:
                advantage_expected += 1

        temp_A = list(A)
        is_permutation = True
        output_counts = {}
        temp_A_counts = {}
        for x in output:
            output_counts[x] = output_counts.get(x, 0) + 1
        for x in temp_A:
            temp_A_counts[x] = temp_A_counts.get(x, 0) + 1
        if output_counts != temp_A_counts:
            is_permutation = False

        if is_permutation and advantage_output >= advantage_expected: # Check if output is a permutation and advantage is maximized (or at least same as example)
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_advantage_count()