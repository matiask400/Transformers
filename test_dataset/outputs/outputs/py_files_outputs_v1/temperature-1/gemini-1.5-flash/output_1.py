def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

# Test cases
nums1 = [2, 7, 11, 15]
input1 = nums1, 9
output1 = two_sum(*input1)

nums2 = [3, 2, 4]
input2 = nums2, 6
output2 = two_sum(*input2)

nums3 = [3, 3]
input3 = nums3, 6
output3 = two_sum(*input3)

print(f"Input 1: {input1}, Output 1: {output1}")
print(f"Input 2: {input2}, Output 2: {output2}")
print(f"Input 3: {input3}, Output 3: {output3}")

result1 = output1 == [0, 1]
result2 = output2 == [1, 2]
result3 = output3 == [0, 1]
print(f"Result 1: {result1}, Result 2: {result2}, Result 3: {result3}")