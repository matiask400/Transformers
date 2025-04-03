class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestKValues(root, target, k):
    """
    Finds the k values in the BST that are closest to the target.

    Args:
        root: The root of the binary search tree.
        target: The target value.
        k: The number of values to return.

    Returns:
        A list of the k values in the BST that are closest to the target.
    """

    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    inorder_list = inorder(root)
    closest_values = sorted(inorder_list, key=lambda x: abs(x - target))[:k]
    return closest_values

def test_closestKValues():
    test_cases = [
        (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)), 3.714286, 2, [4, 3]),
        (TreeNode(1), 0.000000, 1, [1]),
        (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)), 3, 2, [3, 2]),
        (TreeNode(10, TreeNode(5, TreeNode(2, TreeNode(1), None), TreeNode(6)), TreeNode(15, None, TreeNode(20))), 13, 3, [15, 10, 20]),
    ]

    num_correct = 0
    for i, (root, target, k, expected) in enumerate(test_cases):
        result = closestKValues(root, target, k)
        result.sort()
        expected.sort()
        if result == expected:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: root={root}, target={target}, k={k}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    print(f"\n{num_correct} / {len(test_cases)}")

if __name__ == "__main__":
    test_closestKValues()