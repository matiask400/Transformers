def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result


input_values = [
    ([1, 0, -1, 0, -2, 2], 0),
    ([], 0),
]

expected_outputs = [
    [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
    []
]

for i, (input_val, expected_output) in enumerate(zip(input_values, expected_outputs)):
    print(f"Test Case {i + 1}: {four_sum(input_val[0], input_val[1]) == expected_output}")