import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Helper for debugging tree structure (level-order)
        if not self:
            return "[]"
        nodes = []
        q = collections.deque([self])
        while q:
            curr = q.popleft()
            if curr:
                nodes.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                # Only add null if there are more nodes to process potentially
                # This avoids trailing nulls in the representation
                 if any(node is not None for node in q):
                     nodes.append("null")
                 elif nodes and nodes[-1] != "null": # Avoid adding null if last was already null
                     nodes.append("null")


        # Trim trailing nulls for cleaner representation
        while nodes and nodes[-1] == "null":
            nodes.pop()
        return "[" + ",".join(nodes) + "]"


# Function to build a tree from a list (level-order traversal with nulls)
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a list representation."""
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
    """
    Implements the solution to check if a binary tree is a valid BST.
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if the given binary tree is a valid Binary Search Tree (BST).

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is a valid BST, False otherwise.
        """
        # Use float('-inf') and float('inf') for initial bounds
        # as node values can be Integer.MIN_VALUE or Integer.MAX_VALUE
        return self._isValidBSTHelper(root, float('-inf'), float('inf'))

    def _isValidBSTHelper(self, node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        """
        Recursive helper function to validate the BST property within a given range.

        Args:
            node: The current node being checked.
            min_val: The minimum allowed value for this node (exclusive lower bound).
            max_val: The maximum allowed value for this node (exclusive upper bound).

        Returns:
            True if the subtree rooted at 'node' is a valid BST within the bounds,
            False otherwise.
        """
        # Base case: An empty tree (or subtree) is a valid BST.
        if not node:
            return True

        # Check if the current node's value violates the bounds.
        # Note: The bounds are exclusive (node.val must be > min_val and < max_val).
        if not (min_val < node.val < max_val):
            return False

        # Recursively check the left and right subtrees.
        # Left subtree: Must be less than the current node's value (new max_val).
        # Right subtree: Must be greater than the current node's value (new min_val).
        is_left_valid = self._isValidBSTHelper(node.left, min_val, node.val)
        is_right_valid = self._isValidBSTHelper(node.right, node.val, max_val)

        # Both subtrees must be valid BSTs.
        return is_left_valid and is_right_valid


# --- Test Harness ---

def run_tests():
    """
    Runs predefined test cases against the Solution.isValidBST method.
    """
    solution = Solution()
    test_cases = [
        # Input list, Expected output
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1, 1], False), # Duplicate value violates strict inequality
        ([5, 4, 6, None, None, 3, 7], False), # 3 is < 5 but in right subtree of 5 via 6
        ([], True), # Empty tree
        ([1], True), # Single node tree
        ([10, 5, 15, None, None, 6, 20], False), # 6 is < 10 but in right subtree
        ([3, 1, 5, 0, 2, 4, 6], True),
        ([32, 26, 47, 19, None, None, 56, None, 27], False), # 27 > 26 but < 32, should be in left subtree
        ([2147483647], True), # Max int value
        ([-2147483648], True), # Min int value
        ([0, -1], True),
    ]

    correct_count = 0
    print("Running tests...")
    for i, (input_list, expected_output) in enumerate(test_cases):
        root = build_tree(input_list)
        # print(f"Test Case {i+1}: Input Tree = {root}") # Optional: Print tree structure
        actual_output = solution.isValidBST(root)
        result = actual_output == expected_output
        print(f"Test {i+1}: {result}")
        if result:
            correct_count += 1

    print(f"\n{correct_count} / {len(test_cases)} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()