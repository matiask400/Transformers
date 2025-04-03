def nextGreaterElement(nums1, nums2):
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)
    while stack:
        next_greater[stack.pop()] = -1
    return [next_greater[num] for num in nums1]

test_cases = [
    {
        'nums1': [4,1,2],
        'nums2': [1,3,4,2],
        'expected': [-1,3,-1]
    },
    {
        'nums1': [2,4],
        'nums2': [1,2,3,4],
        'expected': [3,-1]
    }
]

passed = 0
total = len(test_cases)
for test in test_cases:
    output = nextGreaterElement(test['nums1'], test['nums2'])
    is_correct = output == test['expected']
    print(is_correct)
    if is_correct:
        passed +=1
print(f"{passed}/{total}")