class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    def inorder_traversal(node, values):
        if not node:
            return
        inorder_traversal(node.left, values)
        values.append(node.val)
        inorder_traversal(node.right, values)

    values = []
    inorder_traversal(root, values)

    min_diff = float('inf')
    for i in range(1, len(values)):
        diff = abs(values[i] - values[i-1])
        min_diff = min(min_diff, diff)

    return min_diff

def run_tests():
    test_cases = [
        {
            "input": TreeNode(1, None, TreeNode(3, TreeNode(2), None)),
            "expected": 1
        },
        {
            "input": TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6)),
            "expected": 1
        },
        {
            "input": TreeNode(236, TreeNode(104, None, TreeNode(227)), TreeNode(701, None, TreeNode(911))),
            "expected": 9
        },
        {
            "input": TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49))),
            "expected": 1
        },
        {
            "input": TreeNode(27,None,TreeNode(34,TreeNode(58,TreeNode(50,TreeNode(44),None),None),TreeNode(35,None,TreeNode(42,TreeNode(15),None)))),
            "expected": 1
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        input_tree = test_case["input"]
        expected_output = test_case["expected"]
        actual_output = getMinimumDifference(input_tree)
        if actual_output == expected_output:
            print(True)
            correct_tests += 1
        else:
            print(False)

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()