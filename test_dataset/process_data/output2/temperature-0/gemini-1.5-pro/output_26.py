def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


def test_remove_duplicates(nums, expected_output):
    result = removeDuplicates(nums)
    nums = nums[:result]
    return nums == expected_output

# Test cases
input1 = [1, 1, 2]
output1 = [1, 2]
print(f"Input 1: {input1}, Output 1: {test_remove_duplicates(input1, output1)}")

input2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
output2 = [0, 1, 2, 3, 4]
print(f"Input 2: {input2}, Output 2: {test_remove_duplicates(input2, output2)}")