def add_operators(num, target):
    def helper(index, current_expression, current_value, previous_operand):
        if index == len(num):
            if current_value == target:
                result.append(current_expression)
            return

        for i in range(index, len(num)):
            if i > index and num[index] == '0':
                break
            current_num = int(num[index:i + 1])

            if index == 0:
                helper(i + 1, str(current_num), current_num, current_num)
            else:
                helper(i + 1, current_expression + "+" + str(current_num), current_value + current_num, current_num)
                helper(i + 1, current_expression + "-" + str(current_num), current_value - current_num, -current_num)
                helper(i + 1, current_expression + "*" + str(current_num), current_value - previous_operand + previous_operand * current_num, previous_operand * current_num)

    result = []
    helper(0, "", 0, 0)
    return result


def test_add_operators():
    test_cases = [
        {"num": "123", "target": 6, "expected": ["1*2*3", "1+2+3"]},
        {"num": "232", "target": 8, "expected": ["2*3+2", "2+3*2"]},
        {"num": "105", "target": 5, "expected": ["1*0+5", "10-5"]},
        {"num": "00", "target": 0, "expected": ["0*0", "0+0", "0-0"]},
        {"num": "3456237490", "target": 9191, "expected": []},
        {"num": "10", "target": 5, "expected": []},
        {"num": "10", "target": 10, "expected": ["10"]},
        {"num": "1", "target": 1, "expected": ["1"]},
        {"num": "105", "target": 5, "expected": ["1*0+5", "10-5"]},
        {"num": "2147483647", "target": 2147483647, "expected": ["2147483647"]}
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test in enumerate(test_cases):
        num = test["num"]
        target = test["target"]
        expected = set(test["expected"])  # Convert expected to a set for easier comparison
        actual = set(add_operators(num, target))

        if actual == expected:
            print(f"True")
            correct_count += 1
        else:
            print(f"False")
            print(f"Test case {i+1} failed:")
            print(f"Input: num = {num}, target = {target}")
            print(f"Expected: {expected}")
            print(f"Actual: {actual}")

    print(f"{correct_count}/{total_count}")


if __name__ == '__main__':
    test_add_operators()