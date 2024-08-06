def two_sum(nums, target):
    nums_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement], i]
        nums_dict[num] = i
    return None

# Example 1
nums_1 = [2, 7, 11, 15]
target_1 = 9
result_1 = two_sum(nums_1, target_1)
print(f"Example 1: Output: {result_1}")

# Example 2
nums_2 = [3, 2, 4]
target_2 = 6
result_2 = two_sum(nums_2, target_2)
print(f"Example 2: Output: {result_2}")

# Example 3
nums_3 = [3, 3]
target_3 = 6
result_3 = two_sum(nums_3, target_3)
print(f"Example 3: Output: {result_3}")

# Check if the results match the expected outputs
example_1_output = [0, 1]
example_2_output = [1, 2]
example_3_output = [0, 1]

print(f"Example 1: {result_1 == example_1_output}")
print(f"Example 2: {result_2 == example_2_output}")
print(f"Example 3: {result_3 == example_3_output}")