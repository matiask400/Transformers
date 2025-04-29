class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pruneTree(root):
    """
    Prunes a binary tree such that any subtree not containing a 1 is removed.

    Args:
        root: The root node of the binary tree.

    Returns:
        The root node of the pruned binary tree.
    """

    def contains_one(node):
        if not node:
            return False

        left_contains_one = contains_one(node.left)
        right_contains_one = contains_one(node.right)

        if not left_contains_one:
            node.left = None
        if not right_contains_one:
            node.right = None

        return node.val == 1 or left_contains_one or right_contains_one

    if not contains_one(root):
        return None
    return root

def tree_to_list(root):
    """
    Converts a binary tree to a list representation (level-order traversal).
    Uses None to represent null nodes.
    """
    if not root:
        return []

    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result

def list_to_tree(lst):
    """
    Converts a list representation (level-order traversal) to a binary tree.
    None values in the list represent null nodes.
    """
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1

    return root

def test_pruneTree():
    test_cases = [
        ([1, None, 0, 0, 1], [1, None, 0, None, 1]),
        ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
        ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]),
        ([0], []),
        ([1], [1]),
        ([0,0,0], []),
        ([1,0,0], [1]),
        ([0,1,0], [None, 1]),
        ([0,0,1], [None, None, 1])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_tree_list, expected_tree_list in test_cases:
        input_tree = list_to_tree(input_tree_list)
        pruned_tree = pruneTree(input_tree)
        actual_tree_list = tree_to_list(pruned_tree)

        if actual_tree_list == expected_tree_list:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_pruneTree()