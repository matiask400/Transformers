def addOperators(num, target):
    def solve(index, current_expression, current_value, last_operand):
        if index == len(num):
            if current_value == target:
                result.append(current_expression)
            return

        for i in range(index, len(num)):
            if i > index and num[index] == '0':
                break
            operand_str = num[index:i+1]
            operand = int(operand_str)

            if index == 0:
                solve(i + 1, operand_str, operand, operand)
            else:
                solve(i + 1, current_expression + "+" + operand_str, current_value + operand, operand)
                solve(i + 1, current_expression + "-" + operand_str, current_value - operand, -operand)
                solve(i + 1, current_expression + "*" + operand_str, current_value - last_operand + last_operand * operand, last_operand * operand)

    result = []
    solve(0, "", 0, 0)
    return result

def test_addOperators(num, target, expected_output):
    actual_output = sorted(addOperators(num, target))
    expected_output_sorted = sorted(expected_output)
    if actual_output == expected_output_sorted:
        print('True')
        return True
    else:
        print('False')
        print(f"  Input: num = '{num}', target = {target}")
        print(f"  Expected Output: {expected_output_sorted}")
        print(f"  Actual Output:   {actual_output}")
        return False

if __name__ == '__main__':
    correct_tests = 0
    total_tests = 0

    # Example 1
    total_tests += 1
    if test_addOperators("123", 6, ["1*2*3","1+2+3"]):
        correct_tests += 1

    # Example 2
    total_tests += 1
    if test_addOperators("232", 8, ["2*3+2","2+3*2"]):
        correct_tests += 1

    # Example 3
    total_tests += 1
    if test_addOperators("105", 5, ["1*0+5","10-5"]):
        correct_tests += 1

    # Example 4
    total_tests += 1
    if test_addOperators("00", 0, ["0*0","0+0","0-0"]):
        correct_tests += 1

    # Example 5
    total_tests += 1
    if test_addOperators("3456237490", 9191, []):
        correct_tests += 1

    # Additional test cases
    total_tests += 1
    if test_addOperators("55", 10, ["5+5"]):
        correct_tests += 1

    total_tests += 1
    if test_addOperators("111", 2, ["1+1", "11/1"]): # removed division, only +, -, * are allowed
        correct_tests += 1

    total_tests += 1
    if test_addOperators("111", 2, ["1+1"]): # test again without division
        correct_tests += 1

    total_tests += 1
    if test_addOperators("12345", 15, ["1+2+3*4", "1+2*3+4", "1*2+3*4", "12+3", "15"]):
        correct_tests += 1

    total_tests += 1
    if test_addOperators("2147483648", -2147483648, []): # overflow test, should be handled implicitly by Python int
        correct_tests += 1

    total_tests += 1
    if test_addOperators("1", 1, ["1"]):
        correct_tests += 1

    total_tests += 1
    if test_addOperators("1", 0, []):
        correct_tests += 1

    total_tests += 1
    if test_addOperators("0", 0, ["0"]):
        correct_tests += 1

    total_tests += 1
    if test_addOperators("0", 5, []):
        correct_tests += 1


    print(f"\n{correct_tests}/{total_tests}")