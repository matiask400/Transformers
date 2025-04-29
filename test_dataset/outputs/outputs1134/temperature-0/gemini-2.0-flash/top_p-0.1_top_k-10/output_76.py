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
    Tests the getMinimumDifference function with various test cases.
    """
    test_cases = [
        (TreeNode(1, None, TreeNode(3, TreeNode(2))), 1),
        (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6)), 1),
        (TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49))), 1),
        (TreeNode(236, TreeNode(104, None, TreeNode(227)), TreeNode(701, None, TreeNode(911))), 9),
        (TreeNode(0, None, TreeNode(2236, TreeNode(1277), TreeNode(2776))), 541)
    ]
    
    num_correct = 0
    total_tests = len(test_cases)
    
    for i, (root, expected) in enumerate(test_cases):
        result = getMinimumDifference(root)
        if result == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")
    
    print(f"\n{num_correct}/{total_tests} correct")

if __name__ == "__main__":
    test_getMinimumDifference()