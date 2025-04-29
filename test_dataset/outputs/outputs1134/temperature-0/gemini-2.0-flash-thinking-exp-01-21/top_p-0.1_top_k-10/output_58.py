def min_start_value(nums):
    start_value = 1
    while True:
        current_sum = start_value
        is_valid = True
        for num in nums:
            current_sum += num
            if current_sum < 1:
                is_valid = False
                break
        if is_valid:
            return start_value
        start_value += 1

def run_tests():
    test_cases = [
        {"nums": [-3, 2, -3, 4, 2], "expected": 5},
        {"nums": [1, 2], "expected": 1},
        {"nums": [1, -2, -3], "expected": 5},
        {"nums": [0, 0], "expected": 1},
        {"nums": [-100], "expected": 101},
        {"nums": [100], "expected": 1},
        {"nums": [-1, -2, -3], "expected": 7},
        {"nums": [2, -1, -2], "expected": 2},
        {"nums": [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]}, # Example from similar problem
    ]
    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        nums = test_case["nums"]
        expected_output = test_case["expected"]
        actual_output = min_start_value(nums)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()