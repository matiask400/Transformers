def evaluate_rpn(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 + operand2)
        elif token == '-':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 - operand2)
        elif token == '*':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 * operand2)
        elif token == '/':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(int(operand1 / operand2))
        else:
            stack.append(int(token))
    return stack[0]

def run_tests():
    test_cases = [
        {
            "input": ["2","1","+","3","*"],
            "expected_output": 9
        },
        {
            "input": ["4","13","5","/","+"],
            "expected_output": 6
        },
        {
            "input": ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
            "expected_output": 22
        },
        {
            "input": ["-2", "1", "+"],
            "expected_output": -1
        },
        {
            "input": ["3", "-4", "+"],
            "expected_output": -1
        },
        {
            "input": ["10", "2", "/"],
            "expected_output": 5
        },
        {
            "input": ["-10", "3", "/"],
            "expected_output": -3
        },
        {
            "input": ["10", "-3", "/"],
            "expected_output": -3
        },
        {
            "input": ["-10", "-3", "/"],
            "expected_output": 3
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_tokens = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = evaluate_rpn(input_tokens)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()