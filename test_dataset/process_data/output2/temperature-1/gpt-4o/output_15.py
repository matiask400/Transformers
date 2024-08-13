def three_sum(nums):
    nums.sort()
    res = []
    length = len(nums)
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, length - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res

# Testing the solutions
input_1 = [-1,0,1,2,-1,-4]
output_1 = [[-1,-1,2],[-1,0,1]]
input_2 = []
output_2 = []
input_3 = [0]
output_3 = []
print(three_sum(input_1) == output_1)  # Should print True
print(three_sum(input_2) == output_2)  # Should print True
print(three_sum(input_3) == output_3)  # Should print True