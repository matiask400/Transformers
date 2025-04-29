def remove_outer_parentheses(S):
    """
    Removes the outermost parentheses of every primitive string in the primitive decomposition of S.

    Args:
        S: A valid parentheses string.

    Returns:
        S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
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
    """
    Tests the remove_outer_parentheses function with several test cases.
    """
    test_cases = [
        ("(()())(())", "()()()"),
        ("(()())(())(()(()))", "()()()()(())"),
        ("()()", ""),
        ("((()))", "()()"),
        ("()", "")
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_str, expected_output in test_cases:
        actual_output = remove_outer_parentheses(input_str)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_remove_outer_parentheses()