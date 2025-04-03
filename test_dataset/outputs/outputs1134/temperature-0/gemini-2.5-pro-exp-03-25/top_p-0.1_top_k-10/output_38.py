import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        """Overrides the default implementation"""
        if not isinstance(other, TreeNode):
            return NotImplemented
        # This comparison is basic and might not be sufficient for all tree equality needs,
        # especially if node order matters differently or structure is complex.
        # For this problem, comparing the list representation is more robust.
        return self.to_list() == other.to_list()

    def to_list(self):
        """Converts the tree to a list representation (level-order)."""
        if not self:
            return []
        
        nodes_list = []
        q = collections.deque([self])
        while q:
            node = q.popleft()
            if node:
                nodes_list.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                # We add None for null nodes encountered during traversal
                # but will trim trailing Nones later.
                nodes_list.append(None)

        # Trim trailing Nones
        while nodes_list and nodes_list[-1] is None:
            nodes_list.pop()
            
        return nodes_list

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a list representation (level-order)."""
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

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Removes subtrees not containing a 1.
        Uses a post-order traversal approach.
        """
        if not root:
            return None

        # Recursively prune the left and right subtrees first.
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # After pruning children, check if the current node should be pruned.
        # A node should be pruned if it's a 0 and both its children are None (or were pruned).
        if root.val == 0 and root.left is None and root.right is None:
            return None  # Prune this node by returning None
        else:
            return root  # Keep this node

# --- Testing Framework ---

def run_tests():
    """Runs test cases against the Solution."""
    solver = Solution()
    
    test_cases = [
        # Input list, Expected output list
        ([1,None,0,0,1], [1,None,0,None,1]),
        ([1,0,1,0,0,0,1], [1,None,1,None,1]),
        ([1,1,0,1,1,0,1,0], [1,1,0,1,1,None,1]),
        ([0,None,0,0,0], []), # Tree with only 0s should become empty
        ([1], [1]),
        ([0], []),
        ([], []),
        ([1,0,0,0,0], [1]),
        ([1,1,1,1,1], [1,1,1,1,1]),
        ([0,0,0,0,1], [0,None,0,None,1]), # Root 0 kept because right subtree has 1
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_list, expected_list) in enumerate(test_cases):
        # Build input tree
        input_tree = build_tree(input_list)
        
        # Get the result from the pruneTree function
        result_tree = solver.pruneTree(input_tree)
        
        # Convert result tree to list for comparison
        result_list = result_tree.to_list() if result_tree else []

        # Compare result list with expected list
        passed = (result_list == expected_list)
        print(f"Test Case {i+1}: {passed}")
        if passed:
            correct_count += 1
        else:
            # Optional: Print details on failure
            print(f"  Input:    {input_list}")
            print(f"  Expected: {expected_list}")
            print(f"  Got:      {result_list}")


    print(f"\nResult: {correct_count} / {total_tests} tests passed.")

# Execute the tests
if __name__ == "__main__":
    # Add helper methods to TreeNode for testing convenience
    TreeNode.to_list = TreeNode.to_list 
    run_tests()