def solve():
    def subarray_ranges_sum(nums, n, left, right):
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        subarray_sums.sort()
        result_sum = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            result_sum = (result_sum + subarray_sums[i]) % mod
        return result_sum

    def run_test(nums, n, left, right, expected_output):
        output = subarray_ranges_sum(nums, n, left, right)
        if output == expected_output:
            print("True")
        else:
            print("False")
        return output == expected_output

    test_cases = [
        (([1, 2, 3, 4], 4, 1, 5), 13),
        (([1, 2, 3, 4], 4, 3, 4), 6),
        (([1, 2, 3, 4], 4, 1, 10), 50),
        (([1, 1, 1], 3, 1, 5), 8),
        (([1, 1, 1], 3, 1, 6), 10),
        (([1, 1, 1], 3, 3, 5), 5),
        (([1, 1, 1], 3, 2, 4), 5),
        (([1, 2], 2, 1, 3), 4),
        (([1, 2], 2, 2, 3), 3),
        (([100, 10, 1], 3, 1, 6), 156),
    ]

    correct_count = 0
    for test_case, expected in test_cases:
        nums, n, left, right = test_case
        if run_test(nums, n, left, right, expected):
            correct_count += 1

    print(f"{correct_count}/{len(test_cases)}")

solve()