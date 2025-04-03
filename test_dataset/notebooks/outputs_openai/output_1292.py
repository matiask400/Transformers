def maxSideLength(mat, threshold):
    m = len(mat)
    n = len(mat[0]) if mat else 0
    if m == 0 or n == 0:
        return 0

    # Compute prefix sum matrix
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        row_sum = 0
        for j in range(1, n + 1):
            row_sum += mat[i-1][j-1]
            prefix[i][j] = prefix[i-1][j] + row_sum

    # Binary search for the maximum side length
    left, right = 1, min(m, n)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        found = False
        for i in range(mid, m + 1):
            for j in range(mid, n + 1):
                total = prefix[i][j] - prefix[i - mid][j] - prefix[i][j - mid] + prefix[i - mid][j - mid]
                if total <= threshold:
                    found = True
                    break
            if found:
                break
        if found:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

# Test cases
test_cases = [
    {
        "mat": [
            [1,1,3,2,4,3,2],
            [1,1,3,2,4,3,2],
            [1,1,3,2,4,3,2]
        ],
        "threshold": 4,
        "expected": 2
    },
    {
        "mat": [
            [2,2,2,2,2],
            [2,2,2,2,2],
            [2,2,2,2,2],
            [2,2,2,2,2],
            [2,2,2,2,2]
        ],
        "threshold": 1,
        "expected": 0
    },
    {
        "mat": [
            [1,1,1,1],
            [1,0,0,0],
            [1,0,0,0],
            [1,0,0,0]
        ],
        "threshold": 6,
        "expected": 3
    },
    {
        "mat": [
            [18,70],
            [61,1],
            [25,85],
            [14,40],
            [11,96],
            [97,96],
            [63,45]
        ],
        "threshold": 40184,
        "expected": 2
    }
]

correct = 0
total = len(test_cases)

for test in test_cases:
    mat = test["mat"]
    threshold = test["threshold"]
    expected = test["expected"]
    result = maxSideLength(mat, threshold)
    passed = result == expected
    print(passed)
    if passed:
        correct += 1

print(f"{correct}/{total}")