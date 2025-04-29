def evaluate_rpn(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                res = a + b
            elif token == '-':
                res = a - b
            elif token == '*':
                res = a * b
            elif token == '/':
                res = int(a / b)
            stack.append(res)
        else:
            stack.append(int(token))
    return stack.pop()

def run_tests():
    test_cases = [
        (["2","1","+","3","*"], 9),
        (["4","13","5","/","+"], 6),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
        (["3","-4","+"], -1),
        (["5"], 5),
        (["-3","-4","*"], 12),
        (["7","2","/"], 3),
        (["7","-2","/"], -3),
        (["0","3","/"], 0)
    ]
    correct = 0
    total = len(test_cases)
    for tokens, expected in test_cases:
        result = evaluate_rpn(tokens)
        if result == expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()