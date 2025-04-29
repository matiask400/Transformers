class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def distanceK(root, target, K):
    """
    Finds nodes that are distance K from the target node in a binary tree.

    Args:
        root: The root of the binary tree (TreeNode).
        target: The target node (TreeNode).
        K: The distance (integer).

    Returns:
        A list of values of nodes that are distance K from the target node.
    """
    parent_map = {}
    def build_parent_map(node, parent):
        if node:
            parent_map[node] = parent
            build_parent_map(node.left, node)
            build_parent_map(node.right, node)

    build_parent_map(root, None)

    queue = [(target, 0)]
    visited = {target}
    result = []

    while queue:
        current_node, distance = queue.pop(0)

        if distance == K:
            result.append(current_node.val)
        elif distance < K:
            # Explore children
            if current_node.left and current_node.left not in visited:
                visited.add(current_node.left)
                queue.append((current_node.left, distance + 1))
            if current_node.right and current_node.right not in visited:
                visited.add(current_node.right)
                queue.append((current_node.right, distance + 1))
            # Explore parent
            parent = parent_map.get(current_node)
            if parent and parent not in visited:
                visited.add(parent)
                queue.append((parent, distance + 1))
    return result


def create_tree_from_list(values):
    """
    Creates a binary tree from a list of values (level order traversal with null).
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current_node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            current_node.left = TreeNode(values[i])
            queue.append(current_node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current_node.right = TreeNode(values[i])
            queue.append(current_node.right)
        i += 1
    return root

def find_node(root, target_val):
    """
    Finds a node in the tree with the given target value.
    """
    if not root:
        return None
    if root.val == target_val:
        return root
    left_search = find_node(root.left, target_val)
    if left_search:
        return left_search
    return find_node(root.right, target_val)


def run_test(root_values, target_val, K, expected_output):
    """
    Runs a test case and prints True if passed, False otherwise.
    """
    root_node = create_tree_from_list(root_values)
    target_node = find_node(root_node, target_val)
    if not target_node:
        print(f"False - Target node with value {target_val} not found in tree.")
        return False

    actual_output = distanceK(root_node, target_node, K)
    actual_output.sort()
    expected_output.sort()

    if actual_output == expected_output:
        print('True')
        return True
    else:
        print('False')
        print(f"  Expected: {expected_output}")
        print(f"  Actual:   {actual_output}")
        return False


def test_distanceK():
    correct_tests = 0
    total_tests = 0

    # Example 1
    total_tests += 1
    if run_test([3,5,1,6,2,0,8,None,None,7,4], 5, 2, [7, 4, 1]):
        correct_tests += 1

    # Example 2: K = 3
    total_tests += 1
    if run_test([3,5,1,6,2,0,8,None,None,7,4], 5, 3, [6, 0, 8]):
        correct_tests += 1

    # Example 3: K = 0
    total_tests += 1
    if run_test([3,5,1,6,2,0,8,None,None,7,4], 5, 0, [5]):
        correct_tests += 1

    # Example 4: K = 1
    total_tests += 1
    if run_test([3,5,1,6,2,0,8,None,None,7,4], 5, 1, [6, 2, 3]):
        correct_tests += 1

    # Example 5: Target is root, K = 1
    total_tests += 1
    if run_test([3,5,1,6,2,0,8,None,None,7,4], 3, 1, [5, 1]):
        correct_tests += 1

    # Example 6: Target is leaf, K = 1
    total_tests += 1
    if run_test([3,5,1,6,2,0,8,None,None,7,4], 6, 1, [5]):
        correct_tests += 1

    # Example 7: Target is leaf, K = 2
    total_tests += 1
    if run_test([3,5,1,6,2,0,8,None,None,7,4], 6, 2, [3,2]):
        correct_tests += 1

    # Example 8: Target is leaf, K = 3
    total_tests += 1
    if run_test([3,5,1,6,2,0,8,None,None,7,4], 6, 3, [1]):
        correct_tests += 1

    # Example 9: Linear Tree, K = 2
    total_tests += 1
    if run_test([1, 2, None, 3, None, 4, None, 5], 3, 2, [1, 5]):
        correct_tests += 1

    # Example 10: Linear Tree, K = 3
    total_tests += 1
    if run_test([1, 2, None, 3, None, 4, None, 5], 3, 3, []):
        correct_tests += 1

    # Example 11: Single node tree
    total_tests += 1
    if run_test([0], 0, 0, [0]):
        correct_tests += 1

    # Example 12: Single node tree, K=1
    total_tests += 1
    if run_test([0], 0, 1, []):
        correct_tests += 1


    print(f"Correct tests: {correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_distanceK()