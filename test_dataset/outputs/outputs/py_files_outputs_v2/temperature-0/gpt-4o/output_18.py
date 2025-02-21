def four_sum(nums, target):
    nums.sort()
    results = []
    length = len(nums)
    for i in range(length - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, length - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, length - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return results

# Example inputs and expected outputs
inputs = [
    ([1, 0, -1, 0, -2, 2], 0),
    ([], 0)
]
expected_outputs = [
    [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
    []
]

# Verify the solution
for i, (nums, target) in enumerate(inputs):
    result = four_sum(nums, target)
    print(result == expected_outputs[i])