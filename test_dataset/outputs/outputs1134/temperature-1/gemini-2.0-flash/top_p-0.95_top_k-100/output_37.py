def solve():
    def subarraySum(nums, n, left, right):
        sums = []
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                sums.append(curr_sum)
        
        sums.sort()
        
        total_sum = 0
        for i in range(left - 1, right):
            total_sum = (total_sum + sums[i]) % (10**9 + 7)
        
        return total_sum

    def test_cases():
        tests = [
            ([1, 2, 3, 4], 4, 1, 5, 13),
            ([1, 2, 3, 4], 4, 3, 4, 6),
            ([1, 2, 3, 4], 4, 1, 10, 50),
            ([4,2,3], 3, 1, 4, 19),
            ([1,4,5,2,3], 5, 2, 7, 42)
        ]
        
        num_correct = 0
        total_tests = len(tests)

        for i, (nums, n, left, right, expected) in enumerate(tests):
            result = subarraySum(nums, n, left, right)
            if result == expected:
                print("True")
                num_correct += 1
            else:
                print("False")
        
        print(f"{num_correct}/{total_tests}")

    test_cases()

solve()