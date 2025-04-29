def solve():
    def get_subarray_sums(nums):
        subarray_sums = []
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        return subarray_sums

    def calculate_sum_range(nums, left, right):
        subarray_sums = get_subarray_sums(nums)
        subarray_sums.sort()
        total_sum = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            total_sum = (total_sum + subarray_sums[i]) % mod
        return total_sum

    test_cases = [
        (([1, 2, 3, 4], 4, 1, 5), 13),
        (([1, 2, 3, 4], 4, 3, 4), 6),
        (([1, 2, 3, 4], 4, 1, 10), 50),
        (([1, 1, 1], 3, 1, 6), 13),
        (([1, 1, 1], 3, 1, 1), 1),
        (([1, 1, 1], 3, 6, 6), 3),
        (([1, 1, 1], 3, 3, 4), 2),
        (([1, 1, 1], 3, 2, 5), 5),
        (([1, 2], 2, 1, 3), 4),
        (([1, 2], 2, 2, 3), 3),
        (([1, 2], 2, 1, 1), 1),
        (([1, 2], 2, 3, 3), 2),
        (([100, 10, 1], 3, 1, 6), 164),
        (([100, 10, 1], 3, 1, 1), 1),
        (([100, 10, 1], 3, 6, 6), 111),
        (([100, 10, 1], 3, 3, 4), 11),
        (([100, 10, 1], 3, 2, 5), 121),
    ]

    num_correct = 0
    for i, (input_args, expected_output) in enumerate(test_cases):
        nums, n, left, right = input_args
        actual_output = calculate_sum_range(nums, left, right)
        if actual_output == expected_output:
            print(True)
            num_correct += 1
        else:
            print(False)
    print(f"{num_correct}/{len(test_cases)}")

solve()