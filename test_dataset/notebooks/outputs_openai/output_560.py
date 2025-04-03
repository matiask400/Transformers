def count_subarrays(nums, k):
    count = 0
    current_sum = 0
    sum_freq = {0: 1}
    for num in nums:
        current_sum += num
        if current_sum - k in sum_freq:
            count += sum_freq[current_sum - k]
        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1
    return count

tests = [
    {'nums': [1,1,1], 'k': 2, 'expected': 2},
    {'nums': [1,2,3], 'k': 3, 'expected': 2},
    {'nums': [1], 'k': 0, 'expected': 0},
    {'nums': [1,-1,0], 'k': 0, 'expected': 3},
    {'nums': [3,4,7,2,-3,1,4,2], 'k': 7, 'expected': 4},
]

correct = 0
total = len(tests)
for test in tests:
    result = count_subarrays(test['nums'], test['k'])
    is_correct = result == test['expected']
    print(is_correct)
    if is_correct:
        correct += 1
print(f"{correct}/{total}")