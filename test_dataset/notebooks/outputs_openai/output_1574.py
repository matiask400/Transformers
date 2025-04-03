def remove_subarray_length(arr):
    n = len(arr)
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    if left == n - 1:
        return 0
    right = n - 1
    while right > 0 and arr[right - 1] <= arr[right]:
        right -= 1
    res = min(n - left - 1, right)
    i, j = 0, right
    while i <= left and j < n:
        if arr[i] <= arr[j]:
            res = min(res, j - i - 1)
            i += 1
        else:
            j += 1
    return res

def run_tests():
    tests = [
        {"input": [1,2,3,10,4,2,3,5], "expected": 3},
        {"input": [5,4,3,2,1], "expected": 4},
        {"input": [1,2,3], "expected": 0},
        {"input": [1], "expected": 0},
    ]
    correct = 0
    total = len(tests)
    for test in tests:
        output = remove_subarray_length(test["input"])
        expected = test["expected"]
        if output == expected:
            print('True')
            correct += 1
        else:
            print('False')
    print(f"{correct}/{total}")

run_tests()