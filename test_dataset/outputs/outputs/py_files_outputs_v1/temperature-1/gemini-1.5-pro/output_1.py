def two_sum(nums, target):
    num_indices = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], index]
        num_indices[num] = index


# Input 1
nums1 = [2, 7, 11, 15]
target1 = 9
output1 = [0, 1]

# Input 2
nums2 = [3, 2, 4]
target2 = 6
output2 = [1, 2]

# Input 3
nums3 = [3, 3]
target3 = 6
output3 = [0, 1]

print(f'{two_sum(nums1,target1) == output1}')
print(f'{two_sum(nums2,target2) == output2}')
print(f'{two_sum(nums3,target3) == output3}')