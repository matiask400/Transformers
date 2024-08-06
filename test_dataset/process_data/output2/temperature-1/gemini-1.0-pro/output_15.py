from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = num + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                triplets.append([num, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return triplets

# Example Inputs and Results 
input1 = [-1,0,1,2,-1,-4]
output1 = three_sum(input1)
print(output1 == [[-1,-1,2],[-1,0,1]])

input2 = []
output2 = three_sum(input2)
print(output2 == [])

input3 = [0]
output3 = three_sum(input3)
print(output3 == [])
# custom input 1
input4 = [1,2,-2,-1,0,2,2]
output4 = three_sum(input4)
print(output4 == [[-2,0,2],[-2,1,1]])

# custom input 2
input5 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
output5 = three_sum(input5)
print(output5 == [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]])

# custom input 3
input6 = [-1, -2, -3, 0, 1, 1, -3]
output6 = three_sum(input6)
print(output6 == [[-3,-2,1],[-1,-2,-1]])

# custom input 4
input7 = [-5, -3, -3, 0, 1, 1, -3, 4]
output7 = three_sum(input7)
print(output7 == [[-5,-3,8],[-3,-3,6]])