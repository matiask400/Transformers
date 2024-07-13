def threeSumClosest(nums, target):
    """  
    Given an array \"nums\" of n integers and an integer \"target\", find three integers in \"nums\" such that the sum is closest to \"target\". Return the sum of the three integers. You may assume that each input would have exactly one solution.

    Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
    Constraints:
    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4

    "  
    nums.sort()
    result = nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        left , right = i+1,len(nums)-1
        while left<right:
            current_sum = nums[left] + nums[right] + nums[i]
            if abs(target-current_sum)<abs(target-result):
                result=current_sum
            if current_sum<target:
                left+=1
            else:
                right-=1
    return result

# Example 1:
nums1 = [-1, 2, 1, -4]
target1 = 1 
result1 = threeSumClosest(nums1,target1)  

# Example 2:
nums2 = [1, 1, -1, -1, 3]
target2 = -1 
result2 = threeSumClosest(nums2,target2) 

# Example 3:
nums3 = [0, 2, 1, -3]
target3 = 1
result3 = threeSumClosest(nums3,target3) 

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)

assert result1 == 2
assert result2 == -1
assert result3 == 0