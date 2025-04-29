def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 + num2)
        elif token == "-":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 - num2)
        elif token == "*":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 * num2)
        elif token == "/":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(int(num1 / num2))
        else:
            stack.append(int(token))
    return stack[0]

def test_evalRPN():
    tests = [
        (["2","1","+","3","*"], 9),
        (["4","13","5","/","+"], 6),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
        (["1"], 1),
        (["-10", "2", "+"], -8),
        (["-3", "4", "+"], 1),
        (["3","-4","+"], -1)
    ]
    
    correct_count = 0
    total_count = len(tests)
    
    for i, (tokens, expected) in enumerate(tests):
        result = evalRPN(tokens)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
    
    print(f"{correct_count}/{total_count}")

test_evalRPN()