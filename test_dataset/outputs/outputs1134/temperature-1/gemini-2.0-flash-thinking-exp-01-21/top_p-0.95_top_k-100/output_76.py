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
        min_diff = min(min_diff, values[i] - values[i-1])
    return min_diff

def run_tests():
    test_cases = []

    # Test case 1
    root1 = TreeNode(1)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(2)
    test_cases.append({'root': root1, 'expected': 1})

    # Test case 2
    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    test_cases.append({'root': root2, 'expected': 1})

    # Test case 3: Only two nodes
    root3 = TreeNode(10)
    root3.right = TreeNode(22)
    test_cases.append({'root': root3, 'expected': 12})

    # Test case 4: Skewed tree
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    root4.right.right.right = TreeNode(4)
    test_cases.append({'root': root4, 'expected': 1})

    # Test case 5: More complex tree
    root5 = TreeNode(236)
    root5.left = TreeNode(104)
    root5.right = TreeNode(701)
    root5.left.right = TreeNode(227)
    root5.right.right = TreeNode(911)
    test_cases.append({'root': root5, 'expected': 110})


    correct_tests = 0
    total_tests = len(test_cases)

    for i, case in enumerate(test_cases):
        result = getMinimumDifference(case['root'])
        if result == case['expected']:
            print(f'Test {i+1}: True')
            correct_tests += 1
        else:
            print(f'Test {i+1}: False')

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()