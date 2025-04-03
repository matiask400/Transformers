import sys

def solve():
    """
    Solves the Remove Outermost Parentheses problem.
    Reads input from stdin, computes the result, and prints it to stdout.
    """
    # This function is designed to be called if reading from stdin is needed.
    # For the current problem structure, we'll use the test framework directly.
    pass

def removeOuterParentheses(S: str) -> str:
    """
    Given a valid parentheses string S, removes the outermost parentheses
    of every primitive string in the primitive decomposition of S.

    Args:
        S: The input valid parentheses string.

    Returns:
        The modified string after removing outermost parentheses.
    """
    result_chars = []
    balance = 0
    for char in S:
        if char == '(':
            # Only append '(' if it's not the start of a primitive component
            if balance > 0:
                result_chars.append(char)
            balance += 1
        elif char == ')':
            balance -= 1
            # Only append ')' if it's not the end of a primitive component
            if balance > 0:
                result_chars.append(char)
    return "".join(result_chars)

def run_tests():
    """
    Runs predefined test cases against the removeOuterParentheses function.
    """
    test_cases = [
        ("(()())(())", "()()()"),
        ("(()())(())(()(()))", "()()()()(())"),
        ("()()", ""),
        ("()", ""),
        ("(())", "()"),
        ("((()))", "(())"),
        ("(()())", "()()"),
        ("", ""), # Edge case: empty string
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        result = removeOuterParentheses(input_str)
        passed = result == expected_output
        print(f"{passed}")
        if passed:
            correct_count += 1
        # Optional: Print details for failed tests
        # else:
        #     print(f"Test Case {i+1} Failed:")
        #     print(f"  Input:    '{input_str}'")
        #     print(f"  Expected: '{expected_output}'")
        #     print(f"  Got:      '{result}'")

    print(f"{correct_count}/{total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()