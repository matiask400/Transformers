import math

def threeSumClosest(nums, target):
    """Finds three integers in nums such that the sum is closest to the target."""
    nums.sort()  # Sort the array in ascending order
    n = len(nums)  # Get the length of the array
    closestSum = math.inf  # Initialize the closest sum to infinity
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements
        left, right = i + 1, n - 1
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum
            if currentSum < target:
                left += 1
            else:
                right -= 1
    return closestSum

# Test the solution with the given inputs and expected outputs
input1 = [-1,2,1,-4]
target1 = 1
output1 = threeSumClosest(input1, target1)
print(output1 == 2)

input2 = [0,0,0]
target2 = 1
output2 = threeSumClosest(input2, target2)
print(output2 == 0)

input3 = [1,1,-1,-1,3]
target3 = -1
output3 = threeSumClosest(input3, target3)
print(output3 == -1)