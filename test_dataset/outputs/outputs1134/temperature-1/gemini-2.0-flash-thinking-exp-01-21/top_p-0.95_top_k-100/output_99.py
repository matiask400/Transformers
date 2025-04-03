class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree(s):
    if not s:
        return None

    def parse_tree(index):
        if index >= len(s):
            return None, index

        is_negative = False
        if s[index] == '-':
            is_negative = True
            index += 1

        val_str = ""
        while index < len(s) and s[index].isdigit():
            val_str += s[index]
            index += 1

        if not val_str:
            return None, index

        val = int(val_str)
        if is_negative:
            val = -val
        root = TreeNode(val)

        if index < len(s) and s[index] == '(':
            index += 1 # consume '('
            root.left, index = parse_tree(index)
            if index < len(s) and s[index] == ')':
                index += 1 # consume ')'
            else:
                return None, index # error in format

        if index < len(s) and s[index] == '(':
            index += 1 # consume '('
            root.right, index = parse_tree(index)
            if index < len(s) and s[index] == ')':
                index += 1 # consume ')'
            else:
                return None, index # error in format

        return root, index

    root, _ = parse_tree(0)
    return root

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def solve_and_test(s, expected_output):
    root = construct_binary_tree(s)
    output = level_order_traversal(root)
    if output == expected_output:
        print('True')
        return True
    else:
        print('False')
        return False

if __name__ == '__main__':
    test_cases = [
        {"input": "4(2(3)(1))(6(5))", "expected_output": [4, 2, 6, 3, 1, 5]},
        {"input": "4(2(3)(1))(6(5)(7))", "expected_output": [4, 2, 6, 3, 1, 5, 7]},
        {"input": "-4(2(3)(1))(6(5)(7))", "expected_output": [-4, 2, 6, 3, 1, 5, 7]},
        {"input": "1", "expected_output": [1]},
        {"input": "10", "expected_output": [10]},
        {"input": "1(2)", "expected_output": [1, 2]},
        {"input": "1()(2)", "expected_output": [1, 2]},
        {"input": "5(4(11(7)(2))()) (8() (13)(4()(1)))", "expected_output": [5, 4, 8, 11, 13, 4, 7, 2, 1]},
        {"input": "-1(0)", "expected_output": [-1, 0]},
        {"input": "0(-1)", "expected_output": [0, -1]},
        {"input": "-5(-4(-11(-7)(-2))())(-8()(-13)(-4()(1)))", "expected_output": [-5, -4, -8, -11, -13, -4, -7, -2, 1]}

    ]

    correct_tests = 0
    total_tests = len(test_cases)
    for test in test_cases:
        if solve_and_test(test["input"], test["expected_output"]):
            correct_tests += 1

    print(f"{correct_tests}/{total_tests}")