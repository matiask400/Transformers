def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = two_sum(nums1, target1)
print(f'Example 1: Input: {nums1}, {target1}, Output: {result1}')

# Example 2
nums2 = [3, 2, 4]
target2 = 6
result2 = two_sum(nums2, target2)
print(f'Example 2: Input: {nums2}, {target2}, Output: {result2}')

# Example 3
nums3 = [3, 3]
target3 = 6
result3 = two_sum(nums3, target3)
print(f'Example 3: Input: {nums3}, {target3}, Output: {result3}')