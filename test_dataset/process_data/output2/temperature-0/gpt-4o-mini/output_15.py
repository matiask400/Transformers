def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

# Example inputs
input_1 = [-1, 0, 1, 2, -1, -4]
output_1 = [[-1, -1, 2], [-1, 0, 1]]
input_2 = []
output_2 = []
input_3 = [0]
output_3 = []

# Testing the function
print(three_sum(input_1) == output_1)  # True
print(three_sum(input_2) == output_2)  # True
print(three_sum(input_3) == output_3)  # True