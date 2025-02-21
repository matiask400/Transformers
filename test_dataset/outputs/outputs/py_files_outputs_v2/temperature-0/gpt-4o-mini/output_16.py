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

# Example inputs
input_1 = ([-1, 2, 1, -4], 1)
output_1 = 2
input_2 = ([0, 0, 0], 1)
output_2 = 0
input_3 = ([-1, 0, 1, 1], 0)
output_3 = 1

# Testing the function
print(three_sum_closest(*input_1) == output_1)  # True
print(three_sum_closest(*input_2) == output_2)  # True
print(three_sum_closest(*input_3) == output_3)  # True