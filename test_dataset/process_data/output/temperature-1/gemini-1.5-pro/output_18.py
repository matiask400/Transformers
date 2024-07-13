def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        # Skip duplicate numbers for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            # Skip duplicate numbers for the second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate numbers for the third element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate numbers for the fourth element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    return result


test_cases = [([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
              ([], 0, []),
              ]

for case in test_cases:
    nums, target, expected = case
    result = fourSum(nums, target)
    print(result == expected)