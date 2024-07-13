def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result


if __name__ == '__main__':
    input1 = [-1, 0, 1, 2, -1, -4]
    output1 = [[-1, -1, 2], [-1, 0, 1]]
    input2 = []
    output2 = []
    input3 = [0]
    output3 = []

    print(f'Test 1: {three_sum(input1) == output1}')
    print(f'Test 2: {three_sum(input2) == output2}')
    print(f'Test 3: {three_sum(input3) == output3}')