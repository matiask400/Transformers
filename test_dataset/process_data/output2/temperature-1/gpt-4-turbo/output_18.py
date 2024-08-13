def four_sum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                sum_val = nums[i] + nums[j] + nums[left] + nums[right]
                if sum_val == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_val < target:
                    left += 1
                else:
                    right -= 1
    return result

inputs = [([1,0,-1,0,-2,2], 0), ([], 0), (third_input_example, third_input_target)]
outputs = [[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], [], third_output_example]
for input_val, expected in zip(inputs, outputs):
    result = four_sum(*input_val)
    print(result == expected)