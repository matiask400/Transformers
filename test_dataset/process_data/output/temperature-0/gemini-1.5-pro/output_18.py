def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

# Test cases
input_1 = [1, 0, -1, 0, -2, 2]
target_1 = 0
output_1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

input_2 = []
target_2 = 0
output_2 = []

# No input 3 and output 3 provided in the context

print(f'Test 1: {four_sum(input_1, target_1) == output_1}')
print(f'Test 2: {four_sum(input_2, target_2) == output_2}')