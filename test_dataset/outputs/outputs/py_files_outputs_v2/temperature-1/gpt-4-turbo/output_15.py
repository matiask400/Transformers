def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
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

# Test Cases
def verify_output(nums, expected):
    output = three_sum(nums)
    return sorted([sorted(sublist) for sublist in output]) == sorted([sorted(sublist) for sublist in expected])

print(verify_output([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]))
print(verify_output([], []))
print(verify_output([0], []))