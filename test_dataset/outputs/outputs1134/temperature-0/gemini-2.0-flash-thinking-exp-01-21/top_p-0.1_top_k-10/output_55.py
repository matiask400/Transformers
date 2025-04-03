def evalRPN(tokens):
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
            if operand2 == 0:
                raise ZeroDivisionError("Division by zero")
            stack.append(int(operand1 / operand2))
        else:
            stack.append(int(token))
    return stack[0]

def run_tests():
    test_cases = [
        {
            "tokens": ["2","1","+","3","*"],
            "expected": 9
        },
        {
            "tokens": ["4","13","5","/","+"],
            "expected": 6
        },
        {
            "tokens": ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
            "expected": 22
        },
        {
            "tokens": ["-1", "-1", "+"],
            "expected": -2
        },
        {
            "tokens": ["10", "2", "/"],
            "expected": 5
        },
        {
            "tokens": ["-10", "2", "/"],
            "expected": -5
        },
        {
            "tokens": ["10", "-2", "/"],
            "expected": -5
        },
        {
            "tokens": ["-10", "-2", "/"],
            "expected": 5
        }
    ]

    num_correct = 0
    for i, test_case in enumerate(test_cases):
        tokens = test_case["tokens"]
        expected_output = test_case["expected"]
        actual_output = evalRPN(tokens)
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            num_correct += 1
        else:
            print(f'Test {i+1}: False')
    print(f'{num_correct}/{len(test_cases)}')

if __name__ == '__main__':
    run_tests()