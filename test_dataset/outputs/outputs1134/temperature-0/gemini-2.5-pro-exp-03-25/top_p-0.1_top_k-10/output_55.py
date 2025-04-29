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
        # Use a lambda for division to handle truncation towards zero
        "/": lambda a, b: int(a / b) 
    }

    for token in tokens:
        if token in operators:
            # Pop the top two operands
            # Note: The second operand popped (operand1) comes before 
            # the first operand popped (operand2) in the original expression
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Perform the operation
            operation = operators[token]
            result = operation(operand1, operand2)
            
            # Push the result back onto the stack
            stack.append(result)
        else:
            # If it's not an operator, it must be an operand (number)
            stack.append(int(token))

    # The final result is the only element left on the stack
    return stack[0]

# --- Testing Framework ---
def run_tests():
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["3", "4", "+"], 7),
        (["5", "1", "2", "+", "4", "*", "+", "3", "-"], 14), # (5 + ((1 + 2) * 4)) - 3 = (5 + (3 * 4)) - 3 = (5 + 12) - 3 = 17 - 3 = 14
        (["4", "3", "-"], 1), # 4 - 3
        (["10", "2", "/"], 5), # 10 / 2
        (["10", "3", "/"], 3), # 10 / 3 truncates to 3
        (["-10", "3", "/"], -3), # -10 / 3 truncates towards zero to -3
        (["10", "-3", "/"], -3), # 10 / -3 truncates towards zero to -3
        (["-10", "-3", "/"], 3), # -10 / -3 truncates towards zero to 3
        (["5"], 5), # Single number
        (["-1"], -1), # Single negative number
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (tokens, expected) in enumerate(test_cases):
        result = evalRPN(tokens.copy()) # Pass a copy to avoid modifying original test case list if needed
        passed = result == expected
        print(f"Test {i+1}: {passed}")
        if passed:
            correct_count += 1
        # Optional: Print details on failure
        # else:
        #     print(f"  Input: {tokens}")
        #     print(f"  Expected: {expected}")
        #     print(f"  Got: {result}")


    print(f"\n{correct_count}/{total_tests} tests passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()