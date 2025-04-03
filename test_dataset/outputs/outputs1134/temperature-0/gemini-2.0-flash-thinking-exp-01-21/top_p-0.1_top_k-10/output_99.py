class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_tree(s):
    if not s:
        return None

    val_str = ""
    i = 0
    if s[0] == '-':
        val_str += '-'
        i += 1
    while i < len(s) and s[i].isdigit():
        val_str += s[i]
        i += 1

    root = TreeNode(int(val_str))

    balance = 0
    start_index = -1
    subtree_count = 0

    for j in range(i, len(s)):
        if s[j] == '(':
            if balance == 0:
                start_index = j
            balance += 1
        elif s[j] == ')':
            balance -= 1
            if balance == 0 and start_index != -1:
                subtree_str = s[start_index+1:j]
                subtree_count += 1
                if subtree_count == 1:
                    root.left = construct_tree(subtree_str)
                elif subtree_count == 2:
                    root.right = construct_tree(subtree_str)
                start_index = -1
    return root

def level_order(root):
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

def test_cases():
    test_inputs = [
        "4(2(3)(1))(6(5))",
        "4(2(3)(1))(6(5)(7))",
        "-4(2(3)(1))(6(5)(7))",
        "1",
        "1()",
        "1()()",
        "1(())",
        "1(()())",
        "1((()))",
        "1(2)",
        "1(2)(3)",
        "1(2(4))(3(5))",
        "5(4(11(7)(2)))(8(13)(4()(1)))"
    ]
    expected_outputs = [
        [4, 2, 6, 3, 1, 5],
        [4, 2, 6, 3, 1, 5, 7],
        [-4, 2, 6, 3, 1, 5, 7],
        [1],
        [1],
        [1],
        [1, 2],
        [1, 2],
        [1, 2],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 8, 11, 13, 4, 7, 2, 1]
    ]

    correct_count = 0
    for i in range(len(test_inputs)):
        root = construct_tree(test_inputs[i])
        output = level_order(root)
        if output == expected_outputs[i]:
            print('True')
            correct_count += 1
        else:
            print('False')
    print(f"{correct_count}/{len(test_inputs)}")

if __name__ == '__main__':
    test_cases()