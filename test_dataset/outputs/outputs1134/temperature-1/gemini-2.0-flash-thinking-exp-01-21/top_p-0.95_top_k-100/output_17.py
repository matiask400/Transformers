def solve():
    def get_maximum_generated(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        for i in range(1, n // 2 + 1):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums)

    test_cases = [
        (7, 3),
        (2, 1),
        (3, 2),
        (0, 0),
        (1, 1),
        (4, 2),
        (5, 3),
        (6, 3),
        (10, 5),
        (15, 8),
        (20, 10),
        (50, 25),
        (100, 50)
    ]

    correct_tests = 0
    for n, expected_output in test_cases:
        output = get_maximum_generated(n)
        if output == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')
    print(f"{correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    solve()