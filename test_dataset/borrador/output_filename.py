def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


# Test cases
input1 = [2, 7, 11, 15]
target1 = 9
output1 = [0, 1]

input2 = [3, 2, 4]
target2 = 6
output2 = [1, 2]

input3 = [3, 3]
target3 = 6
output3 = [0, 1]

print(f"Test 1: {two_sum(input1, target1) == output1}")
print(f"Test 2: {two_sum(input2, target2) == output2}")
print(f"Test 3: {two_sum(input3, target3) == output3}")