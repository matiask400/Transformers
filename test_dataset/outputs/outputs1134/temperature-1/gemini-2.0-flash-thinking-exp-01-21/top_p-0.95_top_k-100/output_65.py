def count_subarrays_with_sum_s(A, S):
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            current_subarray = A[i:j+1]
            current_sum = sum(current_subarray)
            if current_sum == S:
                count += 1
    return count

def run_tests():
    test_cases = [
        ([1,0,1,0,1], 2, 4),
        ([0,0,0,0,0], 0, 15),
        ([0,0,0,0,0], 1, 0),
        ([1,1,1,1,1], 3, 10),
        ([1,1,1,1,1], 0, 0),
        ([1,0,0,1,0,1], 2, 7),
        ([0,1,0,1,1,1,0,0,1,0], 3, 18),
        ([0,0,0,0,0,0,0,0,0,0], 0, 55),
        ([1,1,1,1,1,1,1,1,1,1], 10, 1),
        ([1,1,1,1,1,1,1,1,1,1], 5, 56),
        ([0], 0, 1),
        ([0], 1, 0),
        ([1], 0, 0),
        ([1], 1, 1),
        ([], 0, 0),
        ([], 1, 0),
        ([1,0], 1, 2),
        ([1,0], 2, 1),
        ([1,0], 0, 1),
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (A, S, expected_output) in enumerate(test_cases):
        actual_output = count_subarrays_with_sum_s(A, S)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)

    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    run_tests()