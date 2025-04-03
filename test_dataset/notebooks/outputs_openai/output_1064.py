def find_fixed_point(arr):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            result = mid
            right = mid - 1  # Look for a smaller index
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return result

def run_tests():
    tests = [
        ([-10, -5, 0, 3, 7], 3),
        ([0, 2, 5, 8, 17], 0),
        ([-10, -5, 3, 4, 7, 9], -1),
        ([-1, 0, 1, 3, 5], 3),
        ([-20, -10, -5, -2, 4, 5, 6], 4),
        ([1], -1),
        ([0], 0),
        ([-1, 0, 2, 4, 5], 2),
        ([-5, -4, -3, -2, -1], -1),
        ([-10, -5, -2, 3, 4, 5, 6, 7, 8, 9], 3),
    ]
    correct = 0
    for i, (arr, expected) in enumerate(tests, 1):
        output = find_fixed_point(arr)
        if output == expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct} / {len(tests)}")

run_tests()