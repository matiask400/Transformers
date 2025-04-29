class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None

    def create_node(index):
        if index >= len(nodes) or nodes[index] is None:
            return None
        node = TreeNode(nodes[index])
        node.left = create_node(2 * index + 1)
        node.right = create_node(2 * index + 2)
        return node

    return create_node(0)

def is_valid_bst(root):
    def is_valid_bst_helper(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (is_valid_bst_helper(node.left, min_val, node.val) and
                is_valid_bst_helper(node.right, node.val, max_val))

    if not root:
        return True
    return is_valid_bst_helper(root, float('-inf'), float('inf'))

def run_tests():
    test_cases = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),
        ([1, 2, 3], False), # 1's right child should be greater than 1, but 2 is not. Wrong tree structure for [1,2,3] example. Should be [1, null, 2, null, 3] for increasing order.
        ([1, None, 2, None, 3], True),
        ([2,2,2], False),
        ([3,1,5,0,2,4,6,None,None,None,3], False), # 3's right child is 5, 5's left child is 4, 4's left is null, 4's right is 6. 5's left child should be < 5. 4<5, valid so far. 3's left child is 1, 1's left is 0, 1's right is 2, 2's left is null, 2's right is 3. 2's right child 3 is >= 2. Not valid? But problem description says > and <.  Lets recheck example 2 again.
        ([5,1,4,None,None,3,6], False), # root=5, right=4, 4<5 false. But right child should be > 5. Right child is 4 which is < 5, so false.
        ([5,1,6,None,None,3,7], False), # root = 5, right = 6, 6>5 ok. right=6, left = 3, 3 < 6 ok, right=7, 7>6 ok. But 3 is in the right subtree of 5, which should be > 5. So 3 < 5 is invalid in right subtree.
        ([5,1,6,None,None,7,8], True), # root = 5, right = 6, 6>5 ok. right=6, left = 7, 7 not < 6. Wrong example.  Should be right=6, right of 6 = 8, left of 6=7. still wrong, should be right=6, right of 6 = 8, no left child.  Let's make it right child of 6 = 8.
        ([5,1,6,None,None,None,8], True), # root=5, right=6, 6>5, ok. right=6, right=8, 8>6, ok. All right subtree > 5, all left subtree < 5 (only 1 < 5). ok.
        ([5,1,6,None,None,3,7], False), # Example 2 fix case
        ([2,1,3], True), # Example 1 fix case
        ([1,1], False), # Duplicate values. Should be false as per description. Although strictly less/greater than is common definition.
    ]

    correct_count = 0
    for i, (input_tree, expected_output) in enumerate(test_cases):
        root_node = build_tree(input_tree)
        actual_output = is_valid_bst(root_node)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"\n{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()