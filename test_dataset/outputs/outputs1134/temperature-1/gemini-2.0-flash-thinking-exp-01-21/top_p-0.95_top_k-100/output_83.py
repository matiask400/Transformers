class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

def sum_root_to_leaf(root):
    def dfs(node, current_val):
        if not node:
            return 0
        current_val = (current_val << 1) | node.val
        if not node.left and not node.right:
            return current_val
        left_sum = dfs(node.left, current_val)
        right_sum = dfs(node.right, current_val)
        return left_sum + right_sum

    return dfs(root, 0)

def solve():
    test_cases = [
        ([1,0,1,0,1,0,1], 22),
        ([0], 0),
        ([1], 1),
        ([1,1], 3),
        ([1,0], 2),
        ([1, None, 0], 2),
        ([1, None, 0, None, None, None, None], 2),
        ([1, 0, 1, None, None, 0, 1], 11)
    ]

    num_correct = 0
    for i, (input_tree_arr, expected_output) in enumerate(test_cases):
        root = build_tree(input_tree_arr)
        actual_output = sum_root_to_leaf(root)
        if actual_output == expected_output:
            print(f'Test {i+1}: True')
            num_correct += 1
        else:
            print(f'Test {i+1}: False')
    print(f'{num_correct}/{len(test_cases)}')

if __name__ == '__main__':
    solve()