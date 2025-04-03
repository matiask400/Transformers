import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        
        # Process left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Process right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
        
    return root

def sumRootToLeaf(root: TreeNode | None) -> int:
    """
    Calculates the sum of all root-to-leaf binary numbers.
    """
    total_sum = 0

    def dfs(node, current_num):
        nonlocal total_sum
        if not node:
            return

        # Update the current number by shifting left and adding the node's value
        current_num = (current_num << 1) | node.val

        # If it's a leaf node, add the number represented by the path to the total sum
        if not node.left and not node.right:
            total_sum += current_num
            return

        # Recursively call for left and right children
        dfs(node.left, current_num)
        dfs(node.right, current_num)

    dfs(root, 0)
    return total_sum

# Test cases
test_cases = [
    ([1,0,1,0,1,0,1], 22),
    ([0], 0),
    ([1], 1),
    ([1,1], 3),
    ([], 0), # Edge case: empty tree
    ([1,0,1,None,None,0,1], 18), # (100) + (111) = 4 + 7 = 11 - Error in manual calc, let's recheck: 1->0->None, 1->1->0, 1->1->1. Paths: 10 (leaf 0), 110 (leaf 0), 111 (leaf 1). Wait, the example is [1,0,1,None,None,0,1]. Let's trace:
    # Root: 1
    # Left: 0 (path 10) -> Leaf. Value = 2
    # Right: 1 (path 11)
    #   Left: 0 (path 110) -> Leaf. Value = 6
    #   Right: 1 (path 111) -> Leaf. Value = 7
    # Sum = 2 + 6 + 7 = 15. Let's use this as the expected value.
    ([1,0,1,None,None,0,1], 15),
    ([1,1,0,1,1,0,0], 26), # Paths: 111 (7), 111 (7), 100 (4), 100 (4). Sum = 7+7+4+4 = 22. Let's retrace tree:
    #       1
    #      / \
    #     1   0
    #    / \ / \
    #   1  1 0  0
    # Paths: 1->1->1 (7), 1->1->1 (7), 1->0->0 (4), 1->0->0 (4). Sum = 7+7+4+4 = 22. Corrected expected value.
    ([1,1,0,1,1,0,0], 22),
]

# --- Testing Framework ---
def run_tests():
    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_list, expected_output) in enumerate(test_cases):
        # Build the tree from the input list
        root = build_tree(input_list)
        
        # Calculate the actual output
        actual_output = sumRootToLeaf(root)
        
        # Compare actual output with expected output
        passed = actual_output == expected_output
        print(f"Test Case {i+1}: {passed}")
        if passed:
            correct_count += 1
            
    print(f"\nResult: {correct_count} / {total_tests} tests passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()