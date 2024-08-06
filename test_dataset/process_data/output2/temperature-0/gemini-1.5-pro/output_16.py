def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return target

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


# Test cases
input_1 = [-1, 2, 1, -4]
target_1 = 1
output_1 = 2

input_2 = None  # No second example provided
target_2 = None
output_2 = None

input_3 = None  # No third example provided
target_3 = None
output_3 = None

print(f"Input 1: {three_sum_closest(input_1, target_1) == output_1}")

# Cannot test input 2 and 3 as they are not provided