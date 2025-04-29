def add_operators(num, target):
    """
    Finds all possibilities to add binary operators '+', '-', or '*' between the digits of num
    so that the resultant expression evaluates to the target value.

    Args:
        num (str): A string containing only digits.
        target (int): The target value.

    Returns:
        list[str]: A list of strings representing the expressions that evaluate to the target value.
    """

    def helper(index, current_expression, current_value, previous_operand):
        if index == len(num):
            if current_value == target:
                results.append(current_expression)
            return

        for i in range(index, len(num)):
            if i > index and num[index] == '0':
                break  # Avoid leading zeros

            current_string = num[index:i + 1]
            current_number = int(current_string)

            if index == 0:
                helper(i + 1, current_string, current_number, current_number)
            else:
                helper(i + 1, current_expression + '+' + current_string, current_value + current_number, current_number)
                helper(i + 1, current_expression + '-' + current_string, current_value - current_number, -current_number)
                helper(i + 1, current_expression + '*' + current_string, current_value - previous_operand + previous_operand * current_number, previous_operand * current_number)

    results = []
    helper(0, "", 0, 0)
    return results


def test_add_operators():
    test_cases = [
        ("123", 6, ["1*2*3", "1+2+3"]),
        ("232", 8, ["2*3+2", "2+3*2"]),
        ("105", 5, ["1*0+5", "10-5"]),
        ("00", 0, ["0*0", "0+0", "0-0"]),
        ("3456237490", 9191, []),
        ("1", 1, ["1"]),
        ("1+1", 2, []),
        ("10", 10, ["10"]),
        ("10", 1, []),
        ("100", 1, []),
        ("100", 0, ["1*0*0", "1*0+0", "1*0-0", "1+0*0", "1+0+0", "1+0-0", "1-0*0", "1-0+0", "1-0-0"]),
        ("123456789", 45, ["1+2+3+4+5+6+7+8*9", "1+2+3+4+5+6+78-9", "1+2+3+4+5+67-8+9", "1+2+3+4+56+7-8-9", "1+2+3+4-5+6+7+8*9", "1+2+3+4-5-6+78-9", "1+2+3-4+5+6+78-9", "1+2+3-4*5+6*7+8+9", "1+2-3*4+5+6+7*8+9", "1+2-3*4-5+6*7+8+9", "1-2+3*4+5+6+7*8+9", "1-2+3*4-5+6*7+8+9", "1-2-3*4+5+6+7*8+9", "1-2-3*4-5+6*7+8+9", "12+3+4+5-6-7+8-9", "12+3-4+5+6+7-8-9", "12-3-4+5+6-7-8+9", "123+45-67+8-9", "123+4-5+67-89", "123-45-67+89", "123-4-5-6-7+8-9"]),
    ]

    num_correct = 0
    for num, target, expected in test_cases:
        result = add_operators(num, target)
        result.sort()
        expected.sort()
        if result == expected:
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Input: num={num}, target={target}")
            print(f"Expected: {expected}")
            print(f"Got: {result}")

    print(f"{num_correct}/{len(test_cases)}")


if __name__ == "__main__":
    test_add_operators()