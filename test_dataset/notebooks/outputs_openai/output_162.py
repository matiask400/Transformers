def findPeakElement(nums):
    left, right = 0, len(nums) -1
    while left < right:
        mid = left + (right - left)//2
        if nums[mid] > nums[mid +1]:
            right = mid
        else:
            left = mid +1
    return left

test_cases = [
    {"nums": [1,2,3,1], "expected": 2},
    {"nums": [1,2,1,3,5,6,4], "expected": 5},
    {"nums": [1], "expected": 0},
    {"nums": [2,1], "expected": 0},
    {"nums": [1,2], "expected": 1},
    {"nums": [1,3,2,1], "expected":1},
    {"nums": [1,2,3,4,5], "expected":4},
    {"nums": [5,4,3,2,1], "expected":0},
]

correct = 0
total = len(test_cases)

for test in test_cases:
    result = findPeakElement(test["nums"])
    if result == test["expected"]:
        print(True)
        correct +=1
    else:
        print(False)

print(f"{correct}/{total}")