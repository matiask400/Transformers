def remove_outer_parentheses_primitive_decomposition(s):
    def get_primitive_decomposition(s):
        primitives = []
        balance = 0
        start_index = 0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            elif s[i] == ')':
                balance -= 1
            if balance == 0:
                primitives.append(s[start_index:i+1])
                start_index = i + 1
        return primitives

    def remove_outer_parentheses(primitive_s):
        if len(primitive_s) >= 2 and primitive_s[0] == '(' and primitive_s[-1] == ')':
            return primitive_s[1:-1]
        return primitive_s

    primitive_strings = get_primitive_decomposition(s)
    result_parts = []
    for primitive_s in primitive_strings:
        result_parts.append(remove_outer_parentheses(primitive_s))
    return "".join(result_parts)

def run_tests():
    test_cases = [
        {
            "input": "(()())(())",
            "expected_output": "()()()"
        },
        {
            "input": "(()())(())(()(()))",
            "expected_output": "()()()()(())"
        },
        {
            "input": "()()",
            "expected_output": ""
        },
        {
            "input": "()",
            "expected_output": ""
        },
        {
            "input": "(())",
            "expected_output": "()"
        },
        {
            "input": "((()))",
            "expected_output": "(())"
        },
        {
            "input": "(((())))",
            "expected_output": "((()))"
        },
        {
            "input": "(())(())",
            "expected_output": "()()"
        },
        {
            "input": "(()())",
            "expected_output": "()()"
        }
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        input_s = test_case["input"]
        expected_output = test_case["expected_output"]
        actual_output = remove_outer_parentheses_primitive_decomposition(input_s)
        if actual_output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()