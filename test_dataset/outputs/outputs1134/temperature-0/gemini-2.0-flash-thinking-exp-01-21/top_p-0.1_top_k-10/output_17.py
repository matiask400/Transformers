def solve():
    def get_max_generated_array(n):
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        for i in range(1, n + 1):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums)

    def run_tests():
        test_cases = [
            (7, 3),
            (2, 1),
            (3, 2),
            (0, 0),
            (1, 1),
            (4, 2),
            (5, 3),
            (6, 3),
            (8, 3),
            (9, 4),
            (10, 5),
            (15, 8),
            (100, 31),
        ]
        correct_count = 0
        for input_n, expected_output in test_cases:
            actual_output = get_max_generated_array(input_n)
            if actual_output == expected_output:
                print('True')
                correct_count += 1
            else:
                print('False')
        print(f"{correct_count}/{len(test_cases)}")

    run_tests()

solve()