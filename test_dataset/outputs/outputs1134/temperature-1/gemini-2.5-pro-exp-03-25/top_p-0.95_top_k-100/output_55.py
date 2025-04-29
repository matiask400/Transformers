import math
import operator

def evalRPN(tokens: list[str]) -> int:
    """
    Evaluates the value of an arithmetic expression in Reverse Polish Notation.

    Args:
        tokens: A list of strings representing the RPN expression.

    Returns:
        The integer result of the evaluation.
    """
    stack = []
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        # Division needs special handling for truncation towards zero
        "/": lambda a, b: int(a / b) 
    }

    for token in tokens:
        if token in operators:
            # Pop the second operand first (right-hand side)
            operand2 = stack.pop()
            # Pop the first operand second (left-hand side)
            operand1 = stack.pop()
            # Perform the operation
            result = operators[token](operand1, operand2)
            # Push the result back onto the stack
            stack.append(result)
        else:
            # It's an operand, convert to int and push onto the stack
            stack.append(int(token))

    # The final result is the only element left on the stack
    return stack[0]

def run_tests():
    """
    Runs test cases against the evalRPN function and prints the results.
    """
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["3", "4", "+"], 7),
        (["5"], 5),
        (["18"], 18),
        (["4", "2", "/"], 2),
        (["4", "-2", "/"], -2),
        (["-4", "2", "/"], -2),
        (["-4", "-2", "/"], 2),
        (["5", "3", "-"], 2),
        (["3", "5", "-"], -2),
        (["1", "2", "+", "3", "4", "+", "*"], 21), # (1+2)*(3+4) = 3*7 = 21
        (["10", "2", "3", "*", "+"], 16), # 10 + (2*3) = 16
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (tokens, expected) in enumerate(test_cases):
        result = evalRPN(tokens)
        passed = result == expected
        print(f"Test Case {i + 1}: {passed}")
        if passed:
            correct_tests += 1
        # Optional: Print details on failure
        # else:
        #    print(f"  Input: {tokens}")
        #    print(f"  Expected: {expected}")
        #    print(f"  Got: {result}")


    print(f"\nResult: {correct_tests} / {total_tests} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()