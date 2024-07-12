def two_sum(nums, target):
  """
  Finds two numbers in an array that sum to a given target.

  Args:
    nums: A list of integers.
    target: The target sum.

  Returns:
    A list containing the indices of the two numbers that sum to the target, or None if no such pair exists.
  """
  seen = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
      return [seen[complement], i]
    seen[num] = i
  return None

# Example usage
nums = [3,2,4]
target = 6

result = two_sum(nums, target)
if result:
  print(f"Indices of the two numbers that sum to {target}: {result}")
else:
  print(f"No two numbers in the array sum to {target}")
