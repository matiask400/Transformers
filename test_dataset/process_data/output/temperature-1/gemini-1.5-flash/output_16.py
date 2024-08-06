import sys

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = sys.maxsize
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum

# Example usage:
nums = [-1, 2, 1, -4]
 target = 1

result = threeSumClosest(nums, target)

print(f'Output: {result}')

# Check if the output is correct
output_is_correct = result == 2
print(f'Output is correct: {output_is_correct}')