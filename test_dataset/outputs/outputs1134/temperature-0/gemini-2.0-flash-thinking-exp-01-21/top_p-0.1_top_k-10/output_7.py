def solve():
    def can_jump(arr, i, j, d):
        n = len(arr)
        if not (0 <= j < n):
            return False
        if not (0 < abs(i - j) <= d):
            return False
        if not (arr[i] > arr[j]):
            return False
        start = min(i, j) + 1
        end = max(i, j)
        for k in range(start, end):
            if not (arr[i] > arr[k]):
                return False
        return True

    def get_max_reachable(arr, d, start_index, memo):
        if start_index in memo:
            return memo[start_index]

        max_count = 1
        n = len(arr)

        # Jump forward
        for j in range(start_index + 1, min(start_index + d + 1, n)):
            if can_jump(arr, start_index, j, d):
                max_count = max(max_count, 1 + get_max_reachable(arr, d, j, memo))

        # Jump backward
        for j in range(max(0, start_index - d), start_index):
            if can_jump(arr, start_index, j, d):
                max_count = max(max_count, 1 + get_max_reachable(arr, d, j, memo))

        memo[start_index] = max_count
        return max_count

    def max_indices_visited(arr, d):
        n = len(arr)
        max_total_visited = 0
        for start_node in range(n):
            memo = {}
            max_total_visited = max(max_total_visited, get_max_reachable(arr, d, start_node, memo))
        return max_total_visited

    test_cases = [
        (([6,4,14,6,8,13,9,7,10,6,12], 2), 4),
        (([3,3,3,3,3], 3), 1),
        (([7,6,5,4,3,2,1], 1), 7),
        (([7,1,7,1,7,1], 2), 2),
        (([66], 1), 1),
    ]

    num_correct = 0
    for i, (input_args, expected_output) in enumerate(test_cases):
        arr, d = input_args
        actual_output = max_indices_visited(arr, d)
        if actual_output == expected_output:
            print(True)
            num_correct += 1
        else:
            print(False)

    print(f"{num_correct}/{len(test_cases)}")

solve()