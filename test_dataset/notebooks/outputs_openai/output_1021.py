def remove_outer_parentheses(S: str) -> str:
    result = []
    depth = 0
    for char in S:
        if char == '(':
            if depth > 0:
                result.append(char)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                result.append(char)
    return ''.join(result)

def run_tests():
    tests = [
        ("(()())(())", "()()()"),
        ("(()())(())(()(()))", "()()()()(())"),
        ("()()", "")
    ]
    correct = 0
    total = len(tests)
    for i, (input_str, expected) in enumerate(tests, 1):
        output = remove_outer_parentheses(input_str)
        is_correct = output == expected
        print(is_correct)
        if is_correct:
            correct += 1
    print(f"{correct}/{total}")

run_tests()