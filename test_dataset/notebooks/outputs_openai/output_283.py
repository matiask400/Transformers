def moveZeroes(nums):
    last_non_zero = 0
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero], nums[current] = nums[current], nums[last_non_zero]
            last_non_zero +=1

def run_tests():
    test_cases = [
        ([0,1,0,3,12], [1,3,12,0,0]),
        ([0], [0]),
        ([1,0,1], [1,1,0]),
        ([0,0,1], [1,0,0]),
        ([4,2,4,0,0,3,0,5,1,0], [4,2,4,3,5,1,0,0,0,0]),
        ([1,2,3,4,5], [1,2,3,4,5]),
        ([0,0,0,0], [0,0,0,0]),
        ([0,1], [1,0]),
        ([1,0], [1,0]),
    ]
    correct = 0
    total = len(test_cases)
    for nums, expected in test_cases:
        nums_copy = nums.copy()
        moveZeroes(nums_copy)
        if nums_copy == expected:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()