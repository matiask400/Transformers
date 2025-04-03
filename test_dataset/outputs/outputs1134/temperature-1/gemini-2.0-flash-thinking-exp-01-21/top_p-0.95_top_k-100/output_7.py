def get_possible_jumps(arr, d, i):
    jumps = []
    for x in range(1, d + 1):
        # forward jump
        j = i + x
        if j < len(arr):
            if arr[i] > arr[j]:
                valid_jump = True
                for k in range(min(i, j) + 1, max(i, j)):
                    if arr[i] <= arr[k]:
                        valid_jump = False
                        break
                if valid_jump:
                    jumps.append(j)
        # backward jump
        j = i - x
        if j >= 0:
            if arr[i] > arr[j]:
                valid_jump = True
                for k in range(min(i, j) + 1, max(i, j)):
                    if arr[i] <= arr[k]:
                        valid_jump = False
                        break
                if valid_jump:
                    jumps.append(j)
    return jumps

def solve(arr, d, i, memo):
    if i in memo:
        return memo[i]
    max_count = 1
    for j in get_possible_jumps(arr, d, i):
        max_count = max(max_count, 1 + solve(arr, d, j, memo))
    memo[i] = max_count
    return max_count

def max_indices_visited(arr, d):
    max_indices = 0
    for i in range(len(arr)):
        max_indices = max(max_indices, solve(arr, d, i, {}))
    return max_indices

def run_tests():
    test_cases = [
        {"arr": [6,4,14,6,8,13,9,7,10,6,12], "d": 2, "expected": 4},
        {"arr": [3,3,3,3,3], "d": 3, "expected": 1},
        {"arr": [7,6,5,4,3,2,1], "d": 1, "expected": 7},
        {"arr": [7,1,7,1,7,1], "d": 2, "expected": 2},
        {"arr": [66], "d": 1, "expected": 1},
    ]
    correct_count = 0
    for i, case in enumerate(test_cases):
        arr = case["arr"]
        d = case["d"]
        expected_output = case["expected"]
        output = max_indices_visited(arr, d)
        if output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()