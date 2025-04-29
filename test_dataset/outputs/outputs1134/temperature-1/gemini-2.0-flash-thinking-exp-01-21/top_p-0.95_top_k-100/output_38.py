class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_array(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    n = len(nodes)
    for i in range(n):
        if nodes[i]:
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2
            if left_child_index < n:
                nodes[i].left = nodes[left_child_index]
            if right_child_index < n:
                nodes[i].right = nodes[right_child_index]
    return nodes[0]

def tree_to_array(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

def contains_one(root):
    if not root:
        return False
    if root.val == 1:
        return True
    return contains_one(root.left) or contains_one(root.right)

def pruneTree(root):
    if not root:
        return None
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if root.val == 0 and root.left is None and root.right is None:
        return None
    if root.val == 0:
        if root.left is None and root.right is None:
            return None
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                if contains_one(root.right): return root
                else: return None
            elif root.right is None:
                if contains_one(root.left): return root
                else: return None
            else:
                if contains_one(root.left) or contains_one(root.right): return root
                else: return None
    return root

def pruneTree_optimized(root):
    if not root:
        return None
    root.left = pruneTree_optimized(root.left)
    root.right = pruneTree_optimized(root.right)
    if root.val == 0 and root.left is None and root.right is None:
        return None
    if root.val == 0:
        if root.left is None and root.right is None:
            return None
        elif root.left is None and root.right is not None:
             if contains_one(root.right): return root
             else: return None
        elif root.left is not None and root.right is None:
             if contains_one(root.left): return root
             else: return None
        elif root.left is not None and root.right is not None:
             if contains_one(root.left) or contains_one(root.right): return root
             else: return None
    return root

def pruneTree_recursive(root):
    if not root:
        return None
    root.left = pruneTree_recursive(root.left)
    root.right = pruneTree_recursive(root.right)
    if root.val == 0 and root.left is None and root.right is None:
        return None
    if root.val == 0:
        if root.left is None and root.right is None:
            return None
        else:
            has_one = False
            if root.left and contains_one(root.left): has_one = True
            if root.right and contains_one(root.right): has_one = True
            if not has_one: return None
            else: return root
    return root

def pruneTree_final(root):
    if not root:
        return None

    root.left = pruneTree_final(root.left)
    root.right = pruneTree_final(root.right)

    if root.val == 0 and root.left is None and root.right is None:
        return None
    return root

def pruneTree_final_and_contains_one(root):
    if not root:
        return False, None

    left_contains_one, root.left = pruneTree_final_and_contains_one(root.left)
    right_contains_one, root.right = pruneTree_final_and_contains_one(root.right)

    current_contains_one = (root.val == 1) or left_contains_one or right_contains_one
    if root.val == 0 and not current_contains_one:
        return False, None
    return current_contains_one, root

def pruneTree_best(root):
    contains_one_val, pruned_root = pruneTree_final_and_contains_one(root)
    return pruned_root


def solve():
    test_cases = [
        ([1, None, 0, 0, 1], [1, None, 0, None, 1]),
        ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
        ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]),
        ([0, 0, 0], []),
        ([0, None, 1], [0, None, 1]),
        ([1, 0, 0], [1])
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for input_tree_arr, expected_tree_arr in test_cases:
        root = build_tree_from_array(input_tree_arr)
        result_root = pruneTree_best(root)
        result_arr = tree_to_array(result_root)
        if result_arr == expected_tree_arr:
            print('True')
            correct_tests += 1
        else:
            print('False')

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    solve()