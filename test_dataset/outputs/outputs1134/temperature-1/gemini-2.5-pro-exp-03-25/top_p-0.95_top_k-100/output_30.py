import sys

def solve():
    """
    Solves the Remove Outermost Parentheses problem.
    Reads input from stdin, computes the result, and prints it to stdout.
    """
    # This function is not used in the final test structure, 
    # but might be useful for standalone execution or different testing setups.
    s = sys.stdin.readline().strip()
    print(removeOuterParentheses(s))

def removeOuterParentheses(S: str) -> str:
    """
    Given a valid parentheses string S, removes the outermost parentheses
    of every primitive string in its primitive decomposition.

    Args:
        S: The input valid parentheses string.

    Returns:
        The modified string after removing outermost parentheses.
    """
    result = []
    balance = 0
    
    for char in S:
        if char == '(':
            # If balance > 0, it means this '(' is not an outermost parenthesis
            # of a primitive component starting at this point.
            if balance > 0:
                result.append(char)
            balance += 1
        else: # char == ')'
            balance -= 1
            # If balance > 0, it means this ')' is not the outermost closing
            # parenthesis of the primitive component ending here.
            if balance > 0:
                result.append(char)
                
    return "".join(result)

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
        ("(()(()))", "()(())"),
        ("", ""), # Edge case: empty string
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = removeOuterParentheses(input_str)
        passed = actual_output == expected_output
        print(f"Test Case {i + 1}: {passed}")
        # Optional: Print details on failure
        # if not passed:
        #     print(f"  Input:    '{input_str}'")
        #     print(f"  Expected: '{expected_output}'")
        #     print(f"  Actual:   '{actual_output}'")
            
        if passed:
            correct_count += 1

    print(f"\nResult: {correct_count} / {total_tests} tests passed.")

# Main execution block
if __name__ == "__main__":
    # The problem asks for executable code that runs tests.
    # So, we call run_tests() directly.
    run_tests()
    # If you want to use solve() for custom input via stdin:
    # solve()