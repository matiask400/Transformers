def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_xor(nums):
    n = len(nums)
    xor_sum = 0
    for i in range(n + 1):
        xor_sum ^= i
    for num in nums:
        xor_sum ^= num
    return xor_sum

def run_tests():
    test_cases = [
        {"input": [3, 0, 1], "expected": 2},
        {"input": [0, 1], "expected": 2},
        {"input": [9, 6, 4, 2, 3, 5, 7, 0, 1], "expected": 8},
        {"input": [0], "expected": 1},
        {"input": [1], "expected": 0},
        {"input": [0, 2, 3], "expected": 1},
        {"input": [1, 2, 3], "expected": 0},
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        nums = test_case["input"]
        expected_output = test_case["expected"]

        # Using sum method
        output_sum = find_missing_number(nums)
        if output_sum == expected_output:
            print(f"Test {i+1} (Sum method): True")
            correct_count += 1
        else:
            print(f"Test {i+1} (Sum method): False, Input: {nums}, Expected: {expected_output}, Output: {output_sum}")

        # Using XOR method
        output_xor = find_missing_number_xor(nums)
        if output_xor == expected_output:
            print(f"Test {i+1} (XOR method): True")
        else:
            print(f"Test {i+1} (XOR method): False, Input: {nums}, Expected: {expected_output}, Output: {output_xor}")

    print(f"\nCorrect tests: {correct_count}/{total_count}")

if __name__ == '__main__':
    run_tests()