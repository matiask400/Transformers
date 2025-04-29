def max_jumps(arr, d):
    n = len(arr)
    dp = [0] * n

    def dfs(i):
        if dp[i]:
            return dp[i]
        res = 1
        for direction in (-1, 1):
            for step in range(1, d + 1):
                j = i + direction * step
                if j < 0 or j >= n or arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))
        dp[i] = res
        return res

    return max(dfs(i) for i in range(n))

def run_tests():
    test_cases = [
        {
            'arr': [6,4,14,6,8,13,9,7,10,6,12],
            'd': 2,
            'expected': 4
        },
        {
            'arr': [3,3,3,3,3],
            'd': 3,
            'expected': 1
        },
        {
            'arr': [7,6,5,4,3,2,1],
            'd': 1,
            'expected': 7
        },
        {
            'arr': [7,1,7,1,7,1],
            'd': 2,
            'expected': 2
        },
        {
            'arr': [66],
            'd': 1,
            'expected': 1
        }
    ]

    correct = 0
    total = len(test_cases)
    for idx, test in enumerate(test_cases, 1):
        result = max_jumps(test['arr'], test['d'])
        is_correct = result == test['expected']
        print(is_correct)
        if is_correct:
            correct += 1
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()