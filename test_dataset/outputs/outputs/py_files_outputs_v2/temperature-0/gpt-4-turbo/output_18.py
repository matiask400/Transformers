def four_sum(nums, target):
    nums.sort()
    results = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    results.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
    return results

# Test cases
nums1, target1 = [1,0,-1,0,-2,2], 0
expected_output1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
output1 = four_sum(nums1, target1)
print('Test 1:', sorted(output1) == sorted(expected_output1))

nums2, target2 = [], 0
expected_output2 = []
output2 = four_sum(nums2, target2)
print('Test 2:', output2 == expected_output2)