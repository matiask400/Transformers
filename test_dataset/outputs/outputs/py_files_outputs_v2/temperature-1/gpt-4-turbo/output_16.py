import sys
def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = sys.maxsize
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
                return current_sum
    return closest_sum

# Test cases
inputs = [([-1, 2, 1, -4], 1)]
outputs = [2]
results = [three_sum_closest(*inp) == out for inp, out in zip(inputs, outputs)]
print('Test Results:', results)