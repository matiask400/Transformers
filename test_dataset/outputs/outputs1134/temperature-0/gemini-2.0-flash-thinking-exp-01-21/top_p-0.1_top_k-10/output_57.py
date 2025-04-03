def solve():
    def calculate_money(n):
        total_amount = 0
        monday_deposit = 1
        current_deposit = monday_deposit
        day_of_week = 1
        for _ in range(n):
            total_amount += current_deposit
            if day_of_week == 7:
                monday_deposit += 1
                current_deposit = monday_deposit
                day_of_week = 1
            else:
                current_deposit += 1
                day_of_week += 1
        return total_amount

    test_cases = [
        {"input": 4, "expected_output": 10},
        {"input": 10, "expected_output": 37},
        {"input": 20, "expected_output": 96},
        {"input": 1, "expected_output": 1},
        {"input": 7, "expected_output": 28},
        {"input": 8, "expected_output": 30},
        {"input": 14, "expected_output": 63},
        {"input": 15, "expected_output": 66},
        {"input": 21, "expected_output": 99},
        {"input": 22, "expected_output": 103},
        {"input": 28, "expected_output": 140},
    ]

    correct_tests = 0
    for i, case in enumerate(test_cases):
        input_n = case["input"]
        expected_output = case["expected_output"]
        actual_output = calculate_money(input_n)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"Input: {input_n}, Expected Output: {expected_output}, Actual Output: {actual_output}")

    print(f"\n{correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    solve()