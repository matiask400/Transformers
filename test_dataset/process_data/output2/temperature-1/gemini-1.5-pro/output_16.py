# Solution
def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum

    return closest_sum


# Example Input 1
nums1 = [-1, 2, 1, -4]
target1 = 1
# Expected Output 1
output1 = 2
# Test
print(three_sum_closest(nums1, target1) == output1)
