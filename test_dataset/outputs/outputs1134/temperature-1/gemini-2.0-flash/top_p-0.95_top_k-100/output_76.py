class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    """
    Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
    """
    values = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        values.append(node.val)
        inorder(node.right)

    inorder(root)
    min_diff = float('inf')
    for i in range(1, len(values)):
        min_diff = min(min_diff, values[i] - values[i-1])
    return min_diff

def test_getMinimumDifference():
    """
    Tests the getMinimumDifference function.
    """
    tests = []
    expected = []

    # Test case 1
    root1 = TreeNode(1)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(2)
    tests.append(root1)
    expected.append(1)

    # Test case 2
    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    tests.append(root2)
    expected.append(1)

    # Test case 3
    root3 = TreeNode(0)
    root3.right = TreeNode(2236)
    root3.right.left = TreeNode(1277)
    root3.right.right = TreeNode(2776)
    root3.right.left.left = TreeNode(519)
    tests.append(root3)
    expected.append(759)

    # Test case 4: Single branch
    root4 = TreeNode(236)
    root4.left = TreeNode(104)
    root4.left.left = TreeNode(227)
    root4.left.right = TreeNode(701)
    root4.left.left.right = TreeNode(911)
    tests.append(root4)
    expected.append(68)

    correct_count = 0
    for i in range(len(tests)):
        result = getMinimumDifference(tests[i])
        if result == expected[i]:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Test case {i+1} failed. Expected: {expected[i]}, Got: {result}")

    print(f"{correct_count}/{len(tests)}")

if __name__ == "__main__":
    test_getMinimumDifference()