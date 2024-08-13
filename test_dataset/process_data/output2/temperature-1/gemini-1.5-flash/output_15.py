def threeSum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                right -= 1
    return result

# Example 1
nums_1 = [-1, 0, 1, 2, -1, -4]
output_1 = threeSum(nums_1)
expected_output_1 = [[-1, -1, 2], [-1, 0, 1]]
print(f"Example 1: {output_1 == expected_output_1}")

# Example 2
nums_2 = []
output_2 = threeSum(nums_2)
expected_output_2 = []
print(f"Example 2: {output_2 == expected_output_2}")

# Example 3
nums_3 = [0]
output_3 = threeSum(nums_3)
expected_output_3 = []
print(f"Example 3: {output_3 == expected_output_3}")