def solve():
    def subarray_sum(nums, n, left, right):
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        
        subarray_sums.sort()
        
        total_sum = 0
        for i in range(left - 1, right):
            total_sum = (total_sum + subarray_sums[i]) % (10**9 + 7)
        
        return total_sum

    def test_cases():
        test_data = [
            ([1,2,3,4], 4, 1, 5, 13),
            ([1,2,3,4], 4, 3, 4, 6),
            ([1,2,3,4], 4, 1, 10, 50),
            ([4,5,6], 3, 1, 3, 19),
            ([4,5,6], 3, 4, 6, 21),
            ([1,4,2,3], 4, 1, 4, 17),
            ([1,4,2,3], 4, 5, 7, 18),
            ([1,4,2,3], 4, 8, 10, 15),
            ([1,1,1], 3, 1, 6, 10),
            ([1,1,1], 3, 1, 3, 3),
            ([1,1,1], 3, 4, 6, 7)
        ]

        num_tests = len(test_data)
        correct_tests = 0

        for i, (nums, n, left, right, expected) in enumerate(test_data):
            result = subarray_sum(nums, n, left, right)
            if result == expected:
                print("True")
                correct_tests += 1
            else:
                print("False")
                print(f"Test {i+1}: Expected {expected}, got {result}")

        print(f"{correct_tests}/{num_tests}")

    test_cases()

solve()