import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Helper function to compare two trees for equality (used in testing)
    def __eq__(self, other):
        if not other or not isinstance(other, TreeNode):
            return False
        
        q1 = collections.deque([self])
        q2 = collections.deque([other])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False # Structure mismatch
            if node1.val != node2.val:
                return False # Value mismatch

            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
            
        # If both queues are empty, trees are equal
        return not q1 and not q2

# Function to build a tree from a list representation (level-order)
def list_to_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        current_node = queue.popleft()
        
        # Process left child
        if i < len(nodes) and nodes[i] is not None:
            left_child = TreeNode(nodes[i])
            current_node.left = left_child
            queue.append(left_child)
        i += 1
        
        # Process right child
        if i < len(nodes) and nodes[i] is not None:
            right_child = TreeNode(nodes[i])
            current_node.right = right_child
            queue.append(right_child)
        i += 1
        
    return root

# Function to convert a tree back to a list representation (level-order)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            # Important: Add children to queue even if None, 
            # to correctly represent the level structure,
            # but stop adding None children if all subsequent nodes are None
            if node.left or node.right or any(n is not None for n in queue):
                 queue.append(node.left)
                 queue.append(node.right)
            elif any(n is not None for n in queue): # Check if there are non-None nodes later in the queue
                 queue.append(node.left)
                 queue.append(node.right)

        else:
            result.append(None)

    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()
        
    return result
    
# --- Solution ---
def pruneTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Removes subtrees not containing a 1.
    Uses post-order traversal.
    """
    if not root:
        return None

    # Recursively prune left and right subtrees first (post-order)
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)

    # Check if the current node should be pruned
    # A node should be pruned if it's a 0 AND both its children were pruned (are None)
    if root.val == 0 and root.left is None and root.right is None:
        return None  # Prune this node by returning None to its parent
    else:
        return root # Keep this node

# --- Testing Framework ---
def run_tests():
    test_cases = [
        ([1,None,0,0,1], [1,None,0,None,1]),
        ([1,0,1,0,0,0,1], [1,None,1,None,1]),
        ([1,1,0,1,1,0,1,0], [1,1,0,1,1,None,1]),
        ([0], []), # Tree with only 0 root
        ([1], [1]), # Tree with only 1 root
        ([], []),   # Empty tree
        ([0,0,0], []), # Tree with only 0s
        ([0,None,1], [0,None,1]), # Root is 0 but right child is 1
        ([1,None,0], [1]), # Right child is 0 and has no children
        ([1,0,0,0,0,0,0], [1]), # Tree where only root is 1
        ([1,1,1], [1,1,1]), # Tree with only 1s
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_list, expected_list) in enumerate(test_cases):
        # Build input tree
        root_input = list_to_tree(input_list)
        
        # Build expected output tree (for potential tree comparison if needed)
        # root_expected = list_to_tree(expected_list) 

        # Run the function
        result_tree = pruneTree(root_input)

        # Convert result tree back to list for comparison
        result_list = tree_to_list(result_tree)

        # Compare result list with expected list
        passed = (result_list == expected_list)
        print(f"Test Case {i+1}: {passed}")
        if passed:
            correct_count += 1
        else:
            print(f"  Input:    {input_list}")
            print(f"  Expected: {expected_list}")
            print(f"  Got:      {result_list}")


    print(f"\nResult: {correct_count} / {total_tests} tests passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()