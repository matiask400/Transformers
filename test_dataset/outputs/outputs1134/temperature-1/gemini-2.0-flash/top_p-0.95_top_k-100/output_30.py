def remove_outer_parentheses(S):
    """
    Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
    Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

    Args:
        S (str): A valid parentheses string.

    Returns:
        str: The modified string after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
    """
    result = ""
    open_count = 0
    for char in S:
        if char == '(':
            if open_count > 0:
                result += char
            open_count += 1
        elif char == ')':
            open_count -= 1
            if open_count > 0:
                result += char
    return result

def test_remove_outer_parentheses():
    test_cases = [
        {"input": "(()())(())", "expected": "()()()"},
        {"input": "(()())(())(()(()))", "expected": "()()()()(())"},
        {"input": "()()", "expected": ""},
        {"input": "((()))", "expected": "()()"},
        {"input": "()", "expected": ""}
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_str = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = remove_outer_parentheses(input_str)

        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {input_str}, Expected: {expected_output}, Actual: {actual_output})")

    print(f"\nCorrect: {correct_count} / {total_count}")

if __name__ == "__main__":
    test_remove_outer_parentheses()