class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pruneTree(root):
    """
    Given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

    Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
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

    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()

    return result

def list_to_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        node = queue.pop(0)

        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1

    return root

def test_prune_tree():
    test_cases = [
        ([1,None,0,0,1], [1,None,0,None,1]),
        ([1,0,1,0,0,0,1], [1,None,1,None,1]),
        ([1,1,0,1,1,0,1,0], [1,1,0,1,1,None,1]),
        ([0], []),
        ([1], [1]),
        ([0, 0, 0], []),
        ([1, 0, 0], [1])
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for input_tree_list, expected_tree_list in test_cases:
        input_tree = list_to_tree(input_tree_list)
        expected_tree = list_to_tree(expected_tree_list)

        pruned_tree = pruneTree(input_tree)
        pruned_tree_list = tree_to_list(pruned_tree)
        expected_tree_list = tree_to_list(expected_tree)

        if pruned_tree_list == expected_tree_list:
            print("True")
            correct_tests += 1
        else:
            print("False")

    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    test_prune_tree()