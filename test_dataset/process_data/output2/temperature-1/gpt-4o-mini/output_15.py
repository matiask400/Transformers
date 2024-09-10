def three_sum(nums):
    nums.sort()
    result = set()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return [list(triplet) for triplet in result]

# Example Inputs
input_1 = [-1,0,1,2,-1,-4]
output_1 = [[-1,-1,2],[-1,0,1]]
input_2 = []
output_2 = []
input_3 = [0]
output_3 = []

# Testing
result_1 = three_sum(input_1)
result_2 = three_sum(input_2)
result_3 = three_sum(input_3)

print(result_1 == output_1)  # True or False
print(result_2 == output_2)  # True or False
print(result_3 == output_3)  # True or False