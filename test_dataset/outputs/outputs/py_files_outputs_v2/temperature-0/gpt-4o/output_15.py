def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res

# Example inputs and expected outputs
input_1 = [-1, 0, 1, 2, -1, -4]
output_1 = [[-1, -1, 2], [-1, 0, 1]]
input_2 = []
output_2 = []
input_3 = [0]
output_3 = []

# Verify the solution
print(three_sum(input_1) == output_1)
print(three_sum(input_2) == output_2)
print(three_sum(input_3) == output_3)