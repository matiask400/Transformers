from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def construct_tree(s):
    def parse(s, index):
        if index[0] >= len(s):
            return None
        # Read the integer value
        sign = 1
        if s[index[0]] == '-':
            sign = -1
            index[0] += 1
        num = 0
        while index[0] < len(s) and s[index[0]].isdigit():
            num = num * 10 + int(s[index[0]])
            index[0] += 1
        node = TreeNode(sign * num)
        # Parse left child
        if index[0] < len(s) and s[index[0]] == '(':
            index[0] += 1  # skip '('
            node.left = parse(s, index)
            index[0] += 1  # skip ')'
        # Parse right child
        if index[0] < len(s) and s[index[0]] == '(':
            index[0] += 1  # skip '('
            node.right = parse(s, index)
            index[0] += 1  # skip ')'
        return node

    index = [0]
    return parse(s, index)

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return result

def run_tests():
    tests = [
        ("4(2(3)(1))(6(5))", [4,2,6,3,1,5]),
        ("4(2(3)(1))(6(5)(7))", [4,2,6,3,1,5,7]),
        ("-4(2(3)(1))(6(5)(7))", [-4,2,6,3,1,5,7]),
        ("", []),
        ("1", [1]),
        ("1(2)(3(4)(5))", [1,2,3,4,5]),
        ("10(20(30)(40))(50)", [10,20,50,30,40]),
        ("-1(-2)(-3(-4)(-5))", [-1,-2,-3,-4,-5]),
    ]
    correct = 0
    total = len(tests)
    for s, expected in tests:
        tree = construct_tree(s)
        output = level_order(tree)
        if output == expected:
            print('True')
            correct +=1
        else:
            print('False')
    print(f"{correct}/{total}")

run_tests()