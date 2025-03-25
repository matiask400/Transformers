def twoSum(nums, target):
    """
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    """
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index