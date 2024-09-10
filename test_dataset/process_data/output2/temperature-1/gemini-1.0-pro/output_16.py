import sys


if __name__ == "__main__":
    input1 = [-1, 2, 1, -4]
    target1 = 1
    output1 = 2
    result1 = threeSumClosest(input1, target1)
    print(result1 == output1)

    input2 = [0, 0, 0]
    target2 = 1
    output2 = 0
    result2 = threeSumClosest(input2, target2)
    print(result2 == output2)

    input3 = [1, 1, 1, 1]
    target3 = -100
    output3 = -100
    result3 = threeSumClosest(input3, target3)
    print(result3 == output3)


def threeSumClosest(nums, target):
    nums.sort()
    result = sys.maxsize
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1

        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]

            if abs(current_sum - target) < abs(result - target):
                result = current_sum

            if current_sum < target:
                l += 1
            else:
                r -= 1

    return result