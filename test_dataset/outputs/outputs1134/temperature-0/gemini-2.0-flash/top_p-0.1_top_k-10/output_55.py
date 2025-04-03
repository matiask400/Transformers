def evaluate_rpn(tokens):
    """
    Evaluates the value of an arithmetic expression in Reverse Polish Notation.

    Args:
        tokens: A list of strings representing the RPN expression.

    Returns:
        The integer value of the expression.
    """
    stack = []
    for token in tokens:
        if token == "+":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 + operand2)
        elif token == "-":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 - operand2)
        elif token == "*":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 * operand2)
        elif token == "/":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(int(operand1 / operand2))  # Truncate towards zero
        else:
            stack.append(int(token))
    return stack[0]


def test_evaluate_rpn():
    """
    Tests the evaluate_rpn function with several test cases.
    """
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["1"], 1),
        (["-1", "1", "+"], 0),
        (["10", "5", "/"], 2),
        (["-10", "5", "/"], -2),
        (["0", "5", "/"], 0),
        (["3", "-4", "+"], -1)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for tokens, expected_output in test_cases:
        actual_output = evaluate_rpn(tokens)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {tokens}")
            print(f"Expected: {expected_output}")
            print(f"Actual: {actual_output}")

    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_evaluate_rpn()