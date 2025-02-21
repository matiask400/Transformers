def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum
    return closest_sum

# Test cases
inputs = [([-1, 2, 1, -4], 1)]
expected_outputs = [2]
results = [three_sum_closest(*inp) == exp for inp, exp in zip(inputs, expected_outputs)]
print(results)