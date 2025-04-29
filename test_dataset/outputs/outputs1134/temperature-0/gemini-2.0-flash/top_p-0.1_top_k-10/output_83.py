class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root):
    def dfs(node, current_number):
        if not node:
            return 0

        current_number = (current_number << 1) | node.val

        if not node.left and not node.right:
            return current_number

        return dfs(node.left, current_number) + dfs(node.right, current_number)

    return dfs(root, 0)

def test_sumRootToLeaf():
    test_cases = [
        (TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1))), 22),
        (TreeNode(0), 0),
        (TreeNode(1), 1),
        (TreeNode(1, TreeNode(1)), 3),
        (TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)))), 21)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (root, expected) in enumerate(test_cases):
        result = sumRootToLeaf(root)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_sumRootToLeaf()