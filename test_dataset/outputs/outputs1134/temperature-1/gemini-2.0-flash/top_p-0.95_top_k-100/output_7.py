def maxJumps(arr, d):
    n = len(arr)
    dp = [0] * n

    def solve(i):
        if dp[i] != 0:
            return dp[i]

        max_reachable = 1
        
        # Jump to the right
        for j in range(i + 1, min(i + d + 1, n)):
            valid_jump = True
            for k in range(i + 1, j):
                if arr[i] <= arr[k]:
                    valid_jump = False
                    break
            if valid_jump and arr[i] > arr[j]:
                max_reachable = max(max_reachable, 1 + solve(j))
                
        # Jump to the left
        for j in range(i - 1, max(i - d - 1, -1), -1):
            valid_jump = True
            for k in range(j + 1, i):
                if arr[i] <= arr[k]:
                    valid_jump = False
                    break
            if valid_jump and arr[i] > arr[j]:
                max_reachable = max(max_reachable, 1 + solve(j))

        dp[i] = max_reachable
        return dp[i]

    max_result = 0
    for i in range(n):
        max_result = max(max_result, solve(i))

    return max_result

def test_maxJumps():
    test_cases = [
        ([6,4,14,6,8,13,9,7,10,6,12], 2, 4),
        ([3,3,3,3,3], 3, 1),
        ([7,6,5,4,3,2,1], 1, 7),
        ([7,1,7,1,7,1], 2, 2),
        ([66], 1, 1),
        ([1,2,3,4,5,6,7,8,9,10], 2, 2),
        ([10,9,8,7,6,5,4,3,2,1], 2, 10),
        ([1,2,3,2,1], 2, 3),
        ([1,2,1,2,1], 2, 3),
        ([1,2,3], 1, 1),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (arr, d, expected) in enumerate(test_cases):
        result = maxJumps(arr, d)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")
    
    print(f"\nCorrect: {correct_count}/{total_tests}")

if __name__ == "__main__":
    test_maxJumps()