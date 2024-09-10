def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    return closest_sum

# Example 1 Inputs and Outputs
test_input_1 = [-1, 2, 1, -4]
test_target_1 = 1
test_output_1 = 2
print(three_sum_closest(test_input_1, test_target_1) == test_output_1)

# Include any additional examples for verification.
# Example 2 and 3 are not provided in the problem description.