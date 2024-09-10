def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Example Inputs
nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

# Example Outputs
output1 = 2
output2 = 5

# Verify Examples
print(removeDuplicates(nums1) == output1)
print(removeDuplicates(nums2) == output2)