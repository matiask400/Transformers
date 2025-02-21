def four_sum(nums, target):
    nums.sort()
    quadruplets = set()
    n = len(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    quadruplets.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return [list(quad) for quad in quadruplets]

# Example inputs
input_1 = ([1, 0, -1, 0, -2, 2], 0)
output_1 = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
result_1 = four_sum(*input_1) == output_1

input_2 = ([], 0)
output_2 = []
result_2 = four_sum(*input_2) == output_2

# Print results
print(result_1)
print(result_2)