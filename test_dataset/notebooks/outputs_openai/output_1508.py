def subarray_sum_sorted(nums, n, left, right):
    MOD = 10**9 + 7
    sub_sums = []
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            sub_sums.append(current_sum)
    sub_sums.sort()
    return sum(sub_sums[left-1:right]) % MOD

# Define test cases
test_cases = [
    {
        'nums': [1,2,3,4],
        'n': 4,
        'left': 1,
        'right': 5,
        'expected': 13
    },
    {
        'nums': [1,2,3,4],
        'n': 4,
        'left': 3,
        'right': 4,
        'expected': 6
    },
    {
        'nums': [1,2,3,4],
        'n': 4,
        'left': 1,
        'right': 10,
        'expected': 50
    }
]

correct = 0
total = len(test_cases)

for test in test_cases:
    result = subarray_sum_sorted(test['nums'], test['n'], test['left'], test['right'])
    if result == test['expected']:
        print(True)
        correct +=1
    else:
        print(False)

print(f"{correct}/{total}")