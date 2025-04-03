def solve():
    def generate_array(n):
        nums = [0] * (n + 1)
        nums[0] = 0
        if n >= 1:
            nums[1] = 1
        for i in range(1, (n // 2) + 1):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        return nums
    
    def get_maximum_generated(n):
        nums = generate_array(n)
        if not nums:
            return 0
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
            (100, 7)
        ]
        
        correct_count = 0
        total_count = len(test_cases)

        for n, expected in test_cases:
            result = get_maximum_generated(n)
            if result == expected:
                print("True")
                correct_count += 1
            else:
                print("False")
        
        print(f"{correct_count}/{total_count}")
    
    run_tests()

solve()