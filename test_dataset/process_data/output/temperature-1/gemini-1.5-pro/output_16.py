def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return target
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
    
    return closest_sum


nums1 = [-1,2,1,-4]
target1 = 1
output1 = three_sum_closest(nums1, target1)

print(f'Input 1: {nums1}, {target1}')
print(f'Output 1: {output1}')
print(f'Expected Output 1: 2')
print(f'Test 1 Passed: {output1 == 2}')